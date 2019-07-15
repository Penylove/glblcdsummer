def is_even(x):
    if x % 2 is 0:
        return True
    else:
        return False

numbers = [1,56,234,87,4,76,24,69,90,135]

new_num = list(map(is_even,numbers))

print("is_even: ",new_num)

new_lamd = list(filter(lambda x : x % 2 is 0,numbers))
print("lambda : ",new_lamd)

odd_lamd = list(filter(lambda x : x % 2 is 1,numbers))

print("odd_lamd : ",odd_lamd)


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)

n_word = [len(word) for word in words]

print(n_word)

n2_word = [len(word) for word in words if word != "the"]

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


numbers2 = [list(filter((lambda x: x>0 ),numbers))]

print(numbers2)


numbers3 = [n for n in numbers if n%2 == 0 ]
print(numbers3)

numbers4 = [c for c in numbers if c > 0]

print(numbers4)

list1 = [d for d in range(1,50)]
print("main list: ",list1)
print("\n")
list2 = [v for v in list1 if v%2 == 0]
print("even:",list2)
print("\n")


list3 = [f for f in list1 if f%2 == 1]
print("odd: ",list3)
print("\n")


#print(list9)
list9 = []
for i in words:
    #list9.append(i.upper())
    #tup2 = list((i.upper(),len(i)))
    list9.append((i.upper(),len(i)))
    

tup1 = tuple((p for p  in list9))

print("tuple:",tup1)
#print("i".upper())
d = 1
'''
def factorial(t):
    for i in range(1,t):
        q = t * i
    return q
print(factorial(4) )   
   
'''

def factorial(n):
    if n ==1:
        return 1
    
    else:
        return n * factorial(n-1)

print(factorial(3))
#print(facto(2))