def cube_generator(n):
    for i in range(1, n + 1):
        yield i ** 3
n = int(input("Input a number: "))
cubes = cube_generator(n)
print("Cubes of numbers from 1 to", n)
for num in cubes:
    print(num)
