number1=int(input("Pick a large number\n"))
number2=int(input("Pick another large number\n"))
print("You owe $"+str(number1+number2)+" to the IRS\n")
first_name=input("What's your first name?\n")
last_name=input("What's your last name?\n")
print("Name: "+last_name+",",first_name+"\n")
noun=input("Pick a noun\n")
verb=input("Pick a verb\n")
adjective=input("Pick an adjective\n")
adverb=input("Pick an adverb\n")
print("The very "+adjective,noun+" was very very \n"+adjective+" and had to "+adverb,verb+" for fun \n")
km=float(input("Kilometers:\n"))
miles=str(km*0.621371)
miles2=miles
miles=miles[:4]
print(str(km)+" Kilometers ≈ "+str(miles)+" ("+miles2+") ""Miles\n")
number3=int(input("Pick a big number\n"))
number4=int(input("Pick another smaller number\n"))
print(str(number3)+" has "+str(number3%number4)+" left when divided by "+str(number4))