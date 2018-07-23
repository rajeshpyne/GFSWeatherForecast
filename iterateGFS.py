import datacartridge as dc
import subprocess
import sys

fileName = str(sys.argv[1])
yearmonday = str(sys.argv[2])

weatherStations=dc.getTable('Weather Historical Station Details')
#print(weatherStations.head())
cond1 = weatherStations['isActive_CY'] == True
cond2=weatherStations['Country']=="United States"

filterStations=weatherStations[cond1 & cond2]
#print(filterStations)
#argFilterStations=(filterStations[['StationIdentifier','Latitude','Longitude']])
argFilterStations=dc.customQuery("SELECT TOP 10000 StationIdentifier, Latitude, Longitude FROM WeatherHistoricalStationDetails WHERE isActive_CY=1 AND Country='United States'")

for row in argFilterStations.itertuples():
	sid=(row.StationIdentifier)
	lat=(row.Latitude)
	lon=(row.Longitude)
	#print(fileName,sid,lat,lon)
	#subprocess.call(['python3','/data_cartridge/noodleWorkspace/weatherForecast/GFSwritecsv.py',fileName,yearmonday,sid,lat,lon])#US1FLPN0055,27.8164,-82.6433
	subprocess.call('/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/GFSwritecsv.py '+fileName+' '+yearmonday+' '+sid+' '+lat+' '+lon,shell=True)
