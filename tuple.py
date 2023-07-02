#tuple allows duplicate items and it is unchangeable
tpl = (1,2,3,4)
print(tpl)
print(type(tpl))
print(tpl[0],tpl[2],tpl[-1])

tpl = (2,4,6,10)
for i in tpl:
    print(i) 
tpl = (1,2,3)
print(tpl,type(tpl))

"""
li = [1,2,3,4]
tpl = (1,2,3,4)
li[2] = 5   # list is mutable
print(li)
tpl[2] = 5 # tuple is immutable or unchangeable
print(tpl)

"""
print(dir(tuple))
tpl = (1,2,3,4,5,3)
print(tpl.count(3))

tpl = (4,6,7,8,7)
print(tpl.count(7))

#unpack
tpl = (1,2,3,4)
p,q,r,s = tpl
print(tpl)

tpl = (10,20,30,40,50)
p,q,r,s = tpl
print(p,q,r,s) 

tpl = (2,4,6,8)
p,q,r,s,t = tpl
print(p,q,r,s)

