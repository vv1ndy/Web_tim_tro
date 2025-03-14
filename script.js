async function fetchRooms() {
    let response = await fetch("/rooms");
    let rooms = await response.json();
    return rooms;
}

async function initMap() {
    let map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 10.762622, lng: 106.660172 }, // Mặc định ở TP.HCM
        zoom: 12
    });

    let rooms = await fetchRooms();

    rooms.forEach(room => {
        if (room.location) {
            let marker = new google.maps.Marker({
                position: { lat: room.location.lat, lng: room.location.lng },
                map: map,
                title: room.name
            });

            let infoWindow = new google.maps.InfoWindow({
                content: `<h3>${room.name}</h3><p>Giá: ${room.price} VND</p>`
            });

            marker.addListener("click", () => {
                infoWindow.open(map, marker);
            });
        }
    });
}

