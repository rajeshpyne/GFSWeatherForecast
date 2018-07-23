from multiprocessing import Pool
import time
import subprocess
import sys

yearmonday=str(sys.argv[1])

work = (["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f036 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f060 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f084 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f108 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f132 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f156 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f180 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f204 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f228 "+yearmonday],
	["/usr/local/bin/python3 /data_cartridge/noodleWorkspace/weatherForecast/iterateGFS.py gfs.t00z.pgrb2.0p25.f252 "+yearmonday]
)

def work_log(work_data):
	subprocess.call(work_data[0],shell=True)
	#subprocess.call([work_data[0],work_data[1],work_data[2],work_data[3]])
	#print(" Process %s is working for %s" % (work_data[0],work_data[1]))
	#time.sleep(int(work_data[1]))
	#print(" Process %s is finished" %work_data[0])
    
def pool_handler():
    p = Pool(100)
    p.map(work_log,work)
    
if __name__=='__main__':
    pool_handler()
