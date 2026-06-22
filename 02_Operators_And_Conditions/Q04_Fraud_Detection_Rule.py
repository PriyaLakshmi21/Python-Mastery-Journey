amount = int(input("Enter transaction amount: "))
country = input("Enter country: ")
if amount > 50000 and country.lower() != "india":
    print("Suspicious Transaction")
else:
    print("Normal Transaction")