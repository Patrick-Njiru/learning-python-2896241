# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request 
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]: print(theJSON["metadata"]["title"])
    
    # output the number of events, plus the magnitude and each event name  
    count = theJSON["metadata"]["count"]
    print(count, "events recorded \n")

    # for each event, print the place where it occurred
    for i in theJSON["features"]: print(i["properties"]["place"])
    print("--------------------------------\n")

    # print the events that only have a magnitude greater than 4
    count2 = 0
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            count2 += 1
            print(i["properties"]["place"])
    print()
    print(count2, "events with a magnitude greater than 4.0")
    print("--------------------------------\n")


    # print only the events where at least 1 person reported feeling something
    print("Events that were felt:")
    for i in theJSON["features"]:
        felt_reports = i["properties"]["felt"]
        if felt_reports != None and felt_reports > 0: print(i["properties"]["place"], felt_reports, "times")

  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()) + "\n")
    if (webUrl.getcode() == 200):
        data =  webUrl.read()
        printResults(data)
    else:
        print("Received an error from the server, cannot print results", webUrl.getcode())

if __name__ == "__main__":
    main()
