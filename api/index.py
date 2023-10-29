from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/spatial_concerntration')
def spatial_concerntration():
    return render_template('spatial_concerntration.html')

@app.route('/spatial_concerntration_map_1')
def spatial_concerntration_map_1():
    return render_template('spatial_concerntration_1_Map_6.html')
@app.route('/spatial_concerntration_map_2')
def spatial_concerntration_map_2():
    return render_template('spatial_concerntration_2_Map_7.html')
@app.route('/spatial_concerntration_map_3')
def spatial_concerntration_map_3():
    return render_template('spatial_concerntration_3_Map_2.html')
@app.route('/spatial_concerntration_map_4')
def spatial_concerntration_map_4():
    return render_template('spatial_concerntration_4_Map_4.html')


@app.route('/temporal_fluctuations')
def temporal_fluctuations():
    return render_template('temporal_fluctuations.html')

@app.route('/temporal_fluctuations_map_1')
def temporal_fluctuations_map_1():
    return render_template('temporal_fluctuations_1_Map_8.html')

@app.route('/temporal_fluctuations_map_2')
def temporal_fluctuations_map_2():
    return render_template('temporal_fluctuations_2_Map_11.html')

@app.route('/temporal_fluctuations_map_3')
def temporal_fluctuations_map_3():
    return render_template('temporal_fluctuations_3_Time_series_2.html')

@app.route('/temporal_fluctuations_map_4')
def temporal_fluctuations_map_4():
    return render_template('temporal_fluctuations_4_Time_series_1.html')

@app.route('/depth_magnitude_relationship')
def depth_magnitude_relationship():
    return render_template('depth_magnitude.html')

@app.route('/depth_magnitude_relationship_map_1')
def depth_magnitude_relationship_map_1():
    return render_template('depth_magnitude_relationship_map_1.html')
@app.route('/depth_magnitude_relationship_map_2')
def depth_magnitude_relationship_map_2():
    return render_template('depth_magnitude_relationship_map_2.html')
@app.route('/depth_magnitude_relationship_map_3')
def depth_magnitude_relationship_map_3():
    return render_template('depth_magnitude_relationship_map_3.html')
@app.route('/depth_magnitude_relationship_map_4')
def depth_magnitude_relationship_map_4():
    return render_template('depth_magnitude_relationship_map_4.html')

@app.route('/regional_variations')
def regional_variations():
    return render_template('regional_variations.html')

@app.route('/regional_variations_map_1')
def regional_variations_map_1():
    return render_template('regional_variations_map_1.html')
@app.route('/regional_variations_map_2')
def regional_variations_map_2():
    return render_template('regional_variations_map_2.html')
@app.route('/regional_variations_map_3')
def regional_variations_map_3():
    return render_template('regional_variations_map_3.html')
@app.route('/regional_variations_map_4')
def regional_variations_map_4():
    return render_template('regional_variations_map_4.html')
@app.route('/regional_variations_map_5')
def regional_variations_map_5():
    return render_template('regional_variations_map_5.html')
@app.route('/regional_variations_map_6')
def regional_variations_map_6():
    return render_template('regional_variations_map_6.html')

# @app.route('/scatterplot1')
# def scatterplot1():
#     return render_template('scatterplot_1.html')

# @app.route('/scatterplot2')
# def scatterplot2():
#     return render_template('scatterplot_2.html')



# @app.route('/realtimemap',  methods=['GET', 'POST'])
# def realTimeMap():
#     start_time = request.form.get('start_date', '')
#     end_time = request.form.get('end_date', '')

#     url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=100"
#     if start_time and end_time:
#         url += f"&starttime={start_time}&endtime={end_time}"

#     # Fetch the earthquake data
#     response = requests.get(url)
#     print(response.json())
#     data = response.json()
#     earthquakes = data['features']
#     recent_earthquakes = earthquakes[:5]

#     # Create a map centered around coordinates
#     m = folium.Map(location=[20,0], zoom_start=2, control_scale=True)

#     # Add earthquake data to the map
#     for quake in earthquakes:
#         lat = quake['geometry']['coordinates'][1]
#         lon = quake['geometry']['coordinates'][0]
#         magnitude = quake['properties']['mag']
#         popup_content = f"<strong>Magnitude:</strong> {magnitude}<br><strong>Location:</strong> {quake['properties']['place']}<br><strong>Time:</strong> {datetime.utcfromtimestamp(quake['properties']['time']/1000).strftime('%Y-%m-%d %H:%M:%S')}"
#         popup = folium.Popup(popup_content, max_width=300)
#         folium.CircleMarker(
#             location=[lat, lon],
#             radius=magnitude*5,
#             color='red',
#             fill=True,
#             fill_color='red',
#             popup=popup
#         ).add_to(m)

#     # Render the map
#     return render_template('map.html', m=m._repr_html_(), recent_earthquakes=recent_earthquakes, start_time=start_time, end_time=end_time)
# # Custom filter to format the timestamp
# @app.template_filter('datetimeformat')
# def datetimeformat(value):
#     return datetime.utcfromtimestamp(value/1000).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)