// Gestion de la fin du chargement de la page web
window.addEventListener("load", function () {
    console.log("Page entièrement chargée");
  
    var boutonElt = document.getElementById("search");
    
    // Ajout d'un gestionnaire pour l'événement click
    boutonElt.addEventListener("click", function () {
      console.log("clic");

      var form = document.querySelector("form");
      // Affiche de toutes les données saisies ou choisies
      form.addEventListener("submit", function (e) {
          var query = form.elements.query.value;
          if (query == "") {
            alert("Question must be filled out");
            return false;
        }
        console.log("Vous avez choisi la question " + query );
        
        e.preventDefault(); // Annulation de l'envoi des données

        function myMap() {
          var mapProp = {
            zoom:8,
            center:new google.maps.LatLng(51.508742,-0.120850)
          }
          var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

          /*var marker = new google.maps.marker({
            position:new google.maps.LatLng(51.508742,-0.120850),
            map = map
          });*/
          }
        /*ajaxGet("https://www.mediawiki.org/w/api.php?action=query&list=search&srsearch="+query+"&utf8=&format=json", function (reponse) {
        console.log(reponse);
        });*/
      });

      
    });  
});