#This script was designed to extract trunk highways from the MNDOT county-based line shape files.
#It assumes that the shapefiles have been stored in one directory (workspace). 
#The code was taken in part from an example in the "Writing Geoprocessing Scripts with ArcGIS", and in part from #exported code from model builder, with modifications to join the code together. 


#Import Standard Library Modules
import sys, os, string, arcgisscripting

#Create the Geoprocessor Object

GP = arcgisscripting.create()

#Set the Input Workspace, or folder where the shapefiles are kept.
GP.Workspace = "C:\twincitiesinput"

#Set the output Workspace, or folder where the output shapefiles will be kept. 
outWorkspace = "C:\twincitiesoutput"


try:
    #Because we have previously set the workspace, we can use the next line of code to place the
    #shape files in the input folder into an enumeration, or list where there is an unknown or open-ended number of     #items, stored as the local variable "counties". 
    fcs = GP.ListFeatureClasses()
    #The following two lines reset the enumeration to ensure correct functionality, and then bring up the first         #item.
    fcs.Reset()
    fc = fcs.Next()
    #The while loop goes through each input feature class, uses the select tool to extract the lines representing       #trunk highways, and then stores them in an output feature class. 
    while fc:
        #Validate the new featureclass name for the ouput workspace.
        outFeatureClass = (outWorkspace + "\trnkhwys" + fc)
        gp.Select_analysis(fc, outFeatureClass, "\"CODE\" = '01' OR \"CODE\" = '02' OR \"CODE\" = '03'")
        fc = fcs.Next()

except:
    GP.AddMessage(GP.GetMessages(2))
    print GP.GetMessages(2)

    