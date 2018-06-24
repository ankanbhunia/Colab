#import pip
import os, time, pexpect, sys
#pip.main(['install', 'tqdm'])
os.system('pip install tqdm')
from tqdm import tqdm
import pandas
import numpy as np
import time

def task(pross):
	dd = [i.split(' ') for i in get_ipython().getoutput("ps -eF | grep "+pross+"| grep -v grep | awk '{print  $2,  $6, $10, $11}'")]
	return pandas.DataFrame(dd,np.arange(1,len(dd)+1),['PID','memory','time','process'])
def ngrok(auth , port=6007):
  import re
  get_ipython().system_raw('./ngrok authtoken ' + auth)
  get_ipython().system_raw('./ngrok http '+ str(port)+ ' &')
  time.sleep(5)
  url = ' '.join(re.findall('http://.*?ngrok.io',' '.join(get_ipython().getoutput('curl -s http://localhost:4040/api/tunnels'))))
  print('Main '+url + '\n''Colab '+url+"/tree/drive/CoLab")
  
def localtunnel(domain,port=6007):
	get_ipython().system_raw("ruby localtunnel.rb -s " + domain + " -p " + str(port) + " &")
	print ('http://'+domain + '.localtunnel.me')
	
def load(port=6007,show_result=False):
	cmd = [['apt-get install -y -qq software-properties-common python-software-properties module-init-tools',True],
	['add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null',True],
	['apt-get update -qq 2>&1 > /dev/null',True],
	['apt-get -y install -qq google-drive-ocamlfuse fuse',True],
	['apt-get install unrar',True],
	['apt-get install ruby-full',True],
	['pip install --upgrade jupyter',True],
	['pip install jupyter-tensorboard',True],
	['pip install jupyter_contrib_nbextensions',True],
	['pip install jupyter_nbextensions_configurator',True],
	['apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python',True],
	['pip install -q keras',True],
	['pip install jupyterlab',True],
	['jupyter notebook --generate-config',not os.path.isfile('/content/.jupyter/jupyter_notebook_config.py')],
	["echo \"c.NotebookApp.token = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	["echo \"c.NotebookApp.notebook_dir = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	['npm install -g localtunnel',True],
	['wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip',not os.path.isfile("ngrok-stable-linux-amd64.zip")],
	['unzip ngrok-stable-linux-amd64.zip',not os.path.isfile("ngrok")],
	['pip install gpustat',True]]
  
	for i in tqdm(cmd):
	  if i[1]:
	      if show_result ==False:
		        get_ipython().getoutput(i[0])
	      else:
		        print (i[0]); print(get_ipython().getoutput(i[0]))

    
	if len(get_ipython().getoutput('jupyter notebook list'))==2:
	  get_ipython().system_raw("jupyter notebook --port "+str(port)+" &")
	
def load_drive(drive_no):	 
	cmd = [['unzip gdfuse'+str(drive_no)+'.zip',not os.path.isdir("/content/.gdfuse")],
	['mkdir -p drive',not os.path.isdir("drive")],
	['google-drive-ocamlfuse drive', not os.path.isdir("drive")]]
	
	for i in cmd:
	  if i[1]:
	      get_ipython().getoutput(i[0])
	     
