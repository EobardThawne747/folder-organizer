import os
import shutil
import re

folder_name = r'C:\Users\erin.manka\Desktop\FUTURE\Test'

def prapashtese_file(pathi):   #funksion per te ekstraktuar prapashtesen e file pa .
    prapashtesa = re.compile(r'\.(\w+)$')
    kerko = prapashtesa.search(pathi)
    return kerko.group(1)


# krijon nje direktori te re tek direktoria parent qe do mbaje filet e organizuar
parent_directory = os.path.dirname(folder_name)
organized_directory = os.path.join(parent_directory, "Test-organized")
os.makedirs(organized_directory)


for files in os.walk(folder_name): # kthen nje tuple ne format (absolute path, liste subfolder, liste file)
    for file in files[2]:  # loop tek lista e fileve
        pathi = os.path.join(files[0],file) #absolute path
        prapashtesa = prapashtese_file(pathi)
        subfolder_name = os.path.join(organized_directory, prapashtesa + "Files") # emri i folderit formatin prapashtese+file
        if os.path.isdir(subfolder_name):  #organizojme filet sipas direktorive
            shutil.move(pathi, subfolder_name)
        else:
            os.makedirs(subfolder_name)
            shutil.move(pathi, subfolder_name)


# te fshihet direktoria qe mbante materialin e paorganizuar pasi te kalohet i gjithi
shutil.rmtree(folder_name)