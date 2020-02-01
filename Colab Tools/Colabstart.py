#import pip
import os, time, pexpect, sys
#pip.main(['install', 'tqdm'])
os.system('pip install tqdm')
from tqdm import tqdm
import pandas
import numpy as np
import time
import pickle
import sys
import os
import PySimpleGUI as sg

folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

treedata = sg.TreeData()
def add_files_in_folder(parent, dirname, savepath,c):
    c = c + 1 
    files = os.listdir(dirname)
    for f in files:
        fullname = os.path.join(dirname, f)
        if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
            treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
            if c<4: 
              
              add_files_in_folder(fullname, fullname,savepath,c )
        else:
            treedata.Insert(parent, fullname, f, values=[
                            "{0:.2f}".format(os.stat(fullname).st_size/(1024*1024))], icon=file_icon)


    with open(savepath, 'wb') as treefile:

      pickle.dump(treedata, treefile)
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
	cmd = [#['apt-get install -y -qq software-properties-common python-software-properties module-init-tools',True],
	#['add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null',True],
	#['apt-get update -qq 2>&1 > /dev/null',True],
	#['apt-get install unrar',True],
	#['apt-get install ruby-full',True],
	#['pip install --upgrade jupyter',True],
	#['apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python',True],
	#['pip install -q keras',True],
	['pip install jupyterlab',True],
	#['jupyter notebook --generate-config',not os.path.isfile('~/.jupyter/jupyter_notebook_config.py')],
	#["echo \"c.NotebookApp.token = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	#["echo \"c.NotebookApp.notebook_dir = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	#['npm install -g localtunnel',True],
	['dpkg -i "/tmp/Colab/Colab Tools/google-drive-ocamlfuse_0.7.0-0ubuntu1_amd64.deb"',True],
        ['apt-get install -f',True],
	['apt-get -y install -qq fuse', True],
	['sudo apt-get -y install firefox', True],
	['pip3 install -r "/tmp/Colab/Colab Tools/requirements.txt"', True],
	['pip2 install -r "/tmp/Colab/Colab Tools/requirements.txt"', True],
	]
	
  
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
	
	
	
	
def load_drive():	 
	cmd = [['unzip "/tmp/Colab/Colab Tools/gdfuse.zip" -d /', not os.path.isdir("/root/.gdfuse")],
	['mkdir -p Drive',not os.path.isdir("Drive")],
	['google-drive-ocamlfuse Drive', not os.path.isdir("Drive")]]
	print ('Mounted at /Drive')
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
