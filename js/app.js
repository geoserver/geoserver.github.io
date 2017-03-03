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
    [-13733006, 6177383], // Victoria
    [-13703429, 6317388], // Vancouver
    [-12697846, 6630142], // Calgary 
    [-12634762, 7082259],  // Edmonton
    [-11875930, 6824263], // Saskatoon
    [-10813486, 6428871], // Winnipeg
    [-8838767, 5419133],   // Toronto
    [-8425983, 5688108],  // Ottawa
    [-8189407, 5700582],  // Montreal
    [-7421303, 5772340],  // Fredericton
    [-7081032, 5569718],  // Halifax
    [-5867338, 6035201]   // St, John's
    [3473167, -3056995],// Lobamba
    [1385683, 5146013],// Vatican City
    [682388, 6379291],// Luxembourg
    [13472994, 1648946],// Quezon City
    [13469657, 1637443],// Pasay City
    [12703800, 2578208],// Shenzhen
    [13141048, 4411534],// Zibo
    [-6253149, -4144342],// Montevideo
    [-10380957, 5618676],// Minneapolis
    [-13619041, 6035935],// Seattle
    [-12475791, 3967458],// Phoenix
    [-13044633, 3871697],// San Diego
    [-13627416, 4546872],// San Francisco
    [-13155951, 4027717],// Los Angeles
    [-11686983, 4828395],// Denver
    [-10045685, 4669802],// St. Louis
    [-10780397, 3871697],// Dallas
    [-10613414, 3480679],// Houston
    [-7977368, 1201719],// Maracaibo
    [-7911694, 5210827],// Boston
    [-9179468, 3242537],// Tampa
    [-8930723, 2973039],// Miami
    [-9395576, 4006260],// Atlanta
    [-9768508, 5135837],// Chicago
    [-8572865, 4707571],// "Washington
    [-8235634, 4975819],// New York
    [-8368102, 4866221],// Philadelphia
    [-7449387, 1175785],// Caracas
    [-6848044, 1192665],// Port-of-Spain
    [-9248646, 5210827],// Detroit
    [135900, 684128],// Lome
    [1133196, 4411652],// Tunis
    [3396878, 6522008],// Kiev
    [6052061, 2810379],// Abu Dhabi
    [6153521, 2904260],// Dubai
    [6499199, 4572364],// Ashgabat
    [7713660, 5058715],// Tashkent
    [11782953, 2396085],// Hanoi
    [11877019, 1207390],// Ho Chi Minh City
    [3148269, -1737039],// Lusaka
    [3455664, -2016004],// Harare
    [13979441, -956390],// Dili
    [18736922, -2006361],// Port-Vila
    [-9709227, 1586149],// Tegucigalpa
    [-6475124, 758977],// Georgetown
    [-2443464, 9387963],// Reykjavk
    [-8052627, 2101201],// Port-au-Prince
    [-13210, 6710566],// London
    [3229161, 5028128],// Istanbul
    [3658230, 4855656],// Ankara
    [3626942, 35467],// Kampala
    [2124128, 6024393],// Budapest
    [4920838, 1730340],// Sanaa
    [3346106, -217298],// Kigali
    [-6141165, 650678],// Paramaribo
    [-410245, 4924528],// Madrid
    [235408, 1519049],// Niamey
    [242835, 5069332],// Barcelona
    [2905216, 5533057],// Bucharest
    [4137531, 4332579],// Aleppo
    [4040680, 3962124],// Damascus
    [683504, 5814067],// Geneva
    [951566, 6004639],// Zrich
    [2014369, 8257013],// Stockholm
    [7655873, 4658844],// Dushanbe
    [11189245, 1545773],// Bangkok
    [3465746, -3038352],// Mbabane
    [-8577390, -1350951],// Lima
    [-6416839, -2911955],// Asuncion
    [-9603581, 1363349],// Managua
    [-1018218, 4682309],// Lisbon
    [-1945316, 1656696],// Dakar
    [-1473442, 946549],// Freetown
    [3515472, 538308],// Juba
    [3621471, 1757293],// Khartoum
    [4365644, 2453852],// Jeddah
    [475329, 6814610],// The Hague
    [1196465, 8381645],// Oslo
    [1615798, 5789213],// Ljubljana
    [1905453, 6131848],// Bratislava
    [5206501, 2831931],// Riyadh
    [5736623, 2910982],// Doha
    [8144655, 3988849],// Islamabad
    [8276390, 3705941],// Lahore
    [7457077, 2860023],// Karachi
    [9497188, 3213546],// Kathmandu
    [13519534, 2878032],// Taipei
    [2051956, -4017805],// Cape Town
    [2919900, -3390927],// Bloemfontein
    [3142269, -2962586],// Pretoria
    [3120069, -3019915],// Johannesburg
    [3448462, -3485960],// Durban
    [16385394, -1058431],// Port Moresby
    [17805526, -1055416],// Honiara
    [547101, 6864007],// Amsterdam
    [-8853793, 1002635],// Panama City
    [-848066, 3975474],// Casablanca
    [-761025, 4032200],// Rabat
    [2144715, 5231037],// Podgorica
    [3212425, 5942894],// Chisinau
    [3627592, -2993302],// Maputo
    [3374547, 8386605],// St. Petersburg
    [4187124, 7509620],// Moscow
    [5049978, 230328],// Mogadishu
    [6522577, 2706360],// Muscat
    [8899992, 769968],// Sri Jawewardenepura Kotte
    [8889724, 773552],// Colombo
    [14137328, 4518618],// Seoul
    [13421784, 1854572],// Baguio City
    [13467462, 1643846],// Manila
    [-11168899, 2958505],// Monterrey
    [-11502863, 2352806],// Guadalajara
    [-10931794, 2161047],// Puebla
    [-11035427, 2207325],// Mexico City
    [377326, 718995],// Lagos
    [948229, 1345927],// Kano
    [2337492, 6845809],// Warsaw
    [13998731, 4724735],// Pyongyang
    [11901686, 6093326],// Ulaanbaatar
    [19456785, -5056688],// Wellington
    [1901731, -2580100],// Windhoek
    [4371115, -758539],// Dar es Salaam
    [3979672, -689662],// Dodoma
    [19454532, -4417950],// Auckland
    [831219, 5928485],// Bern
    [-1469417, 3142222],// Laayoune
    [838389, 1015633],// Abuja
    [10981455, 398997],// Medan
    [-695841, 7045207],// Dublin
    [-1736401, 1330351],// Bissau
    [-1202212, 704363],// Monrovia
    [1585530, 4989060],// Naples
    [1389413, 5145697],// Rome
    [2356186, 5261378],// Pristina
    [3999860, 3757007],// Amman
    [1024480, 5696124],// Milan
    [2818234, 7300654],// Vilnius
    [2682795, 7749910],// Riga
    [8302570, 5292968],// Bishkek
    [11320973, 352908],// Kuala Lumpur
    [11553856, 4308601],// Lanzhou
    [12057915, 2610498],// Nanning
    [11879803, 3071343],// Guiyang
    [11865882, 3448002],// Chongqing
    [12956068, 4855896],// Beijing
    [13280203, 3009233],// Fuzhou
    [12615065, 2649796],// Guangzhou
    [12661787, 2638167],// Dongguan
    [4098194, -142656],// Nairobi
    [3059423, -3416013],// Maseru
    [5289309, -2144894],// Antananarivo
    [11974422, -775359],// Bandung
    [11891981, -688449],// Jakarta
    [12551148, -808924],// Surabaya
    [-8896874, -246978],// Guayaquil
    [-8738802, -23715],// Quito
    [-8413188, 700148],// Medellin
    [-9360410, 1111764],// San Jose
    [-9930253, 1541189],// San Salvador
    [-8545711, 2034865],// Kingston
    [-8247136, 512438],// Bogota
    [-8516153, 378921],// Cali
    [-9168955, 2648220],// Havana
    [-6833571, 1723915],// Roseau
    [1675046, 1358803],// Ndjamena
    [977749, 417748],// Malabo
    [3478513, 3510223],// Cairo
    [3333801, 3659006],// Alexandria
    [4334037, 1727646],// Asmara
    [4803213, 1299652],// Djibouti
    [965698, 6463608],// Frankfurt
    [1112978, 7085757],// Hamburg
    [1781111, 5748357],// Zagreb
    [1288305, 6128824],// Munich
    [1610128, 6461058],// Prague
    [1491636, 6895388],// Berlin
    [2752712, 8274761],// Tallinn
    [5340703, 3423036],// Kuwait
    [9748588, 5435616],// Urumqi
    [11321408, 324527],// Putrajaya
    [12121918, 4066053],// Xian
    [12528241, 4562058],// Taiyuan
    [12720263, 3578579],// Wuhan
    [12575545, 3274454],// Changsha
    [11584804, 3590217],// Chengdu
    [11430065, 2884581],// Kunming
    [12652923, 4130899],// Zhengzhou
    [13742171, 5132101],// Shenyeng
    [13023609, 4394169],// Jinan
    [13046429, 4740593],// Tianjin
    [12899485, 3335225],// Nanchang
    [13222309, 3770133],// Nanjing
    [13518033, 3661144],// Shanghai
    [13377048, 3535973],// Hangzhou
    [14743261, 4081260],// Hiroshima
    [13952566, 5444876],// Changchun
    [12225114, 4961462],// Baotou
    [14098395, 5740684],// Harbin
    [15733685, 5323687],// Sapporo
    [15111404, 4168222],// Kyoto
    [15079137, 4130227],// Osaka
    [15556838, 4257632],// Tokyo
    [1704638, -482224],// Kinshasa
    [3760739, -1572300],// Lilongwe
    [-10077632, 1645799],// Guatemala
    [-7781458, 2092872],// Santo Domingo
    [-1846979, 1511634],// Banjul
    [1052855, 42901],// Libreville
    [-24341, 619013],// Accra
    [8596988, 3333957],// Delhi
    [8593862, 3324835],// New Delhi
    [8736131, 1967662],// Hyderabad
    [8633724, 1456526],// Bangalore
    [8220728, 2099908],// Pune
    [8804041, 2412388],// Nagpur
    [8110186, 2157165],// Mumbai
    [19864039, -2053123],// Suva
    [259529, 6252601],// Paris
    [-7866835, -3954929],// Santiago
    [-7973031, -3901387],// Valparaiso
    [-1778366, 2047667],// Nouakchott
    [-890776, 1419997],// Bamako
    [2641764, 4577345],// Athens
    [2385962, 5160980],// Skopje
    [1467192, 3881043],// Tripoli
    [3952706, 4011885],// Beirut
    [4985871, 5120166],// Tbilisi
    [3870363, 3774070],// Tel Aviv-Yafo
    [4941686, 3940599],// Baghdad
    [4307848, 1009994],// Addis Ababa
    [2775437, 8439364],// Helsinki
    [7951303, 6653395],// Astana
    [5724315, 4255841],// Tehran
    [6631085, 4338108],// Mashhad
    [8438912, 3113864],// Jaipur
    [8940964, 3056408],// Kanpur
    [9832041, 2571291],// Kolkata
    [9476415, 2952944],// Patna
    [8936511, 1470237],// Chennai
    [8079352, 2635888],// Ahmedabad
    [8108299, 2415972],// Surat
    [11421377, 2033650],// Vientiane
    [1701267, -474350],// Brazzaville
    [1398344, 7495075],// Kbenhavn
    [-1523093, 1066192],// Conakry
    [-449952, 593289],// Abidjan
    [-587266, 760816],// Yamoussoukro
    [-5396988, -161214],// Belem
    [-5334207, -1779420],// Brasilia
    [-5699775, -3509730],// Porto Alegre
    [-5490493, -2927182],// Curitiba
    [-4294920, -417531],// Fortaleza
    [-4283789, -1456079],// Salvador
    [-4812003, -2622718],// Rio de Janeiro
    [2278269, 5593321],// Belgrade
    [12794314, 544269],// Bandar Seri Begawan
    [-7264656, -2159760],// Sucre
    [-5488270, -1888032],// Goiania
    [-6501000, -4109729],// Buenos Aires
    [-5190490, -2699486],// Sao Paulo
    [-3887004, -901749],// Recife
    [-9881505, 1950183],// Belmopan
    [2065899, 486563],// Bangui
    [1281811, 430983],// Yaounde
    [2206227, 5060774],// Tirana
    [482165, 6592205],// Brussels
    [4955009, 4892585],// Yerevan
    [5550420, 4923833],// Baku
    [7701228, 4098656],// Kabul
    [11679049, 1294762],// Phnom Penh
    [10064020, 2719934],// Dhaka
    [1473033, -987579],// Luanda
    [-7586638, -1862237],// La Paz
    [-6636481, 1471388],// Bridgetown
    [291281, 723263],// Porto-Novo
    [280307, 714149],// Cotonou
    [339369, 4406402],// Algiers
    [2595381, 5264192],// Sofia
    [1821709, 6140519],// Vienna
    [3068486, 7151603],// Minsk
    [9978569, 3182690],// Thimphu
    [10218909, 2551425],// Chittagong
    [2884504, -2832364],// Gaborone
    [16600967, -4202410],// Canberra
    [16829640, -4017805],// Sydney
    [16138328, -4553759],// Melbourne
    [-169948, 1388103],// Ouagadougou
    [2046386, 5442262],// Sarajevo
    [10699659, 2245626],// Naypyidaw
    [10705008, 1895846],// Rangoon
    [3268340, -376041],// Bujumbura
    [17605174, 771834],// Palikir
    [19077934, 792735],// Majuro
    [19950305, -951580],// Funafuti
    [1387783, 5452629],// San Marino
    [14986558, 835875],// Melekeok
    [-1074513, 3013847],// Bir Lehlou
    [824533, 5425239],// Monaco
    [1059390, 5963928],// Vaduz
    [19260227, 148979],// Tarawa
    [4813481, -1312057],// Moroni
    [168814, 5236174],// Andorra
    [-6814095, 1476677],// Kingstown
    [-6790489, 1574442],// Castries
    [-6981625, 1956011],// Basseterre
    [-19505464, -2408402],// Nukualofa
    [4905327, 1069189],// Hargeysa
    [11560960, 144168],// Singapore
    [6172664, -514478],// Victoria
    [749550, 37114],// Sao Tome
    [-19117858, -1556043],// Apia
    [6400870, -2292782],// Port Louis
    [1615770, 4286833],// Valletta
    [8181976, 464245],// Male
    [3919183, 3734258],// Jerusalem
    [-6873048, 1351699],// Saint George's
    [12710800, 2548415],// Hong Kong
    [-2617865, 1679601],// Praia
    [5630879, 3028356],// Manama
    [-8610567, 2885990],// Nassau
    [-6885114, 1934569],// Saint John's
    [3714356, 4186554],// Nicosia
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
