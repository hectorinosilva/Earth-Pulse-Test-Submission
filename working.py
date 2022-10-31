# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:20:34 2022

@author: Hector Silva
"""
from fastapi import FastAPI
import rasterio
import rasterio.features
import rasterio.warp
from rasterio.plot import show
from matplotlib import pyplot
from PIL import Image
import numpy as np

app = FastAPI()

@app.get('/attributes')
def attributes():    
    #Opens the dataset    
    dataset =  rasterio.open("S2L2A_2022-06-09.tiff")    
    return ("Width: " + str(dataset.width), "Height: " + str(dataset.height), "Number of bands: " + str(dataset.count), "Georeferrenced Bounding Box: " +str(dataset.bounds)
            ,"Coordinate Reference System: " + str(dataset.crs))

@app.get('/thumbnail')
def thumbnail():
    dataset = rasterio.open("S2L2A_2022-06-09.tiff")
    img = pyplot.imshow(dataset.read(1), cmap='pink')
    pyplot.savefig("output.png")
    im = Image.open(r"output.png") 
    # This method will show image in any image viewer 
    im.show()
    return {"Opening Image"}
    
@app.get('/ndvi')
def ndvi():
    dataset = rasterio.open("S2L2A_2022-06-09.tiff")    
    red = dataset.read(4)
    nir = dataset.read(5)
    #I couldn't find which of the bands corresponded to the red and near infrared specifically so I assumed these ones based on my searches
    ndvi = (nir.astype(float)-red.astype(float))/(nir+red)
    img = pyplot.imshow(ndvi)
    pyplot.savefig("ndvi_output.png")
    im = Image.open(r"ndvi_output.png")       
    im.show()
    return {"Opening Image"}

    


    