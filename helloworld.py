import ee
ee.Initialize()

print('Hello World')

collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')
print(collection.size().getInfo())
