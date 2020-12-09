let form = document.querySelector("#user-text-form");

function postFormData(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

let element = document.getElementById("response");

form.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log(event);

         //Send form to server
        postFormData("/grandpy", new FormData(form))
            .then(response => {
                console.log(response)
                if (response.place_info === null && response.address !== null) {
                    element.innerHTML = response.no_wiki_info + response.address;
                    displayMap(response.lat, response.lng, 15);
                } else if (response.place_info === null && response.address === null) {
                   element.innerHTML = response.wrong_question;
                } else {
                    element.innerHTML = response.first_answer + "<br>"
                        + response.address + "<br>" + "<br>"
                        + response.second_answer + "<br>"
                        + response.place_info;
                    displayMap(response.lat, response.lng, 15)
                }
            })

})

// Initialize Google Maps
function initMap(){}

function displayMap(lat, lng, zoom) {
    const location = {lat: lat, lng: +lng};
    const map = new google.maps.Map(document.getElementById("map"), {
        center: location,
        zoom: zoom,
    });

    if(displayMap) {
        const marker = new google.maps.Marker({
            position: location,
            map: map
        });
    }
}