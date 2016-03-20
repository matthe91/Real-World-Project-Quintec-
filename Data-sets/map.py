from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color="green",  lake_color="green")
m.drawmapboundary(fill_color="blue")

lat,lon = 55.0, -2.0
x,y = m(lon,lat)
m.plot(x,y,'ro')

lat,lon = 53.0, -2.0
x,y = m(lon,lat)
m.plot(x,y,'ro')

plt.title("Marked Infected Areas")
plt.show()
