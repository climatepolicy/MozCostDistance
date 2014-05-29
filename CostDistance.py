# Name: FeatureToRaster_Ex_02.py
# Description: Converts features to a raster dataset.
# Requirements: None
# Name: CostDistance_Ex_02.py
# Description: Calculates for each cell the least accumulative cost distance
#    to the nearest source over a cost  surface. 
# Requirements: Spatial Analyst Extension
# Author: ESRI

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Overwrite pre-existing files
arcpy.env.overwriteOutput = True

# Set environment settings
env.workspace = "C:/Users/ahobbs/Documents/Mozambique/GIS"

# Set local variables
inFeature = "mozroads4.shp"
outRaster = "roadsgrd"
cellSize = 0.01
field = "speed"

# Execute FeatureToRaster
arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)

# Set local variables
inSourceData = "moz_ports.shp"
inCostRaster = "roadsgrd"
maxDistance = 20000000   
outBkLinkRaster = "outbklink"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute CostDistance
outCostDistance = CostDistance(inSourceData, inCostRaster, maxDistance, outBkLinkRaster)

# Save the output 
outCostDistance.save("outcostdist")