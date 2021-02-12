a = (1,2,3,0,7,0,6,0)


count = 0
for i in a:
    if(i==0):
        count = count + 1
    
print(  count)
print(a.count(0))
