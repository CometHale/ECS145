#pushes 3,5,2,7,-5,-90,11
#pops twice
#prints out resulting bintree

#push reassigns the new bintree to the old variable automatically
#after all pushes have occurred, bintree will be printed
#after each pop bintree will be printed

source("../genfunc.r")
source("../bintree.r")

tree <- newbintree()

print("Pushing 3,5,2,7,-2,10,11,-90")
push.bintree(tree,3,"tree")
push.bintree(tree,5,"tree")
push.bintree(tree,2,"tree")
push.bintree(tree,7,"tree")
push.bintree(tree,-2,"tree")
push.bintree(tree,10,"tree")
push.bintree(tree,11,"tree")
push.bintree(tree,-90,"tree")
print("Printing the bintree...")
print(tree)

print("Popping the BinTree.")
pop(tree,"tree")
print("Printing the bintree...")
print(tree)

print("Pop the BinTree.")
pop(tree,"tree")
print("Printing the bintree...")
print(tree)