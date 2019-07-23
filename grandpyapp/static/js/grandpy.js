// Gestion de la fin du chargement de la page web
window.addEventListener("load", function () {
    console.log("Page entièrement chargée");
  
    var boutonElt = document.getElementById("search");
    
    // Ajout d'un gestionnaire pour l'événement click
    boutonElt.addEventListener("click", function () {
      console.log("clic");
      var form = document.querySelector("form");
      console.log(form);
      // Gestion de la soumission du formulaire
      form.addEventListener("submit", function (e) {
          e.preventDefault();
          var query = form.elements.query.value;
          
          if (query == "") {
            alert("Question must be filled out");
            return false;
          }
          console.log("Vous avez choisi la question " + query );
        
          e.preventDefault(); // Annulation de l'envoi des données
          // Envoi des données du formulaire au serveur
          // La fonction callback est ici vide
          /*"https://www.mediawiki.org/w/api.php?action=query&format=json"*/
          ajaxPost("https://www.mediawiki.org/w/api.php", query, function (reponse) {
            // Le film est affiché dans la console en cas de succès
            console.log("Le film " + JSON.stringify(query) + " a été envoyé au serveur");
            },
            true // Valeur du paramètre isJson
        );
      });

      // Affiche de toutes les données saisies ou choisies
      /*form.addEventListener("submit", function (e) {
          var query = form.elements.query.value;
          
          if (query == "") {
            alert("Question must be filled out");
            return false;
          }
        console.log("Vous avez choisi la question " + query );
        
        e.preventDefault(); // Annulation de l'envoi des données

        ajaxGet("https://www.mediawiki.org/w/api.php?action=query&list=search&srsearch="+query+"&utf8=&format=json", function (reponse) {
          console.log(reponse);
          var films = JSON.parse(reponse);
          // Affiche le titre de chaque film
          films.forEach(function (film) {
            console.log(film.titre);
          })
        });
      });*/

      /*function myMap() {
      var mapProp= {
        center:new google.maps.LatLng(51.508742,-0.120850),
        zoom:5,
      };
      var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
      }*/
    });  
});