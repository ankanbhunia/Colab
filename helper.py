from IPython.display import HTML


import ipywidgets as wg
from IPython.display import display
import os


def helper_():
    


    class printer():
        """
        Print things to stdout on one line dynamically
        """

        def __init__(self,st):
            print (time.strftime('%Y-%m-%d %H:%M %p', time.localtime())+ ' >> ' + st)

    datadict = {i:ind+1 for ind,i in enumerate(os.listdir('drive/datasets/'))}
    dddataset = wg.Dropdown(options=datadict, value=1,
                      description='Dataset',
                      button_style='')
    butt2 = wg.Button(description='Extract')
    inv_map = {v: k for k, v in datadict.items()}
    def data_click(event):
        dpath = 'drive/datasets/' + inv_map[dddataset.value]
        if os.path.isfile(dpath):
          if dpath.endswith('zip'):
            get_ipython().getoutput('unzip '+ dpath)
            printer ('Dataset successfully imported')

          if dpath.endswith('rar'):
            get_ipython().getoutput('unrar x  '+ dpath)
            printer ('Dataset successfully imported')

          if dpath.endswith('tar.gz'):
            get_ipython().getoutput('tar xvf  '+ dpath)
            printer ('Dataset successfully imported')
    butt2.on_click(data_click)   
    ss3 = wg.HBox([dddataset,butt2])
    display(wg.VBox([ss3]))
p = """<script>
        code_show=true; 
        function code_toggle() {
         if (code_show){
         $('div.input').hide();
         } else {
         $('div.input').show();
         }
         code_show = !code_show
        } 
        $( document ).ready(code_toggle);
        </script>
        """