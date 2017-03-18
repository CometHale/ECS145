#pushes in 'a', 'b' to a stack
#push in 'c' to that same stack locally and copies that stack to another stack call myStack globally
#check the class of the new variable myStack
#print out both stacks to see the results
#empty out stack
#empty out myStack

source("../genfunc.r")
source("../stack.r")

print("Creating new stack...")
stack <- newstack()

print("Pushing 'a', 'b' to stack...")
push(stack, 'a', "stack")
push(stack, 'b', "stack")
print("Pushing 'c' to stack and results are saved to myStack...")
push(stack, 'c', "myStack") # append c to stack, but results are saved in myStack. stack is not changed globally
cat("Class of myStack is ")
cat(class(myStack)) # checks the class, should be of class "stack"
cat ("\n")
cat("myStack contains: ")
print(myStack)
cat("stack contains: ")
print(stack)

# below shows the emptying off stack
print("Popping stack 2 times...")
pop(stack, "stack")
pop(stack, "stack")
cat("stack now contains: ")
print(stack) #nothing outputs
cat("\n")
cat("myStack still contains: ")
print(myStack)

# below shows the emptying of myStack
print("Popping myStack 3 times...")
pop(myStack, "myStack")
pop(myStack, "myStack")
pop(myStack, "myStack")

cat("myStack now contains: ")
print(myStack)