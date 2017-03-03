function initMap() {
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

  var centers = [
    [-13733006.90535575, 6177383.5044888975], // Victoria
    [-13703429.316651976, 6317388.117930809], // Vancouver
    [-12697846.960469097, 6630142.913981801], // Calgary 
    [-12634762.20503655, 7082259.731022903],  // Edmonton
    [-11875930.632146042, 6824263.783404279], // Saskatoon
    [-10813486.280065961, 6428871.886617631], // Winnipeg
    [-8838767.56898592, 5419133.259362271],   // Toronto
    [-8425983.765175384, 5688108.060411687],  // Ottawa
    [-8189407.583341518, 5700582.732404122],  // Montreal
    [-7421303.096867932, 5772340.302359437],  // Fredericton
    [-7081032.809360132, 5569718.493209667],  // Halifax
    [-5867338.665139229, 6035201.501836645]   // St, John's
  ];
  map = new ol.Map({
    layers: [
      new ol.layer.Tile({
        source: new ol.source.WMTS({
           attributions: [
            new ol.Attribution({
              html:'<a href="http://www.openstreetmap.org/">OpenStreetMap</a>'
            }),
            ol.source.OSM.DATA_ATTRIBUTION
          ],
          url: 'http://maps.boundlessgeo-dev.com/geoserver/gwc/service/wmts/',
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
          extent: [-20037508.34,-20037508.34,20037508.34,20037508.34]
        })
      })
    ],
    target: 'map',
    ol3Logo: false,
    view: new ol.View2D({
      center: centers[Math.round(Math.random()*centers.length)],
      zoom: 12
    })
  });
}