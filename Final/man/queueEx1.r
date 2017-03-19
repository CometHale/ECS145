#pushes in 1,2,3,4
#pops twice
#push 5
#pop once
#prints out resulting queue

#push returns the new queue structure but automatically updates the queue so there is no need for reassignment
#queue will be printed after a series of pushes or pops to see what is happening 

q <- newqueue()

print("Pushing 1,2,3,4")
push(q, 1, "q")
push(q, 2, "q")
push(q, 3, "q")
push(q, 4, "q")
print(q)

print("Pop the Queue")
pop(q, "q")
print(q)

print("Pushing 5")
push(q, 5, "q")
print(q)

print("Pop the Queue")
pop(q, "q")

print(q)
