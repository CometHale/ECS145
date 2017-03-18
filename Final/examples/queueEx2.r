#pushes in 1,2
#pop three times
#an empty queue will print out nothing
#pop will stop and print out an error

#*push returns the new queue structure but automatically updates the queue so there is no need for reassignment

source("../genfunc.r")
source("../queue.r")

q <- newqueue()

print("Pushing 1 and 2")
push(q, 1, "q")
push(q, 2, "q")
print(q)

print("Popping the queue twice")
pop(q, "q")
pop(q, "q")
print(q)
#queue is empty at this point
print("Pop the Queue")
pop(q, "q")

print(q)
