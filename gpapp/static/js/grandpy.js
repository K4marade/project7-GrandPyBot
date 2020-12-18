let form = document.querySelector("#user-text-form");

function postFormData(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}
function addElement (data) {
    let tag = document.createElement("p");
    // let line = document.createElement("br")
    let text = document.createTextNode(data);
    tag.appendChild(text);
    let element = document.getElementById("gp-response");
    element.appendChild(tag)
}

form.addEventListener("submit", function (event) {
    event.preventDefault();
         //Send form to server
        postFormData("/grandpy", new FormData(form))
            .then(response => {
                if (response.place_info === null && response.address !== null) {
                    dataElement =
                    addElement(response.no_wiki_info);
                    addElement(response.address);
                    displayMap(response.lat, response.lng, 15);
                } else if (response.place_info === null && response.address === null) {
                    addElement(response.wrong_question);
                } else {
                    addElement(response.first_answer);
                    addElement(response.address);
                    addElement(response.second_answer);
                    addElement(response.place_info);
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