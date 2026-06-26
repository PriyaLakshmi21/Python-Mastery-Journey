def logging(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Finished")
    return wrapper
@logging
def generate_report():
    print("Generating Report...")
generate_report()