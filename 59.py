a=int(input("輸入金額:"))
b=a//100
a=a-b*100
c=a//50
a=a-c*50
d=a//10
a=a-d*10
e=a//5
a=a-e*5
f=a//1
print(b+c+d+e+f)
