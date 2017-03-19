\name{newstack,push.stack,pop.stack,print.stack}
\alias{newstack}
\alias{push.stack}
\alias{pop.stack}
\alias{print.stack}

\title{Stack Data Structure}

\description{A class of functions for stack}

\usage{
	newstack()
	push(stack, element, name)
	pop(stack, name)
	print(stack)
}

\arguments{
	\item{stack}{An object of the class "stack"}
	\item{element}{Value to insert into the stack}
	\item{name}{A string of the global variable name to save the stack object in}
}

\details{An R version of a stack class, implementing LIFO. This was written for the final term project for ECS 145.
	
Here is an overview of the functions:

	\itemize{
		\item \code{newstack}: Creates a new stack object, containing numItems, and Items. numItems is a counter of the number of items in the stack. Items holds all the elements of the stack.

		\item \code{push.stack}: A generic function that appends an element to the end of the stack. Check out genfunc.r and genfunc.rd for more details.

		\item \code{pop.stack}: A generic function that removes the last element from the stack and returns the removed element. Check out genfunc.r and genfunc.rd for more details.

		\item \code{print.stack}: A generic function that prints out the elements in the stack according to the order the elements were inserted in. Nothing will output if stack is empty.
	}
}
	
\examples{
	#Example 1

	#pushes in 3,10,11
	#pops three times
	#push 100
	#pop twice
	#the last pop should return an error
	#results should be printed after each pop and push

	#push returns the new stack structure but automatically updates the stack so there is no need for reassignment
	print("Example 1: ")
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


	#Example 2
	
	#pushes in 'a', 'b' to a stack
	#push in 'c' to that same stack locally and copies that stack to another stack call myStack globally
	#check the class of the new variable myStack
	#print out both stacks to see the results
	#empty out stack
	#empty out myStack

	print("Example 2: ")
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
	print(myStack) #nothing outputs
}

\author{Sally Ly, Wai Ying Li, Haley Sanders}