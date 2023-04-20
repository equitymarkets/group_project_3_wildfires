//Store our API route as queryUrl. 
let defaultURL4 = "/geojson";
d3.json(defaultURL4).then(function (data) {
  // Console log the data retrieved 
    console.log(data.features);
    // Once we get a response, send the data.features object to the createFeatures function.
    createFeatures(data.features);
    });

//Create map object
let myMap = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 5
});

//Create tile layer 
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Function to determine marker size
function markerSize(magnitude) {
  return magnitude * 3000;
};

// Function to determine marker color by depth
function chooseColor(depth){
  if (depth < 20) return "#00FF00";
  else if (depth < 40) return "greenyellow";
  else if (depth < 60) return "yellow";
  else if (depth < 80) return "orange";
  else if (depth < 100) return "orangered";
  else return "#FF0000";
}

// Create a map that plots all the fires from your dataset based on their longitude and latitude
function createFeatures(_fire_props) {

// Define a function that we want to run once for each feature in the features array.
  // Give each feature a popup that describes the place and time of the fire.
  function onEachFeature(feature, layer) {
    layer.bindPopup(`<h3>Place:${feature.properties.place}</h3><hr><p>Time:${new Date(feature.properties.time)}</p></h3><hr><p>Magnitude: ${feature.properties.mag}</p>`);
  }
  // Create a GeoJSON layer that contains the features array on the fire object.
  // Run the onEachFeature function once for each piece of data in the array.
  var fires = L.geoJSON(_fire_props, {
    onEachFeature: onEachFeature,

    // Point to layer used to alter markers
    pointToLayer: function (feature, latlng) {
      
      // Determine the style of markers based on properties
      var markers = {
        radius: markerSize(7*feature.properties.mag),
        fillColor: chooseColor(feature.geometry.coordinates[2]),
        color: "black",
        weight: 1,
        opacity: 1,
        stroke: true,
        fillOpacity: 0.8
      };
      return L.circle(latlng, markers);
    }
  });
  // Send our fires layer to the createMap function
  createMap(fires);
}

function createMap(fires) {
  
  // Create the base layers.
  var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })


  // Create our map, giving it the grayscale map and fires layers to display on load.
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street, fires]
  });

  // Add legend
  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function () {
  
      var div = L.DomUtil.create('div', 'info legend'),
      depth = [-10, 10, 30, 50, 70, 90];

      div.innerHTML+='Depth<br><hr>'
  
      // Loop through density intervals 
      for (var i = 0; i < depth.length; i++) {
          div.innerHTML +=
          '<i style="background:' + chooseColor(depth[i] + 1) + '">&nbsp&nbsp&nbsp&nbsp</i> ' +
          depth[i] + (depth[i + 1] ? '&ndash;' + depth[i + 1] + '<br>' : '+');
  }
  
  return div;
  };
  
  legend.addTo(myMap);
};