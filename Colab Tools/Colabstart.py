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
  return url 
  
def localtunnel(domain,port=6007,mode= 'Notebook'):
	get_ipython().system_raw("ruby localtunnel.rb -s " + domain + " -p " + str(port) + " &")
	
	
	
	
def load(port=6007,show_result=False):
	cmd = [['apt-get install -y -qq software-properties-common python-software-properties module-init-tools',True],
	['add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null',True],
	['apt-get update -qq 2>&1 > /dev/null',True],
	['apt-get install unrar',True],
	['apt-get install ruby-full',True],
	['pip install --upgrade jupyter',True],
	['apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python',True],
	['pip install -q keras',True],
	['pip install jupyterlab',True],
	['jupyter notebook --generate-config',not os.path.isfile('~/.jupyter/jupyter_notebook_config.py')],
	["echo \"c.NotebookApp.token = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	["echo \"c.NotebookApp.notebook_dir = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	['npm install -g localtunnel',True],
	['dpkg -i "/tmp/Colab/Colab Tools/google-drive-ocamlfuse_0.7.0-0ubuntu1_amd64.deb"',True],
        ['apt-get install -f',True],
	['apt-get -y install -qq fuse', True],	
	['sleep 3', True]]
	
  
	for i in tqdm(cmd):
	  if i[1]:
	      if show_result ==False:
		        get_ipython().system_raw(i[0])
	      else:
		        print (i[0]); print(get_ipython().getoutput(i[0]))
			
	
    
	#if len(get_ipython().getoutput('jupyter notebook list'))==2:
	#  get_ipython().system_raw("jupyter notebook --port "+str(port)+" &")
	
def get_vscode(dir):
	Domain_Name_for_vscode = ''.join([chr(np.random.choice(np.arange(ord('a'),ord('z')))) for i in range(6)])
	localtunnel(Domain_Name_for_vscode, 8443)
	print ('Your VScode URL:'+ 'http://'+Domain_Name_for_vscode+ '.localtunnel.me')
	get_ipython().system_raw('./code-server1.1119-vsc1.33.1-linux-x64/code-server'+dir+'--allow-http --no-auth /')
	
	
	
	
def load_drive(drive_no):	 
	cmd = [['unzip gdfuse'+str(drive_no)+'.zip'+' -d /', not os.path.isdir("/root/.gdfuse")],
	['mkdir -p drive',not os.path.isdir("drive")],
	['google-drive-ocamlfuse drive', not os.path.isdir("drive")]]
	
	for i in cmd:
	  if i[1]: get_ipython().getoutput(i[0])
import fileinput
import sys



def changevalue(t):
  
  txt = ''
  for i in t.keys():
    txt = txt + i+'='+t[i]+'\n'
  
  with open('/root/.gdfuse/default/state','w') as f:
    f.write(txt)

load()

def get_urls():
	if not 'Domains_jupyter_list' in locals():
	  Domains_jupyter_list = []
	if not 'Domains_Tensorboard_list' in locals():
	  Domains_Tensorboard_list = []


	ans1 = True

	if not len(Domains_jupyter_list) == 0:
	  ans = input('You have already created Jupyter Notebook URL. Do you want to create another one? (Y/N): ')
	  if ans == 'Y':
	    ans1 = True
	  else:
	    ans1 = False

	if Domain_Name_for_jupyter == "":
	  Domain_Name_for_jupyter = ''.join([chr(np.random.choice(np.arange(ord('a'),ord('z')))) for i in range(6)])

	if ans1:
	  localtunnel(Domain_Name_for_jupyter,mode= 'Notebook')
	  Domains_jupyter_list.append(Domain_Name_for_jupyter)



	ans2 = True

	if not len(Domains_Tensorboard_list) == 0:
	  ans = input('You have already created Tensorboard URL. Do you want to create another one? (Y/N): ')
	  if ans == 'Y':
	    ans2 = True
	  else:
	    ans2 = False

	if Domain_Name_for_tensorboard  == "":
	  Domain_Name_for_tensorboard = ''.join([chr(np.random.choice(np.arange(ord('a'),ord('z')))) for i in range(6)])

	port_ten = np.random.choice(np.arange(1000,9000))

	if ans2:
	  get_ipython().system_raw('tensorboard --logdir=/content/logs --port='+str(port_ten)+'&')
	  localtunnel(Domain_Name_for_tensorboard,str(port_ten),mode= 'Tensorboard')
	  Domains_Tensorboard_list.append(Domain_Name_for_tensorboard)

	print ('')
	print ('')
	for i in range(len(Domains_jupyter_list)):
	  print ('Your Notebook URL#'+str(i+1)+': http://'+Domains_jupyter_list[i]+ '.localtunnel.me')
	for i in range(len(Domains_Tensorboard_list)):
	  print ('Your Tensorboard URL#'+str(i+1)+': http://'+Domains_Tensorboard_list[i]+ '.localtunnel.me')
