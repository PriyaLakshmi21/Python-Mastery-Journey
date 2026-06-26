class EvenNumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            even = self.current
            self.current += 2
            return even
        else:
            raise StopIteration
even_numbers = EvenNumberIterator(10)
for num in even_numbers:
    print(num, end=" ")