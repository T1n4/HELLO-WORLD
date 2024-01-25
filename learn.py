def add(*args):
    return sum(args) 

print (add(2,4,5,5,6,6,66,)    )

import os ,datetime
from os import path
from datetime import time, date, timedelta

print(os.name)

file = open("new.txt", 'w+')

for i in range (1, 10):

    file.write('i am going to school\n')
    
file.close()

file = open("new.txt" , 'r' )
if file.mode == 'r':
    content =file.read()
print(content)    

print('path:',path.realpath('new.text'))
print('path a:',path.split(path.realpath('new.text')))


