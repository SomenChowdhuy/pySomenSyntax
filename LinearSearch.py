#Linear Search
li = [2,1,4,3,6,5,100]
key = 5
flag = False
for i in li:
   if key == i:
        print('found')
        flag = True
        break
if flag is True:
    print('not found')
#easiest way
li = [2,4,5,6,1]
key = 10 
if key in li:
    print('found')
else:
    print('not found') 