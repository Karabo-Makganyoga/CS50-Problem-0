bank_greeting = input("Greeting: ").strip().title()
#The title() method returns a string where the first character in every word is upper case

if bank_greeting.startswith("Hello"):
    print("$0")
elif bank_greeting.startswith("H"): #The startswith() method returns True if the string starts with the specified value, otherwise False
    print("$20")
else:
    print("$100")
