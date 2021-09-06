from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#boundary resolution must be one of c, l, i, h or f
#longitudes are theoretical x-axis while latitudes which run top-bottom are the y-axis but normally reported as (y, x)

cod = [-90, 90, -180, 180] #whole world
#cod = [-50, 45, -30, 60] #Africa
#cod = [20,50,-130,-60] #USA

m = Basemap(projection='mill', llcrnrlat=cod[0], urcrnrlat=cod[1], llcrnrlon=cod[2], urcrnrlon=cod[3], resolution='l') 

m.drawcoastlines()
m.drawcountries(color='black', linewidth=2.0)
m.drawstates()
#m.drawrivers()
m.fillcontinents(color='grey', lake_color='#FFFFFF')
#m.bluemarble() #this gives a satelite like view
m.drawmapboundary(fill_color='lightblue', linewidth=1.0)

lat, lon = 29.76, -95.36
x, y = m(lon, lat)
m.plot(x, y, 'mo',  markersize=15, alpha=0.25)

lat, lon = 40.12, -104.24
x, y = m(lon, lat)
m.plot(x, y, 'go', markersize=15, alpha=0.5) #alpha helps if the plots lie above another giving better clarity

x, y = m(0, 0)
m.plot(x, y, marker='o',color='m')


if cod[0] == -90:
	plt.title('World Map')
elif cod[0] == -50:
	plt.title('Africa')
else:
	plt.title('USA')

plt.tight_layout()
plt.show()