import os

#Creazione cartelle input e output
workingpath = os.getcwd()
newpathin = workingpath + '\input'
if not os.path.exists(newpathin):
    os.makedirs(newpathin)
newpathout = workingpath + '\output'
if not os.path.exists(newpathout):
    os.makedirs(newpathout)

#Carattere da inserire
charin = input('Input a character and press Enter. If no character is entered the space will not be substitued.\n')
	
#Rinominare files in cartelle
filenames = os.listdir(newpathin)
for filename in filenames:
    os.rename(os.path.join(newpathin, filename), os.path.join(newpathout, filename.replace(' ', charin)))
