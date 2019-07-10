'''
def enterTup(m,ma):
    k = []
    for i in range(m,ma):
        if(i%2 == 0):
            k.append(i)
    print(k)
    
def getmin_max():
    m = int(input("enter minimum value: "))
    ma = int(input("enter maximum value: "))
    enterTup(m,ma)

#getmin_max()
    '''
def partition():
    c = int(input("enter any number  "))
    tup1=('none',c)
    tup2=(c,'none')
    if c%2 is 0:
        print(tup1)
        print("this is an even number")
    else:
        print(tup2)
        print("this is soooooo odd")
        
partition()
    