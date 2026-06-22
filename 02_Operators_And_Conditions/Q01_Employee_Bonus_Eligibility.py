experience=int(input("Enter Your years of experience:"))
rating=float(input("Enter Rating:"))
salary=int(input("Enter Your current Salary:"))
if experience>=5 and rating>=4.5 and salary<10000:
    print("Eligible to receive Bonus")
else:
    print("Not Eligible to receive Bonus")