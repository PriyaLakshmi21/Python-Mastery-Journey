class OnlinePlatform:
    def __init__(self,coursename,instructor):
        self.coursename=coursename
        self.instructor=instructor
    def respond(self):
        print(f"{self.coursename} is taught by {self.instructor}")
onlineplatform=OnlinePlatform("Python","Priya")
onlineplatform.respond()
    