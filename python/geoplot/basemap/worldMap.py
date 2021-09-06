from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='mill', lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua') 
map.fillcontinents(color='coral', lake_color='aqua') 
map.drawcoastlines()
map.drawcountries()

x, y = map(0, 0)

map.plot(x, y, marker='D',color='m')

plt.tight_layout()
plt.show()