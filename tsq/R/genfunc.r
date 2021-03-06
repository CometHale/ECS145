#sets up generic functions pop and push 
#in the data structure files, use pop.bintree(), pop.stack(), etc 
#to so the generic function pop will dispatch to those functions

#for both functions:
#   dataStruct: the data structure object (either binary tree, stack, or queue)
#   name:(variable) name of the data structure (as a string) to assign the updated data structure as R does not allow passing-by-reference in functions
#     ie. x <- newqueue() , user will pass in "x" as name

#for push:
#   item: item to be pushed

pop <- function(dataStruct, name) UseMethod("pop")
push <- function(dataStruct, item, name) UseMethod("push")