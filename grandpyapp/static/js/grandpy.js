// Management of the end of the loading of the web page
window.addEventListener("load", function () {
    console.log("Page entièrement chargée");
  
    var boutonElt = document.getElementById("search");
    
    // Adding a manager for the click event
    boutonElt.addEventListener("click", function () {
      console.log("clic");

      var form = document.querySelector("form");
      // Displays all data entered or selected
      form.addEventListener("submit", function (e) {
          var query = form.elements.query.value;
          if (query == "") {
            alert("Question must be filled out");
            return false;
        }
        console.log("Vous avez choisi la question " + query );
        
        e.preventDefault(); // Cancel sending data

        /*function myMap() {
          var mapProp = {
            zoom:8,
            center:new google.maps.LatLng(51.508742,-0.120850)
          }
          var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

          /*var marker = new google.maps.marker({
            position:new google.maps.LatLng(51.508742,-0.120850),
            map = map
          });
          }*/
        /*ajaxGet("https://www.mediawiki.org/w/api.php?action=query&list=search&srsearch="+query+"&utf8=&format=json", function (reponse) {
        console.log(reponse);
        });*/

        $(document).ready(function() {
          $('#search').click(function(){
              var word = $('#query').val();
              $.ajax({
              url: "/get_coord",
              type: "get",
              data: {word: word},
              success: function(response) {
                for (var i = 0; i < response.features.length; i++) {
                  var coords = response.features[i].geometry.coordinates;
                  var latLng = new google.maps.LatLng(coords[1],coords[0]);
                  var marker = new google.maps.Marker({
                    position: latLng,
                    map: map
                  });
                }
                var mapProp = {
                  zoom:8,
                  center:latLng
                }
                var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

               /*position:new google.maps.LatLng($("#googleMap").html(response.html));*/
              
             },
             error: function(xhr) {
              console.log("erreur summary")
            }
            });
          });
       });
      }); 
    });  
});