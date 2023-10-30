from datetime import datetime
import requests
import os
import pandas as pd
import pytz

def fetch_earthquake_data(starttime, endtime, minmagnitude):
    # Define the API endpoint
    url = os.environ.get('API_URL')

    # Initialize variables for pagination
    limit = 20000  # maximum number of records per request (as defined by the API)
    offset = 1  # current record offset
    all_earthquakes = []  # list to store all earthquake data
    
    while True:
        # Define the query parameters with pagination
        params = {
            'format': 'geojson',
            'starttime': starttime,
            'endtime': endtime,
            'minmagnitude': minmagnitude,
            'limit': limit,
            'offset': offset
        }
        
        try:
            # Send the HTTP request and get the response
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises a HTTPError if the response status is 4xx, 5xx
            
            # Extract the earthquake data from the response
            data = response.json()
            features = data['features']
            
            # If no features are returned, we've reached the end of the data
            if not features:
                break  # exit the loop
            
            # Process the earthquake data
            for feature in features:
                properties = feature['properties']
                geometry = feature['geometry']
                
                # Extract the desired properties
                desired_properties = {key: properties[key] for key in ['mag', 'place', 'time', 'type', 'title']}
                # Convert time from milliseconds since the epoch to a datetime object
                desired_properties['time'] = datetime.fromtimestamp(desired_properties['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
                
                # Structure the data in a GeoJSON-like format (i.e., a dictionary with 'properties' and 'geometry' keys)
                earthquake = {
                    'type': 'Feature',
                    'properties': desired_properties,
                    'geometry': geometry
                }
                all_earthquakes.append(earthquake)
            
            # Increase the offset by the limit for the next iteration
            offset += limit

            # Convert GeoJSON to DataFrame for ease to use
            # Extracting necessary information from the geojson data
            data = [(eq['geometry']['coordinates'][0],  # longitude
                    eq['geometry']['coordinates'][1],  # latitude
                    eq['geometry']['coordinates'][2],  # depth
                    eq['properties']['time'],          # time
                    eq['properties']['mag'],           # magnitude
                    eq['properties']['type'],          # type
                    eq['properties']['place'])         # place
                    for eq in all_earthquakes]

            # Creating DataFrame
            df = pd.DataFrame(data, columns=['longitude', 'latitude', 'depth', 'time', 'mag', 'type', 'place'])

            # Convert time to aware datetime objects in UTC
            utc = pytz.UTC
            df['time'] = pd.to_datetime(df['time']).dt.tz_localize(utc)
            
        except requests.RequestException as e:
            print(f'An error occurred: {e}')
            return None  # or handle this in whatever way is appropriate for your script
    
    return df