# Operasi pembanding dalam Python
# Lebih besar / lebih kecil, sama dengan, tidak sama dengan

a = 5
b = 10

# Lebih besar > lebih kecil < 
print("Lebih besar dan lebih kecil dari '> / <'")
c = a > b
print(a,">",b,"=",c)
c = b > a
print(b,">",a,"=",c)
c = a > 7
print(a,"> 7 =",c)
c = b > 7
print(b,"> 7 =",c)

# sama dengan ==
print("Sama dengan '=='")
c = a == b
print(a,"==",b,"=",c)
c = a == 5
print(a,"== 5 =",c)
c = a == 4
print(a,"== 4 =",c)

# tidak sama dengan !=
print("tidak sama dengan '!='")
c = a != b
print(a,"!=",b,"=",c)
c = a != 5
print(a,"!= 5 =",c)
c = a != 4
print(a,"!= 4 =",c)
