# and, or, not

a = 100
b = 25
c = 30
print(a>b and a>c) #True
print(a<b and a>c) #False
print(a>b and a<c) #False
print(a<b and a<c) #False
print("__________________")
a = 100
b = 25
c = 30
print(a>b or a>c)
print(a>b or a<c)
print(a<b or a>c)
print(a<b or a<c)
print("__________________")

a = 100
b = 25
c = 30
print(not(a>b))
print(not(a<b))
print(not(a<b or a>c))
print(not(not(a<b) or not(a>c)))
print(not(not(a>b and not(a>c))))