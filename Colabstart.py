import os, time, pexpect, sys
from tqdm import tqdm

def ngrok(port=6007):
  import re
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
	['unzip gdfuse.zip',not os.path.isdir("/content/.gdfuse")],
	['mkdir -p drive',not os.path.isdir("drive")],
	['google-drive-ocamlfuse drive', not os.path.isdir("drive")],
	['npm install -g localtunnel',True],
	['wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip',not os.path.isfile("ngrok-stable-linux-amd64.zip")],
	['unzip ngrok-stable-linux-amd64.zip',not os.path.isfile("ngrok")],
  ['./ngrok authtoken 5vhWvAzJGtsJbnVp4V5di_6KNVTN8BpHMqKYyAaFFXQ',not os.path.isfile("ngrok")]]
  
	for i in tqdm(cmd):
	  if i[1]:
	      if show_result ==False:
		        get_ipython().getoutput(i[0])
	      else:
		        print (i[0]); print(get_ipython().getoutput(i[0]))

    
	if len(get_ipython().getoutput('jupyter notebook list'))==2:
	  get_ipython().system_raw("jupyter notebook --port "+str(port)+" &")
