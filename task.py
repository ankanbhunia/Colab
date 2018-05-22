import pandas
import numpy as np
dd = [i.split(' ') for i in get_ipython().getoutput("ps -ef | grep python| grep -v grep | awk '{print $2, $7, $8}'")]
pandas.DataFrame(dd,np.arange(1,len(dd)+1),['PID','time','process'])