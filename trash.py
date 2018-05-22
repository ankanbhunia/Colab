import os, time
while 1:
  if len(os.listdir('drive/.Trash/'))!=0:
    for i in os.listdir('drive/.Trash/'):
      os.remove('drive/.Trash/'+i)
      time.sleep(60)
