def infinite_counter(start=0):
    num = start
    while True:
        yield num
        num += 1
counter = infinite_counter(10)
for _ in range(5):
    print(next(counter))
