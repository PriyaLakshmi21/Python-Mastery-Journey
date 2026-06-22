subscripton=input("Is subscription is Active?(yes/no):")
age=int(input("Enter your age:"))
if subscripton=="yes" and age>=18:
    print("Access allowed to GPT-5 Premium")
else:
    print("Access Denied")