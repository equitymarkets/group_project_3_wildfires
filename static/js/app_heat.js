let defaultURL4 = "/heatmap";
let defaultURL5 = "/PopData"
d3.json(defaultURL4).then(function(heat_data) {
  d3.json(defaultURL5).then(function (choro_data){
  console.log(heat_data)
  console.log(choro_data)

let h_map_data = heat_data;

//Create tile layer 
let baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  maxZoom: 18
});

//~~~~*~~~~ HEAT MAP CODE ~~~~*~~~~

let points = {
  // radius should be small ONLY if scaleRadius is true (or small radius is intended)
  // if scaleRadius is false it will be the constant radius used in pixels
  "radius": .8,
  "maxOpacity": 1,
  // scales the radius based on map zoom
  "scaleRadius": true,
  // if set to false the heatmap uses the global maximum for colorization
  // if activated: uses the data maximum within the current map boundaries
  //   (there will always be a red spot with useLocalExtremas true)
  "useLocalExtrema": true,
  // which field name in your data represents the latitude - default "lat"
  latField: 'lat',
  // which field name in your data represents the longitude - default "lng"
  lngField: 'lon',
  // which field name in your data represents the data value - default "value"
  valueField: 'size'
};

let heatmapLayer =  new HeatmapOverlay(points);
    heatmapLayer.setData(h_map_data);



//~~~~*~~~~ POP DEN CHORO MAP CODE ~~~~*~~~~


// get color depending on population density value
function getColor(d) {
  return d > 500 ? '#99000d' :
    d > 300  ? '#cb181d' :
    d > 200  ? '#ef3b2c' :
    d > 100  ? '#fb6a4a' :
    d > 50   ? '#fc9272' :
    d > 20   ? '#fcbba1' :
    d > 10   ? '#fee0d2' : '#fff5f0';
}

function style(feature) {
  return {
    weight: 2,
    opacity: 1,
    color: 'white',
    dashArray: '3',
    fillOpacity: 0.7,
    fillColor: getColor(feature.properties.density)
  };
}

function highlightFeature(e) {
  const layer = e.target;

  layer.setStyle({
    weight: 5,
    color: '#666',
    dashArray: '',
    fillOpacity: 0.7
  });

}

// Population density data //
let geojson = L.geoJson(choro_data, {
  style,
  onEachFeature
})


function resetHighlight(e) {
  geojson.resetStyle(e.target);
}

function onEachFeature(_feature, layer) {
  layer.on({
    mouseover: highlightFeature,
    mouseout: resetHighlight,
  });
}
//~~~~*~~~~ CREATE MAP ~~~~*~~~~

let mymap = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 4,
  layers: [baseLayer, heatmapLayer, geojson]
});

  })
});
//----------------------------------------------------------------------------------------------------------->
