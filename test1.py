#! /usr/bin/python3

print ("hello \tworld\n")
print ("test")
print ( 2 ** 100)
a = 'C\'est le test python'
print (a)
print(a[0:3])
print(a[:3])
print(a[3:])
b = "ok!"
print(b * 8)

#=============== affichage
val = 9.23
#print (val)
print ("val = {:.3f}".format(val))


# ============== immutable of string
name = "Noel"
#name[0]= 'Z'
name = 'Z' + name[1:]
print (name)

#------------------------------------
for x in a:
    print(x)




