#Change
import decimal


print ("")
print ("")
print ("")

flag = True 
while(flag):
    cost = float (input("What is the cost: "))
    tender = float (input ("What is the tender: "))
    flag = False 
    
    if(cost > tender):
        flag = True

        print ("")
        print("The cost can not be greater")
        print ("Try one more time, Please")
        print ("")

    
tax= round (cost*.05)
change = round (tender-cost-tax,2)




twenties = int(change /20)
tens = int((change-20*twenties)/10)
fives = int((change%10/5))
ones = int((change%5))
cents = change-int(change)
quarters = int(cents/0.25)
dimes = int((cents-quarters*0.25)/0.10)
nickels = int((cents-quarters*0.25-dimes*0.1)/0.05)
pennies = round((cents%0.05/0.01))

print ("")
print("Tax:", tax)
print("The change including tax deduction:", change)
print ("")
print("Twentie dollar bill:", twenties)
print("Ten dollar bill:", tens)
print("Five dollar bill:", fives)
print("One dollar bill:", ones)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
