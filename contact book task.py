contact = {"mohamed": "010123456789", "anas": "011123456789", "omar": "015123456789"}
print(contact.keys())
searsh = input("searsh for number by name: ")
if searsh == "mohamed":
    print(contact["mohamed"])
elif searsh == "anas":
    print(contact["anas"])
else:
    print(contact["omar"])
