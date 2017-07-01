# Simple example
a = [1, 2, 3, 4]
result = [i**2 for i in a]
print(result)

# Example with if condition

b = ["list", "goal", "gate", "touch"]
result1 = [element for element in b if element.startswith("g")]
print(result1)

#Looping over more than 1 collection
c = [1, 2, 4, 5]
d = [3, 4, 2, 6]
result2 = [i*e for i in c for e in d]
print(result2)
