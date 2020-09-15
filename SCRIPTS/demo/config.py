
RAW='demo'
PROCESSED='demo'
MODEL='demo-model.py'
REPORT='demo'




import os
BASE='../../'

RAW = os.path.join(BASE,'RAW',RAW)
PROCESSED = os.path.join(BASE,'PROCESSED',PROCESSED)
MODEL = os.path.join(BASE,'MODELS',MODEL)
REPORT = os.path.join(BASE,'REPORTS',REPORT)

if __name__=='__main__':
  for x in [RAW,PROCESSED,MODEL,REPORT]:
    os.system(f'mkdir -p {x}')
