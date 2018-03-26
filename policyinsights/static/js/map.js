var map = L.map('map').setView([39.7318566,-75.4168745], 6);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZHVkYXJldiIsImEiOiJCeUx0Y0kwIn0.Yjsz4P3dQn3fMxCDQRH2rg', {
    maxZoom: 10,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
    id: 'mapbox.light'
}).addTo(map);


// control that shows state info on hover
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
};

info.update = function (props) {
    this._div.innerHTML = '<h4>Sustainability Score</h4>' +  (props ?
		'<b>' + props.name + '</b><br />' + props.score 
		: 'Hover over a location');
};

info.addTo(map);


// legend
var legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
		grades = [80, 60, 40, 20, 0],
		labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
		div.innerHTML +=
			'<i style="background:' + getColor(grades[i]) + '"></i> ' +
			grades[i] + '<br/>';
    }

	return div;
};

legend.addTo(map);


// load data
var geojsonLayer = new L.GeoJSON.AJAX("/static/data/locations.geojson", {style: style, onEachFeature: onEachFeature});
geojsonLayer.addTo(map);

function getColor(score) {
    return score >= 80 ? '#a63603' :
           score >= 60 ? '#e6550d' :
           score >= 40 ? '#fd8d3c' :
           score >= 20 ? '#fdbe85' :
                         '#feedde';
}

function style(feature) {
    return {
		fillColor: getColor(feature.properties.score),
		weight: 2,
		opacity: 1,
		color: 'white',
		fillOpacity: 0.7
    };
}

function onEachFeature(feature, layer) {
    layer.on({
        'mouseover': highlightFeature,
  		'mouseout': resetHighlight,
  		'click': function() {
			window.location.href = '/l/' + feature.properties.slug;
		}
    });
}

function highlightFeature(e) {
    var layer = e.target;
    info.update(layer.feature.properties);
}

function resetHighlight(e) {
    info.update();
}
