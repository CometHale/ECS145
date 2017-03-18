#pushes 2,1,3
#pops four times
#an empty bintree will print out nothing
#attempting a pop on an empty bintree will produce an error
#push reassigns the new bintree to the old variable automatically

source("../genfunc.r")
source("../bintree.r")

tree <- newbintree()

push.bintree(tree,2,"tree")
push.bintree(tree,1,"tree")
push.bintree(tree,3,"tree")

print("Printing the bintree...")
print(tree)

print("Popping the bintree three times.")
pop(tree,"tree")
pop(tree,"tree")
pop(tree,"tree")
print("Printing the bintree...")
print(tree)

#bintree is empty
print("Popping the bintree.")
pop(tree,"tree")

print("Printing the bintree...")
print(tree)

