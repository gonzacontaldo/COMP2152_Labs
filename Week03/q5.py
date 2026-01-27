contacts = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9999"}


print("Alice's contact number is:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob's number:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All contacts keys:", contacts.keys())

print("All phone numbers:", contacts.values())

print("Total number of contacts:", len(contacts))
