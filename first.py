
def priAst(q):
    ast = "****"
    for g in range(0,q):
        print(ast)
    print("--------------------------------------")
    print("--------------------------------------")

def incdec(c):
    asterisk = "*"
    for x in range(1,c): 
        v = asterisk * x
        print(v)
    while c > 0:
        c = c - 1
        d = asterisk * c
    
        print(d)
    print("--------------------------------------")
    print("--------------------------------------")

incdec(9)
priAst(9)

a = "a"

def find_char(a,w):
        
    for r in w:
        if(r == a):
            break
        
    print(r == a)
    
    
    
#find_char("2") 
incdec(10)