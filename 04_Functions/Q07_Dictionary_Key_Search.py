Employee_Info={"Eame":"Aditya","Id":"A105","Salary":"50000","Designation":"Manager"}
key=input("Enter the key:")
if key in Employee_Info:
    print(Employee_Info[key])
else:
    print("Key not found")