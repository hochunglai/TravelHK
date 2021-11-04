import folium
import os


m = folium.Map(location=[22.3193,114.1694], zoom_start=11, tiles='CartoDB Dark_Matter', zoom_control=False)

outline= os.path.join('outline.json')

folium.GeoJson(outline, name='outline').add_to(m)


folium.TileLayer('CartoDB Dark_Matter').add_to(m)
folium.TileLayer('CartoDB Positron').add_to(m)

folium.LayerControl().add_to(m)

folium.Marker(
    location=[22.3193,114.1694], popup="<i>Mt. Hood Meadows</i>"
).add_to(m)

m.save('map.html')