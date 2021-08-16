from shutil import copyfile
from pathlib import Path

data_dir='../data/'
data_dir=Path(data_dir)


#create renamed training set
train_dir=data_dir/"train"
Path(data_dir/"train-renamed").mkdir(parents=True, exist_ok=True)
train_renamed_dir=Path(data_dir/"train-renamed")
for sub in Path(train_dir).iterdir():
    if sub.is_dir():
        Path(train_renamed_dir/sub.stem).mkdir(parents=True, exist_ok=True)
        for i,img in enumerate(sub.glob('*.png')):
            #print(i,dir(img))
            new_path=str(Path(train_renamed_dir/sub.stem))+"/"+str(i)+"-"+img.name
            #print(new_path)
            copyfile(img,new_path)



#create renamed validation set
val_dir=data_dir/"val"
Path(data_dir/"val-renamed").mkdir(parents=True, exist_ok=True)
val_renamed_dir=Path(data_dir/"val-renamed")
for sub in Path(val_dir).iterdir():
    if sub.is_dir():
        Path(val_renamed_dir/sub.stem).mkdir(parents=True, exist_ok=True)
        for i,img in enumerate(sub.glob('*.png')):
            #print(i,dir(img))
            new_path=str(Path(val_renamed_dir/sub.stem))+"/"+str(i)+"-"+img.name
            #print(new_path)
            copyfile(img,new_path)






