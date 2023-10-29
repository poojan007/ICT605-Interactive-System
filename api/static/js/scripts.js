/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

$(document).ready(function() {
    $("#start-quiz").click(function() {
        $("#quiz-container").show();
        $("#quiz-cover").hide();
    });

    $("#submit-quiz").click(function() {
      let score = 0;
  
      // Question 1
      const answer1 = $("input[name='q1']:checked").val();
      if (answer1 === "thegroundshakes") {
        score++;
      }

      // Question 2
      const answer2 = $("input[name='q2']:checked").val();
      if(answer2 === "onlandandunderthesea") {
        score++;
      }

      // Question 3
      const answer3 = $("input[name='q3']:checked").val();
      if(answer3 === "atatectonicplateboundary") {
        score++;
      }

      // Question 4
      const answer4 = $("input[name='q4']:checked").val();
      if(answer4 === "earthquakeresistantbuildings") {
        score++;
      }

      // Question 5
      const answer5 = $("input[name='q5']:checked").val();
      if(answer5 === "Richter") {
        score++;
      }
  
      // Display the result
      $("#quiz-result").html("<h3>Your score: <label class='fw-bolder'>" + score + "</label>/5</h3>");

      if(score > 3) {
        $("#success").show();
        $("#fail").hide();
      } else {
        $("#success").hide();
        $("#fail").show();
      }
    });

        });



