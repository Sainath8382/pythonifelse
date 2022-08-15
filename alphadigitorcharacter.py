var=input("Enter value")
if ((var>='A' and var<='Z') or (var>='a' and var<='z')):
    print(var,"is an alphabet")
elif(var>='0' and var<='9'):
    print(var,"is a digit")
else:
    print(var,"is a special character")