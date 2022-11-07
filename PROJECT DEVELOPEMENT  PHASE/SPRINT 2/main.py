import brain


myLocation = "Chennai,IN"
APIKEY = "bf4a8d480ee05c00952bf65b78ae826b"

localityInfo = {
    "schools" : {
        "schoolZone" : True,
        "activeTime" : ["7:00","17:30"] 
        },
    "hospitalsNearby" : False,
    "usualSpeedLimit" : 40 
}

while True :
    print(brain.processConditions(myLocation,APIKEY,localityInfo))
