import random
fid = open("labels.csv", "r")
li = fid.readlines()
fid.close()
print(li)

random.shuffle(li)
print(li)

fid = open("shuffled.csv", "w")
fid.writelines(li)
fid.close()