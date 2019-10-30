import folium
import pandas

df = pandas.read_excel('india.xlsx')

lat=list(df["Latitude"])
lon=list(df["Longitude"])
city=list(df["City"])


html = """
City name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""
map=folium.Map(location=[20.59,78.96],zoom_start=6,tiles="Mapbox Bright")
fgc=folium.FeatureGroup(name="Cities")
for lt,ln,ct in zip(lat,lon,city):
    iframe = folium.IFrame(html=html % (ct, ct), width=200, height=100)
    fgc.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe), fill_color='green', color='grey', fill_opacity=0.7))
fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=(open('world.json','r', encoding='utf-8-sig').read()),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<= x['properties']['POP2005'] <20000000 else 'red'}))

map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("IndiaMap1.html")
