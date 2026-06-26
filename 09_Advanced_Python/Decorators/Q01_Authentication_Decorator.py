def authentication(func):
    def wrapper():
        print("Checking Authentication...")
        func()
    return wrapper
@authentication
def view_profile():
    print("Profile Opened")
view_profile()