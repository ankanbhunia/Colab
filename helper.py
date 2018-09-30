from __future__ import print_function
import time
import GPUtil as GPU 
import os
import pandas
import numpy as np
import threading
def Background_(function):
    
    t = threading.Thread(target=function)
    t.daemon = True
    t.start()
    
def show_():
    while True:
        GPUs = GPU.getGPUs()
        gpu = GPUs[0]
        time.sleep(2)
        print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal),end='\r')
        
        
Background_(show_)

    
def Show_running_process():
    print ('Running Programs : ')
    print(task('python'))
def Kill(PID):
    print(get_ipython().getoutput('kill '+str(PID)))
def Reset():    
    get_ipython().getoutput('kill -9 -1')
def Download_from_Drive(ID, Name):
    get_ipython().system_raw('pip install googledrivedownloader')
    from google_drive_downloader import GoogleDriveDownloader as gdd
    gdd.download_file_from_google_drive(file_id=ID,
                                        dest_path='/content/'+Name,
                                        unzip=False)
def task(pross):
    dd = [i.split(' ') for i in get_ipython().getoutput("ps -eF | grep "+pross+"| grep -v grep | awk '{print  $2,  $6, $10, $11}'")]
    return pandas.DataFrame(dd,np.arange(1,len(dd)+1),['PID','memory','time','process'])
def Extract(path):
    import os
    pp = path.split('/')

    pp1 = '/'.join(pp[:-1])

    if os.path.isdir(path):
      hh= os.listdir(path)
      for i in hh:
        print (i)
    elif os.path.isdir(pp1):
      kk = ([i for i in os.listdir(pp1) if pp[-1] in i])
      for i in kk:
        zz = i.split(pp[-1])
        print(zz[0] + '\x1b[1;37;40m' + pp[-1] + '\x1b[0m' + zz[1])
    path1  = path.split(' ')
    path1 = '\ '.join(path1)   
    if os.path.isfile(path):

      if path.endswith('zip'):
        print ('Extracting ' + path)
        get_ipython().system_raw('unzip '+ path1)

      if path.endswith('rar'):
        print ('Extracting ' + path)
        get_ipython().system_raw('unrar x  '+ path1)

      if path.endswith('tar.gz'):
        print ('Extracting ' + path)
        get_ipython().system_raw('tar -xvf '+ path1)
