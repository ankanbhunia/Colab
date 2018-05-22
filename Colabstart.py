import os, time, pexpect, sys

def ngrok(port=6007):
  import re
  url = re.findall('http://.*?ngrok.io',get_ipython().getoutput('curl -s http://localhost:4040/api/tunnels')[0])[0]
  print('Main '+url + '\n''Colab '+url+"/tree/drive/CoLab")

def localtunnel(domain,port=6007):
	get_ipython().system_raw("ruby localtunnel.rb -s " + domain + " -p " + str(port) + " &")
	print ('http://'+domain + '.localtunnel.me')
	
def load(port=6007):
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
	['jupyter notebook --generate-config',True],
	["echo \"c.NotebookApp.token = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	["echo \"c.NotebookApp.notebook_dir = u''\" >> ~/.jupyter/jupyter_notebook_config.py",True],
	['./ngrok authtoken 5vhWvAzJGtsJbnVp4V5di_6KNVTN8BpHMqKYyAaFFXQ',True],
	['unzip gdfuse.zip',not os.path.isdir("/content/.gdfuse")],
	['mkdir -p drive',not os.path.isdir("drive")],
	['google-drive-ocamlfuse drive', not os.path.isdir("drive")],
	['npm install -g localtunnel'],
	['wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'],
	['unzip ngrok-stable-linux-amd64.zip'],not os.path.isdir("ngrok")]
  
  for i in cmd:
    if i[1]:
      sys.stdout.write(' '.join(get_ipython().getoutput(i[0]))) ; sys.stdout.flush()
    
	if len(get_ipython().getoutput('jupyter notebook list'))==2:
	  get_ipython().system_raw("jupyter notebook --port "+str(port)+" &")
