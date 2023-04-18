let defaultURL3 = "/fire_cause";
d3.json(defaultURL3).then(function(pie) {
  console.log(pie)
  //var data = [data];
  let xvalues3 = pie.x;
  let yvalues3= pie.y;
  let trace3 = {
    values: pie.y,
    labels: pie.x,
    type: 'pie'
  };

  let data = [trace3];
  let layout = {autoscaleYAxis: true,
  title: "Top 10 Causes of Wildfires in United States",
 };
  Plotly.plot("pie", data, layout);
});

// Update the plot with new data
function updatePlotly3(newdata) {
  Plotly.restyle("pie", "x", [newdata.x]);
  Plotly.restyle("pie", "y", [newdata.y]);
}
// Get new data whenever the dropdown selection changes
function getData3(route) {
    console.log(route);
    if (route === "fire_cause") {
      d3.json(`/${route}`).then(function(data) {
      console.log("newdata", data);
      updatePlotly3(data);
      });
    } else {  
      d3.json(`/fire_cause/${route}`).then(function(data) {
      console.log("newdata", data);
      updatePlotly3(data);
      });
    }
  
  }