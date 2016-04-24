
#Change 

cost = float (input("What is the cost"))
tender = float (input ("What is the cash tender:"))
change = tender - cost

twenties = int(change /20)
tens = int((change-20*twenties)/10)
fives = int((change%10/5))
ones = int((change%5))
cents = change-int(change)
quarters = int(cents/0.25)
dimes = int((cents-quarters*0.25)/0.10)
nickels = int((cents-quarters*0.25-dimes*0.1)/0.05)
pennies = round((cents%0.05/0.01))

print("The change are:", change)
print("twenties:", twenties)
print("tens:", tens)
print("fives:", fives)
print("ones:", ones)
print("cents:", cents)
print("quarters:", quarters)
print("dimes:", dimes)
print("nickels:", nickels)
print("pennies:", pennies)
