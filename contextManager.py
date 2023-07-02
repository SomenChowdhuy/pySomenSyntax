fp = open('myfile.txt','w')
li = ['apple\n','orange\n','hogplum\n']
fp.writelines(li)
fp.close()

fp = open('myfile.txt','r')
content = fp.read()
print(content)
fp.close()

fp = open('myfile.txt','a')
li = ['apple\n','orange\n','hogplum\n']
fp.writelines(li)
fp.close()

with open('myfile.txt','r') as fp:
    content = fp.readlines()
    print(content)