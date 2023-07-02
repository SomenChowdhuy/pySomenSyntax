fp = open('myfile.txt','w')
#fp.write("This is a text file\n")
lines = ['apple\n','banana\n','coconut\n']
fp.writelines(lines) 
fp.close()

fp = open('myfile.txt','r')
content = fp.read()
print(content)
fp.close()

fp = open('myfile.txt','w')
lines = ['apple\n','banana\n','coconut\n']
fp.writelines(lines)
fp.close() 

fp = open('myfile.txt','a')  
lines = ['apple\n','banana\n','coconut\n']
fp.writelines(lines)
fp.close() 

fp = open('myfile.txt','a')
lines = ['apple\n','banana\n','coconut\n']
fp.writelines(lines)
fp.close()

