import os

global lisu
global save
lisu = []
save = []

def search(dirname):
    filename = os.listdir(dirname)
    for filename in filename:
        full_filename = os.path.join(dirname, filename)
        if full_filename.find('.') == True:
            pass
        else:
            lisu.append(full_filename[2:])

search('./')

endat = '/English.dat'

for wy in range(0,len(lisu)):
    try:
        data = open('./'+ lisu[wy] + endat,'r',encoding='UTF8')
        print('./'+ lisu[wy] + endat)
        all_data = data.read()
        nanunge = all_data.split('\n')
        save.append(nanunge[0][5:] + '\n')
        save.append(nanunge[1][12:].replace("\n","")+'\n')
        data.close()
    except:
        pass
data2 = open('all.txt','wt',encoding='UTF8')
data2.writelines(save)
data2.close()