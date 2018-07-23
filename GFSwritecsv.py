import netCDF4
import numpy as np
from netCDF4 import num2date, date2num, date2index
from datetime import datetime, timedelta
import sys
import csv
import subprocess

def getclosest_ij(lats,lons,latpt,lonpt):
    # find squared distance of every point on grid
    dist_sq = (lats-latpt)**2 + (lons-lonpt)**2
    # 1D index of minimum dist_sq element
    minindex_flattened = dist_sq.argmin()
    # Get 2D index for latvals and lonvals arrays from 1D index
    return np.unravel_index(minindex_flattened, lats.shape)

fileName = str(sys.argv[1])
observedDate = str(sys.argv[2])
sid=str(sys.argv[3])
lat=float(sys.argv[4])
lon=float(sys.argv[5])
print(fileName,observedDate,sid,lat,lon)

cycle='0000'
startTime=12
loop=24
#
'''ftp = ftplib.FTP('nomads.ncdc.noaa.gov')
#ftp.login('anonymous','anonymous@')
ftp.login()

data = []
defaultDir='/GFS/Grid4/'

ftp.cwd(defaultDir)

#=================================#
yearmon = []

ftp.retrlines("LIST", yearmon.append)
latest_yearmonDir = yearmon[len(yearmon)-6]
yearmonDirname = latest_yearmonDir.split(None, 8)
yearmonDir=yearmonDirname[-1]
print(yearmonDir)

ftp.cwd(yearmonDir)
#==================================#
dirList = []

ftp.retrlines("LIST", dirList.append)
latestDir=dirList[len(dirList)-1]
dirName = latestDir.split(None, 8)
datedir=dirName[-1]
print(datedir)

ftp.cwd(datedir)

#=================================#
# Downloading and extracting to netCDF Files(0000 -model cycle, 12pm forecast, with 24 hour interval)
prefixFilename = "gfs_4_"+datedir+"_"+cycle+"_"
ftp.quit()'''
outfile = open("/data_cartridge/noodleWorkspace/weatherForecast/GFSFinalDatasets/"+observedDate+"_"+fileName+".csv", "a+")
writer=csv.writer(outfile,delimiter=',')
gfs=netCDF4.Dataset('/data_cartridge/noodleWorkspace/weatherForecast/ncFiles/'+fileName+'.nc')
ind_list=["VIS_surface","GUST_surface","PRES_surface","TMP_surface","TSOIL_0M0D1mbelowground","WEASD_surface","SNOD_surface","PEVPR_surface","CPOFP_surface","APCP_surface","SUNSD_surface","PWAT_entireatmosphere_consideredasasinglelayer_","CWAT_entireatmosphere_consideredasasinglelayer_","RH_entireatmosphere_consideredasasinglelayer_","TOZNE_entireatmosphere_consideredasasinglelayer_","PRES_maxwind","UGRD_maxwind","VGRD_maxwind","TMP_maxwind","PRES_80maboveground","LAND_surface","ICEC_surface","LANDN_surface"]
for indic in ind_list:
	p = subprocess.Popen("grep '"+indic+"' /data_cartridge/noodleWorkspace/weatherForecast/ncFiles/"+fileName+".nc", stdout=subprocess.PIPE, shell=True)
	(output,err) = p.communicate()
	p_status= p.wait()
	if(p_status==1):
		continue
	else:

		data=[]
        	#print(indic)
		sfctmp = gfs.variables[indic]
                #for dname in sfctmp.dimensions:
                #       print(gfs.variables[dname])
		timedim = sfctmp.dimensions[0] # time dim name
		#print('name of time dimension = %s' % timedim)
		times = gfs.variables[timedim] # time coord var
		#print('units = %s, values = %s' % (times.units, times[:]))
		dates = num2date(times[:], times.units)
		#observedDate= fileName[6:14] #dates = num2date(times[:], times.units)
		#print([date.strftime('%Y-%m-%d %H:%M:%S') for date in dates[:10]]) # print only first ten...
		date = datetime.now() + timedelta(days=20)
                #print(date)
		ntime = date2index(date,times,select='nearest')
                #print('index = %s, date = %s' % (ntime, dates[ntime]))
		lats, lons = gfs.variables['latitude'][:], gfs.variables['longitude'][:]
                # lats, lons are 1-d. Make them 2-d using numpy.meshgrid
		lons, lats = np.meshgrid(lons,lats)
		j, i = getclosest_ij(lats,lons,lat,lon)
		fcst_temp = sfctmp[ntime,j,i]
		#print('Sid: %s, Indicator: %s, Forecast at %s UTC = %5.1f %s' % (sid,indic,dates[ntime],fcst_temp,sfctmp.units))
		data.append(sid)
		data.append(observedDate)
		data.append(lat)
		data.append(lon)
		data.append(indic)
		data.append(sfctmp.long_name.replace(',',';'))
		data.append(dates[ntime])
		data.append(fcst_temp)
		data.append(sfctmp.units.replace(',',';'))
		writer.writerow(data)

