function initOpenLayers() {
  var projection = ol.proj.get('EPSG:900913');
  var projectionExtent = projection.getExtent();
  var size = ol.extent.getWidth(projectionExtent) / 256;
  var n = 26;
  var resolutions = new Array(n);
  var matrixIds = new Array(n);
  for (var z = 0; z < n; ++z) {
    // generate resolutions and matrixIds arrays for this WMTS
    resolutions[z] = size / Math.pow(2, z);
    matrixIds[z] = 'EPSG:900913:' + z;
  }

  // var map = new ol.Map({
  //     target: 'map',
  //     layers: [
  //       new ol.layer.Tile({
  //         source: new ol.source.MapQuest({layer: 'sat'})
  //       })
  //     ],
  //     view: new ol.View2D({
  //       center: ol.proj.transform([37.41, 8.82], 'EPSG:4326', 'EPSG:3857'),
  //       zoom: 4
  //     })
  //   });
  map = new ol.Map({
    layers: [
      new ol.layer.Tile({
        source: new ol.source.WMTS({
          url: 'http://demo.opengeo.org/geoserver/gwc/service/wmts/',
          layer: 'osm:osm',
          matrixSet: 'EPSG:900913',
          format: 'image/png',
          projection: projection,
          tileGrid: new ol.tilegrid.WMTS({
            origin: ol.extent.getTopLeft(projectionExtent),
            resolutions: resolutions,
            matrixIds: matrixIds
          }),
          style: '_null',
          extent: [-13703362.89946257, 6287709.945851705, -13666596.688857399, 6318131.883109205]
        })
      })
    ],
    target: 'map',
    ol3Logo: false,
    view: new ol.View2D({
      center: [-13684979.794159984, 6302920.914480455],
      zoom: 11
    })
  });
}