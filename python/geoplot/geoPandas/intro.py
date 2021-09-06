#this intro script is representation of real world use for geoPandas
#the errors should be rectified to use this script.
import geoPandas as gpd
import matplotlib.pyplot as plt

#importig and plotting the cities shape file
cities = gpd.read_file("path.shp")
cities.plot(cmap='jet', column='citiesName', figsize=(10, 10))

#importing another shape file
area = gpd.read_file("paht.shp")
area.plot(cmap='jet')

#displaying both shapefile together
fig, ax = plt.subplot(1)
cities.plot(ax=ax)
area.plot(ax=ax, facecolor='yellow')

#intersecting
citiesArea = gpd.overlay(cities, area, how='intersection')
citiesArea.plot(figsize=(10,10))

#information about the cordinate we are using in our geoframe
cities.crs

#to get info about the areas which we can add as a column
cities.area

#assigning a new column - area
 citiesArea['Area(km2)'] = citiesArea.area/1000000 #to convert
 
#saving the geoFrame to .shp shape file
 citiesArea.to_file('path_to_save_the_file')
