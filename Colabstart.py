import os, time, pexpect, sys

def ngrok(port=6007):
  import re
  url = re.findall('http://.*?ngrok.io',get_ipython().getoutput('curl -s http://localhost:4040/api/tunnels')[0])[0]
  print('Main '+url + '\n''Colab '+url+"/tree/drive/CoLab")

def localtunnel(domain,port=6007):
	get_ipython().system_raw("ruby localtunnel.rb -s " + domain + " -p " + str(port) + " &")
	print ('http://'+domain + '.localtunnel.me')
	
def load(port=6007):
	cmd = ['apt-get install -y -qq software-properties-common python-software-properties module-init-tools',
	'add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null',
	'apt-get update -qq 2>&1 > /dev/null',
	'apt-get -y install -qq google-drive-ocamlfuse fuse',
	'apt-get install unrar',
	'apt-get install ruby-full',
	'pip install --upgrade jupyter',
	'pip install jupyter-tensorboard',
	'pip install jupyter_contrib_nbextensions',
	'pip install jupyter_nbextensions_configurator',
	'apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python',
	'pip install -q keras',
	'pip install jupyterlab',
	'jupyter notebook --generate-config',
	"echo \"c.NotebookApp.token = u''\" >> ~/.jupyter/jupyter_notebook_config.py",
	"echo \"c.NotebookApp.notebook_dir = u''\" >> ~/.jupyter/jupyter_notebook_config.py",
	'./ngrok authtoken 5vhWvAzJGtsJbnVp4V5di_6KNVTN8BpHMqKYyAaFFXQ',
	'unzip Colab/.gdfuse.zip',
	'mkdir -p drive',
	'google-drive-ocamlfuse drive',
	'npm install -g localtunnel',
	'wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip',
	'unzip ngrok-stable-linux-amd64.zip']

	for i in cmd:
	  get_ipython().getoutput(i)
	if len(get_ipython().getoutput('jupyter notebook list'))==2:
	  get_ipython().system_raw("jupyter notebook --port "+str(port)+" &")
