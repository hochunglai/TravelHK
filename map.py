import folium
import os
from folium import plugins
import time


m = folium.Map(location=[22.3193,114.1694], zoom_start=10, tiles='CartoDB Dark_Matter', zoom_control=False, height="75%")

""" Country Boundary"""
outline= os.path.join('outline.json')
folium.GeoJson(outline, name='outline').add_to(m)

""" Map Style"""
folium.TileLayer('CartoDB Dark_Matter').add_to(m)
folium.TileLayer('CartoDB Positron').add_to(m)


""" Markers """
fg = folium.FeatureGroup(name="Entertainment")
m.add_child(fg)
g1 = plugins.FeatureGroupSubGroup(fg, "Amusement Parks")
m.add_child(g1)

g2 = plugins.FeatureGroupSubGroup(fg, "Buddha")
m.add_child(g2)

folium.Marker([22.31336191779991, 114.04117296041738]).add_to(g1)
folium.Marker([22.235170545306023, 114.17234094648502]).add_to(g1)

folium.Marker([22.25419319394369, 113.9050054607821]).add_to(g2)
folium.Marker([22.474336336713762, 114.20578127384242]).add_to(g2)


m.get_root().html.add_child(folium.Element("""
<div>
<body style="background-color:rgb(38,38,38);">
</body>
<style>
body {
  font-family: "Lato", sans-serif;
}

.sidenav {
  display: none;
  height: 100%;
  width: 250px;
  position: fixed;
  z-index: 900;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  padding-top: 60px;
}

.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  z-index: 900
  color: #818181;
  display: block;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="#">About</a>
  <a href="#">Services</a>
  <a href="#">Clients</a>
  <a href="#">Contact</a>
</div>

<span style="font-size:30px;cursor:pointer; z-index: 900; color:white;" onclick="openNav()">&#9776;</span>

<script>
function openNav() {
  document.getElementById("mySidenav").style.display = "block";
}

function closeNav() {
  document.getElementById("mySidenav").style.display = "none";
}
</script>


</div>
</div>
"""
))
folium.LayerControl().add_to(m)
m.save('map.html')