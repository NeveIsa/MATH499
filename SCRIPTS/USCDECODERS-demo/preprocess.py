import config
import os,sys,time

from zipfile import ZipFile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


tranch = 1
labels_path = f'{config.RAW}/tranch'+str(tranch)+'_labels.csv'
pictures_path = f'{config.RAW}/persons-posture-tranch'+str(tranch)+'.zip'

labels = pd.read_csv(labels_path)
zip_file = ZipFile(pictures_path)

file_list = [obj.filename for obj in zip_file.infolist()]
file_list_simple = [name.split('/')[-1] for name in file_list]

names = pd.DataFrame({'file_path': file_list, 'file_name': file_list_simple})
names.head()

df = pd.merge(names, labels, on = 'file_name')
print(len(names), len(labels), len(df))
df.head()

# generate labels from class names
class_names = df.staff_patient_other.unique().tolist()
print(class_names)
class_df = pd.DataFrame({'staff_patient_other':class_names,'label':list(range(len(class_names)))})
#print(class_df)

df = df.join(class_df.set_index('staff_patient_other'), on='staff_patient_other')


print(df.head())


#convert to grascale and resize
#https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_rgb_to_gray.html
#https://scikit-image.org/docs/dev/api/skimage.transform.html#skimage.transform.resize

from skimage import data
from skimage.color import rgb2gray
from skimage import transform

IMG_SIZE = (256,256)

def img_cleanup(img,shape=IMG_SIZE):
    img = rgb2gray(img)
    img = transform.resize(img,shape)
    return img

#img loader
def img_load(img_path):
    img = plt.imread(zip_file.open(img_path))
    cleanimg = img_cleanup(img)
    return cleanimg

#from sklearn.model_selection import KFold
#kf = KFold(n_splits=5) # train-80% , test-20%
#kf.get_n_splits(df.index)
#train_index,test_index = list(kf.split(df.index))[0]



def loadimg(idx):
    row = df.iloc[idx]
    if row['staff_patient_other'] in ['Patient', 'Staff']: pass
    else: return None,None,None
    img=img_load(row.file_path)
    return img, row["staff_patient_other"],row.file_name



def storeimg(img,_class,file_name):
    #plt.imshow(img,cmap='gray')
    plt.imsave(f'{config.PROCESSED}/{_class}/{file_name}',img,cmap='gray')
    #test_or_train = 'train' if idx in train_index else 'test'
    #plt.savefig(f'{config.PROCESSED}/{test_or_train}/{row["staff_patient_other"]}/{row["file_name"]}')



print('Will delete data in {config.PROCESSED}? y/N')
ip = input()

if ip=='Y':
    os.system(f'rm -rf {config.PROCESSED}/*')
    time.sleep(2)
else:
    exit(0)

os.system(f'mkdir -p {config.PROCESSED}/Patient')
os.system(f'mkdir -p {config.PROCESSED}/Staff')



total=len(df)
for idx,row in df.iterrows():
    print('\r               \r',end='')
    print(f'{idx}/{total}',end='')
    sys.stdout.flush()    
    img,_class,filename = loadimg(idx)
    if filename:
        storeimg(img,_class,filename)

exit(0)





#img loader
def img_load(img_path):
    img = plt.imread(zip_file.open(img_path))
    return img


im_num = np.random.randint(0,len(df))
print(df.iloc[im_num, 2:])
im = img_load(df.iloc[im_num].file_path)
plt.imshow(im)




plt.imshow(img_cleanup(im),cmap='gray')


