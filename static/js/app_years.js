// Plot the default route once the page loads
let defaultURL = "/total";
d3.json(defaultURL).then(function(line) {
  console.log(line.y)
  //var data = [data];
  let xvalues = line.x;
  let yvalues = line.y;
  let trace = {
        type: 'scatter',
        x: xvalues,
        y: yvalues,
        mode: 'lines',
        name: 'USA',
        line: {
          color: 'blue',
          width: 5
        }
      };
  let data = [trace];
  let layout = {autoscaleYAxis: true,
  title: "United States Count of  Wildfires by State ",
xaxis: {
  title: 'Years'
},
yaxis:{
  title: 'Total Count of Wildfires'
} };


  Plotly.plot("scatter", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("scatter", "x", [newdata.x]);
  Plotly.restyle("scatter", "y", [newdata.y]);
}
// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}




