let map2 = L.map('map2').setView([37.8, -96], 4);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 19,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
	}).addTo(map2); 


	// control that shows state info on hover
	let info2 = L.control();

	info2.onAdd = function (map2) {
		this._div = L.DomUtil.create('div', 'info');
		this.update();
		return this._div;
	};

	info2.update = function (props2) {
		const contents2 = props2 ? `<b>${props2.name}: ${props2.density_change}%` : 'Hover over a state';
		this._div.innerHTML = `<h4>US Population Density<br />% Change 1990 - 2020</h4>${contents2}`;
	};
	
	info2.addTo(map2);


	// get color depending on population density value
	function getColor2(d) {
		return d > 100 ? '#99000d' :
			d > 50  ? '#cb181d' :
			d > 25   ? '#fb6a4a' :
			d > 10   ? '#fcbba1' :
			d < 0   ? '#fee0d2' : '#fff5f0';
	}

	function style2(feature2) {
		return {
			weight: 2,
			opacity: 1,
			color: 'white',
			dashArray: '3',
			fillOpacity: 0.7,
			fillColor: getColor(feature2.properties.density_change)
		};
	}

	function highlightFeature2(e) {
		const layer2 = e.target;

		layer2.setStyle({
			weight: 5,
			color: '#666',
			dashArray: '',
			fillOpacity: 0.7
		});

		layer2.bringToFront();

		info2.update(layer2.feature.properties);
	}

	
	// Population density data //
	let geojson2 = L.geoJson(PopData, {
		style,
		onEachFeature
	}).addTo(map2);

	function resetHighlight2(e) {
		geojson2.resetStyle(e.target);
		info2.update();
	}

	function zoomToFeature2(e) {
		map2.fitBounds(e.target.getBounds());
	}

	function onEachFeature2(feature2, layer2) {
		layer2.on({
			mouseover: highlightFeature,
			mouseout: resetHighlight,
			click: zoomToFeature
		});
	}

	map2.attributionControl.addAttribution('Population data &copy; <a href="https://www.census.gov/data/tables/time-series/dec/density-data-text.html">US Census Bureau</a>');


	let legend2 = L.control({position: 'bottomright'});

	legend2.onAdd = function (_map2) {

		let div2 = L.DomUtil.create('div', 'info legend');
		let grades2 = [-5, 10, 25, 50, 100];
		let labels2 = [];
		let from2, to2;

		for (let i = 0; i < grades2.length; i++) {
			from2 = grades2[i];
			to2 = grades2[i + 1];

			labels2.push(`<i style="background:${getColor(from2 + 1)}"></i> ${from2}${to2 ? `&ndash;${to2}` : '+'}`);
		}

		div2.innerHTML = labels2.join('<br>');
		return div2;
	};

	legend2.addTo(map2);