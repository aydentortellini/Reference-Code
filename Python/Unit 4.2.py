condition = "yes"

while(condition.lower() == "yes"):
    print("Untill you stop say yes this will loop")
    condition = input("do you wish to continue?: ")

print("end of code")

"""
== equal to
!= not equal to
> greater than
< less than
>= Greater than or equal to
<= less than or equal to

and - both conditions must be met(true)
or - either condition must be met(true)
"""

total = 0
while total <100:
    num = int(input("enter a number: "))
    total = total + num
print("The total is", total)
    
        
'''
break - end the loop and  continue with the code
continue - revert to the top of the loop and try again
'''

num1 = 2
while (num1 >= 1):
    if num1 == 1:
        break
    else:
        int(input("what is the number?"))
    print("end of code")
