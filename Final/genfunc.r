#sets up generic functions pop and push 
#in the data structure files, use pop.bintree(), pop.stack(), etc 
#to so the generic function pop will dispatch to those functions

pop <- function(dataStruct, name) UseMethod("pop")
push <- function(dataStruct, item, name) UseMethod("push")