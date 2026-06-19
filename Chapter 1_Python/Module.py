# # we use "import" to import libraries
import pyjokes

# print function
print("Printing Jokes...")

# Variable -----> here "joke" is a variable. Variable stores data in memory
joke = pyjokes.get_joke()
joke1 = pyjokes.get_joke()
joke2 = pyjokes.get_joke()
joke3 = pyjokes.get_joke()
print(joke)
print(joke1)
print(joke2)
print(joke3)
print()

# functions -----> functions perform a task , called using (). for example

# built-in function
print("loop formula")
print()
# Range formula.
for i in range(5):
    print(pyjokes.get_joke()) # pyjokes.get_joke() is a "library function"
    print() #empty line