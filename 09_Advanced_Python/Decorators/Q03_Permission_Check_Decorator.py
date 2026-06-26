def permission(func):
    def wrapper():
        print("Checking Permission...")
        func()
    return wrapper
@permission
def view_salary():
    print("Salary Details")
view_salary()