# Information
print("Enter 3 number suppose A,B,C")



# Declaring Variables A,B,C.

a=int(input("Display A value:"))

b=int(input("Display B value:"))

c=int(input("Display C value:"))



# Conditional Statements.

# Format Methond Used!

if a>b and a>c :
    
    print("Maximum number is {:d}".format(a))

    
elif b>a and b>c :
    
    print("Maximum number is {:d}".format(b))
    
elif c>a and  c>b:
    
    print("Maximum number is {:d}".format(c))
    
if a<b and a<c:
    
    print("Minimum number is {:d}".format(a))
    
elif b<a and b<c:
    
    print("Minimun number is {:d}".format(b))
    
elif c<a and c<b:
    
    print("Minimum number is {:d}".format(c))
    
elif a==b or b==c or c==a:
    
    print("Two Number are equal {:d},{:d}".format(a,b,c))
        
    
