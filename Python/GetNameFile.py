import os
import csv

src='C:/Users/Hang Le/Downloads/GameDog'
obj_list=os.listdir(src)
#print(obj_list)

#>> ['dir1', 'dir2', 'pass.txt', 'user.txt']

with open('C:/Users/Hang Le/Downloads/Test01.csv', mode='w') as f:
    writer = csv.writer(f)
    for i in obj_list:
        writer.writerow(i)
        
