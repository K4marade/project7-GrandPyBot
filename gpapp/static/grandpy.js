let form = document.querySelector("#user-text-form");

        function postFormData(url, data) {
            return fetch(url, {
                method: "POST",
                body: data
            })
            .then(response => response.json())
            .catch(error => console.log(error));
        }

        form.addEventListener("submit", function (event) {
            event.preventDefault();
            console.log("Votre question a bien été envoyée");

            //Envoyer le formulaire au serveur
            postFormData("/question", new FormData(form))
            .then(response => {
                document.getElementById("response").innerHTML = "Bonjour " + response;
            })
        })