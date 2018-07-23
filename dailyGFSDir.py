from ftplib import FTP
import datetime
import subprocess
import requests

def downloadGRB2(finalDir):
    #cycle = '0000'
    startTime = 36
    loop = 24
    #extension = '.grb2'
    #endTime = startTime * (loop-1)
    #print(endTime)
    subprocess.call('rm -rf /data_cartridge/noodleWorkspace/weatherForecast/ncFiles/*',shell=True)
    for x in range(startTime, 253, loop):
        if (x < 100):
            x = '0' + str(x)
            fileName = 'gfs.t00z.pgrb2.0p25.f'+ x
            url = finalDir+'/'+fileName
            print(url)
            #print(fileName+extension)
            #subprocess.call('rm -rf grb2Files/*',shell=True)
            #subprocess.call(['rm','-rf','ncFiles/*'])
            subprocess.call(['wget','-q',url,'-P','/data_cartridge/noodleWorkspace/weatherForecast/grb2Files/'])
            subprocess.call(['wgrib2', '/data_cartridge/noodleWorkspace/weatherForecast/grb2Files/' + fileName, '-netcdf', '/data_cartridge/noodleWorkspace/weatherForecast/ncFiles/' + fileName + '.nc','-match',':(VIS:surface|GUST:surface|PRES:surface|TMP:surface|TSOIL:0-0.1 m below ground|WEASD:surface|SNOD:surface|PEVPR:surface|CPOFP:surface|APCP:surface|SUNSD:surface|PWAT|CWAT|RH:entire atmosphere \(considered as a single layer\)|TOZNE|PRES:max wind|UGRD:max wind|VGRD:max wind|TMP:max wind|PRES:80 m above ground|LAND:surface|ICEC:surface|LANDN:surface):'])
            subprocess.call('rm -rf /data_cartridge/noodleWorkspace/weatherForecast/grb2Files/*',shell=True)
            #subprocess.call(['python3', 'iterateGFS.py', fileName])
        else:
            x = str(x)
            fileName = 'gfs.t00z.pgrb2.0p25.f'+ x
            url = finalDir + '/'+fileName
            print(url)
            #print(fileName+extension)
            #subprocess.call('rm -rf grb2Files/*',shell=True)
            #subprocess.call(['rm', '-rf', 'ncFiles/*'])
            subprocess.call(['wget', '-q', url, '-P', '/data_cartridge/noodleWorkspace/weatherForecast/grb2Files/'])
            subprocess.call(['wgrib2', '/data_cartridge/noodleWorkspace/weatherForecast/grb2Files/' + fileName, '-netcdf', '/data_cartridge/noodleWorkspace/weatherForecast/ncFiles/' + fileName + '.nc','-match',':(VIS:surface|GUST:surface|PRES:surface|TMP:surface|TSOIL:0-0.1 m below ground|WEASD:surface|SNOD:surface|PEVPR:surface|CPOFP:surface|APCP:surface|SUNSD:surface|PWAT|CWAT|RH:entire atmosphere \(considered as a single layer\)|TOZNE|PRES:max wind|UGRD:max wind|VGRD:max wind|TMP:max wind|PRES:80 m above ground|LAND:surface|ICEC:surface|LANDN:surface):'])
            subprocess.call('rm -rf /data_cartridge/noodleWorkspace/weatherForecast/grb2Files/*',shell=True)
            #subprocess.call(['python3', 'iterateGFS.py', fileName])

todaysdate=str(datetime.datetime.today().date()-datetime.timedelta(days=0))

yearmonday=(todaysdate.replace('-',''))
#yearmon=(yearmonday[:-2])
#print(yearmonday)
#print(yearmon)
cycle='00'
httpURL='ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/gfs/prod'

folderName = httpURL+'/gfs.'+yearmonday+cycle
#month = requests.get(folderName)

#dateFolder = folderName+'/'+yearmonday
#day = requests.get(dateFolder)

print(folderName)
downloadGRB2(folderName)
subprocess.call('/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/dailyMultiprocess.py '+yearmonday,shell=True)
subprocess.call('hdfs dfs -copyFromLocal -f /data_cartridge/noodleWorkspace/weatherForecast/GFSFinalDatasets/* /datacartridge/weatherForecast/GFS/Raw/',shell=True)
subprocess.call('rm -rf /data_cartridge/noodleWorkspace/weatherForecast/GFSFinalDatasets/*',shell=True)
subprocess.call(['mail','-s','GFS Forecast DataLoad_'+yearmonday,'rajesh.pyne@noodle.ai'])
'''
if(month):
	print('YES Month Exist')
	if(day):
		print('Day Exist')
		wgetURL=dateFolder
		print(wgetURL)
		#downloadGRB2(wgetURL,yearmonday)
		#subprocess.call(['python3','/data_cartridge/noodleWorkspace/weatherForecast/multiprocess.py',yearmonday])
		#subprocess.call('hdfs dfs -copyFromLocal -f /data_cartridge/noodleWorkspace/weatherForecast/GFSFinalDatasets/* /datacartridge/weatherForecast/GFS/Raw/',shell=True)
		#subprocess.call('rm -rf /data_cartridge/noodleWorkspace/weatherForecast/GFSFinalDatasets/*',shell=True)
	else:
		print('Day do not exist')
else:
	print('NO Month Do not exist')
'''
