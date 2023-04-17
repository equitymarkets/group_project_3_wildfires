// let defaultURL4 = "/fire_heatmap";

// let myMap = L.map("heat", {
//     center: [39.8283, -98.5795],
//     zoom: 5
// });

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(myMap);


//Create map object
let myMap = L.map("map", {
    center: [39.8283, -98.5795],
    zoom: 5
});

//Create tile layer 
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);


