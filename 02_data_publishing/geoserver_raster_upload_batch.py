"""We are going to connect to the Geoserver and upload some data"""
# info source: https://pypi.org/project/geoserver-rest/

import os
from geo.Geoserver import Geoserver #make sure it is updated

#Initialize the library
"""Production-geoserver"""
#geo = Geoserver('https://integratedmodelling.org/dev-geoserver', username='', password='')
"""Development-geoserver"""
geo = Geoserver('http://192.168.250.122:8600/geoserver', username='', password='')


# Create a workspace if necesary
geo.create_workspace(workspace='earth_data')

#path to our source data
"""WARNING, DO NOT PUT ANYTHING ELSE IN THE FOLDER EXCEPT TIF FILES"""
#path=r"C:/Users/ruben.crespo/Documents/03_tests/global_accesibility/access_50k/store"
path = r"C:/Users/ruben.crespo/Desktop/earthdata"
#print(os.listdir(path))

def geoserver_raster_batch(geo,path):
    for file in os.listdir(path):
        location = path +"/"+ file #we create the location
        name = file.replace('.tif','') #store the name without .tif
        print(location)
        print(name)
        # Upload raster data to the geoserver
        geo.create_coveragestore(lyr_name=name, path=location, workspace='earth_data')
    return print("It's over, congratulations")

geoserver_raster_batch(geo,path)


#geo.create_coveragestore(lyr_name="global-accessibility-2021", path="C:/Users/ruben.crespo/Documents/03_tests/global_accesibility/access_50k/store/global-accessibility-2021.tif", workspace='im-data-global-demography')