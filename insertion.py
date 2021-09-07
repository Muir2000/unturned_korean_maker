import os
import os.path
global lisu
lisu = []
a = 0
b = 1

filename = os.listdir('./')
for entry in os.listdir('./'):
    if os.path.isfile(os.path.join('./', entry)):
        print('no')
    else:
        lisu.append(entry)



endat = '/English.dat'
data = open('save2.txt','rt',encoding='UTF8')
all_data = data.read()
nanunge = all_data.split('\n')
for wy in range(0,len(lisu)):
    print('./'+ lisu[wy] + endat)
    Name = nanunge[a]
    Description = nanunge[b]
    file = './'+ lisu[wy] + endat
    if os.path.isfile(file):
        print('확인')
        data2 = open('./'+ lisu[wy] + '/Korean.dat', 'wt', encoding='UTF8')
        save = 'Name ' + Name + '\n' + 'Description ' + Description
        data2.write(save)
        data2.close()
        a += 2
        b += 2
    else:
        print('없음')
data.close()