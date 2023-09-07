import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap

m=Basemap(projection='merc',llcrnrlat=-80 , urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180 , resolution='c')  ###map
m.drawcoastlines()
m.drawstates()
path='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
data= pd.read_csv(path)
lon=[]
for i in data['longitude']:
    lon.append(i)
lat=[]
for i in  data['latitude']:
    lat.append(i)
x,y=m(lon,lat)
sizes=data['mag']**2
m.scatter(x,y,marker='o',c=data['mag'],s=sizes,label=data['mag'])
cursor= mplcursors.cursor(highlight=True)
def change(a):
    a.annotation.set_text((data['place'][a.target.index],data['mag'][a.target.index],data['time'][a.target.index]))
    a.annotation.arrow_patch.set(arrowstyle='simple',fc="white", alpha=0.5)
    a.annotation.get_bbox_patch().set(fc="white",alpha=1)
cursor.connect("add",change)
plt.show()


