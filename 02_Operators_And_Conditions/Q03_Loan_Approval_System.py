credit_score=int(input("Enter the credit score:"))
salary=int(input("Enter Salary:"))
if credit_score>=750 or salary>=1000000:
    print("Loan approved")
else:
    print("Loan rejected")