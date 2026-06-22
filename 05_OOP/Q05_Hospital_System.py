class Hospital:
    def __init__(self,name,disease):
        self.name=name
        self.disease=disease
    def display(self):
        print(f"{self.name} has {self.disease}")
hsp=Hospital("Priya","Cold")
hsp.display()    