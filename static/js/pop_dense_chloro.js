//Original pop_dense_chloro.js maps
let map = L.map('map').setView([37.8, -96], 4);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 19,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
	}).addTo(map); 



		//control that shows state info on hover
		let info = L.control();

		info.onAdd = function () {
			this._div = L.DomUtil.create('div', 'info');
			this.update();
			return this._div;
		};

		info.update = function (props) {
			const contents = props ? `<b>${props.name}: ${props.density} people / mi<sup>2</sup>` : 'Hover over a state';
			this._div.innerHTML = `<h4>2020 US Population Density</h4>${contents}`;
		};

		info.addTo(map);

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

			layer.bringToFront();

			info.update(layer.feature.properties);
		}

		// Population density data //
		let geojson = L.geoJson(PopData, {
			style,
			onEachFeature
		}).addTo(map);

		function resetHighlight(e) {
			geojson.resetStyle(e.target);
			info.update();
		}

		function zoomToFeature(e) {
			map.fitBounds(e.target.getBounds());
		}

		function onEachFeature(_feature, layer) {
			layer.on({
				mouseover: highlightFeature,
				mouseout: resetHighlight,
				click: zoomToFeature
			});
		}

		map.attributionControl.addAttribution('Population data &copy; <a href="https://www.census.gov/data/tables/time-series/dec/density-data-text.html">US Census Bureau</a>');


		let legend = L.control({position: 'bottomright'});

		legend.onAdd = function (_map) {

			let div = L.DomUtil.create('div', 'info legend');
			let grades = [0, 10, 20, 50, 100, 200, 300, 500];
			let labels = [];
			let from, to;

			for (let i = 0; i < grades.length; i++) {
				from = grades[i];
				to = grades[i + 1];

				labels.push(`<i style="background:${getColor(from + 1)}"></i> ${from}${to ? `&ndash;${to}` : '+'}`);
			}

			div.innerHTML = labels.join('<br>');
			return div;
		};

		legend.addTo(map);
