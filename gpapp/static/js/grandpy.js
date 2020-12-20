function postFormData(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

const gpResponseEl = document.getElementById("gp-response");

function addElement (data) {
    let tag = document.createElement("p");
    tag.setAttribute("class", "gp-text text-center text-md-left mt-3 text-white mx-auto mt-md-4 fs-md-5")
    let text = document.createTextNode(data);
    tag.appendChild(text);
    gpResponseEl.appendChild(tag)
}

// Initialize Google Maps
function initMap(){}

function displayMap(lat, lng, zoom) {
    const gmaps = document.createElement("div");
    gmaps.setAttribute("class", "gpmap rounded mx-auto mt-4")
    gpResponseEl.appendChild(gmaps);
    const location = {lat: lat, lng: lng};
    const map = new google.maps.Map(gmaps, {
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

const formEl = document.querySelector("#user-text-form");

formEl.addEventListener("submit", function (event) {
    const userInput = new FormData(event.target)
    addElement(userInput.get("userText"))
    event.preventDefault();
         //Send form to server
        postFormData("/grandpy", userInput)
            .then(response => {
                if (response.place_info === null && response.address !== null) {
                    addElement(response.no_wiki_info);
                    addElement(response.address);
                    displayMap(response.lat, response.lng, 14);
                } else if (response.place_info === null && response.address === null) {
                    addElement(response.wrong_question);
                } else {
                    addElement(response.first_answer);
                    addElement(response.address);
                    addElement(response.second_answer);
                    addElement(response.place_info);
                    displayMap(response.lat, response.lng, 14);
                }
            })
})