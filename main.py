import folium

valaam_map = folium.Map(
    location=[61.36699446527614, 30.93333291785637],    # Valaam cords
    zoom_start=12
)

folium.Marker(location=[61.36699446527614, 30.93333291785637], popup=folium.Popup(folium.IFrame(html="""<img src='img/valaam-1.jpg'>""", width=600, height=200)), tooltip='Жмякни на меня!', icon=folium.Icon(color='blue')).add_to(valaam_map)

folium.Marker(location=[61.38943181703889, 31.006380133676704], popup="Казанский скит", tooltip='Жмякни на меня!', icon=folium.Icon(color='blue')).add_to(valaam_map)

folium.Marker(location=[61.372534279452694, 30.9019985431249], popup="Вознессенская часовня", tooltip='Жмякни на меня!', icon=folium.Icon(color='blue')).add_to(valaam_map)

folium.Marker(location=[61.37355127198035, 30.89114922384849], popup="Воскресенский скит", tooltip='Жмякни на меня!', icon=folium.Icon(color='blue')).add_to(valaam_map)

folium.Marker(location=[61.389197487036135, 30.882658452240868], popup="Церковь Иоанна Предтечи", tooltip='Жмякни на меня!', icon=folium.Icon(color='blue')).add_to(valaam_map)

folium.Marker(location=[61.3897621859065, 30.943626909478958], popup="Валаамский Спасо-Преображенский монастырь", tooltip='Жмякни на меня!', icon=folium.Icon(color='blue')).add_to(valaam_map)

valaam_map.save("map1.html")
