// // Plot the default route once the page loads
// let defaultURL = "/total";
// d3.json(defaultURL).then(function(line) {
//   console.log(line.y)
//   //var data = [data];
//   let xvalues = line.x;
//   let yvalues = line.y;
//   let trace = {
//         type: 'scatter',
//         x: xvalues,
//         y: yvalues,
//         mode: 'lines',
//         name: 'USA',
//         line: {
//           color: 'blue',
//           width: 5
//         }
//       };
//   let data = [trace];
//   let layout = {autoscaleYAxis: true,
//   title: "United States Count of  Wildfires by State ",
// xaxis: {
//   title: 'Years'
// },
// yaxis:{
//   title: 'Total Count of Wildfires'
// } };

//   var config = {responsive: true}
//   Plotly.plot("scatter", data, layout, config);
// });

// // Update the plot with new data
// function updatePlotly(newdata) {
//   Plotly.restyle("scatter", "x", [newdata.x]);
//   Plotly.restyle("scatter", "y", [newdata.y]);
// }
// // Get new data whenever the dropdown selection changes
// function getData(route) {
//   console.log(route);
//   if (route === "total") {
//     d3.json(`/${route}`).then(function(data) {
//       console.log("newdata", data);
//       updatePlotly(data);
//     })
//   } else {
//     d3.json(`/state/${route}`).then(function(data) {
//       console.log("newdata", data);
//       updatePlotly(data);
//     });
//   };
// }

// Plot the default route once the page loads
let defaultURL = "/total";
d3.json(defaultURL).then(function(line) {
  console.log(line.y)
  //var data = [data];
  let xvalues = line.year;
  let yvalues = line.count;
  let sizevalues = line.size;
  let trace1 = {
        type: 'scatter',
        x: xvalues,
        y: yvalues,
        mode: 'lines',
        name: 'Total Fires',
        line: {
          color: 'blue',
          width: 5
        }
      };
  let trace2 ={
    type: 'scatter',
    x: xvalues,
    y: sizevalues,
    mode: 'lines',
    name: "Average Fire Size",
    yaxis: 'y2',
    overlaying: 'y',
    line: {
      color: "red",
      width: 5,
    }
  };
  let data = [trace1, trace2];
  let layout = {autoscaleYAxis: true,
    title: "Number of Wildfires and Average Fire Size",
    xaxis: {
      title: 'Years'
    },
  yaxis:{
    title: 'Total Count of Wildfires'
  },
  yaxis2: {
    title: 'Average Size of Wildfires',
    overlaying: 'y',
    side: 'right'
  },
  showlegend: true,
  legned: {
    x: 1.1,
    y: 1,
    bgcolor: 'transparent'
  }};

  var config = {responsive: true}
  Plotly.plot("scatter", data, layout, config);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("scatter", "x", [newdata.year], 0);
  Plotly.restyle("scatter", "y", [newdata.count], 0);
  Plotly.restyle("scatter", "x", [newdata.year], 1)
  Plotly.restyle("scatter", "y", [newdata.size], 1);
}
// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  if (route === "total") {
    d3.json(`/${route}`).then(function(data) {
      console.log("newdata", data);
      updatePlotly(data);
    })
  } else {
    d3.json(`/state/${route}`).then(function(data) {
      console.log("newdata", data);
      updatePlotly(data);
    });
  };
}




