#pushes in 3,10,11
#pops three times
#push 100
#pop twice
#the last pop should return an error
#results should be printed after each pop and push

#push returns the new stack structure but automatically updates the stack so there is no need for reassignment

print("creating a new stack...")
stack <- newstack()

print("pushing 3, 10, 11 in...")
push(stack, 3, "stack")
push(stack, 10, "stack")
push(stack, 11, "stack")

print("popping 3 times...")
pop(stack, "stack") # should output 11
pop(stack, "stack") # should output 10
pop(stack, "stack") # should output 3
print(stack) # should output nothing

print("pushing 100...")
push(stack, 100, "stack")

print("popping 2 times...")
pop(stack, "stack") # should output 100
pop(stack, "stack") # should give an error