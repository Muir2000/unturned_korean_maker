import os

if os.path.isfile('./Item.meta/English.dat'):
    print('존재')
else:
    print('안존재')

print(os.getcwd())
