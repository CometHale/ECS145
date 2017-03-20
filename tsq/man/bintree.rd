\name{newbintree,push.bintree,pop.bintree,print.bintree}
\alias{newbintree}
\alias{push.bintree}
\alias{pop.bintree}
\alias{print.bintree}

\title{Binary Tree Data Structure}

\description{A class of functions for binary trees}

\usage{
	newbintree()
	push(tree, item, name)
	pop(tree, name)
	print(tree)
}

\arguments{
	\item{tree}{An object of the class "bintree"}
	\item{item}{Value to insert into the binary tree}
	\item{name}{A string of the global variable name to save the binary tree object in}
	\item{row_number}{A row in the tree's data matrix, representing a node in the tree}
}

\details{An R version of a binary tree class. This was written for the final term project for ECS 145.
	
Here is an overview of the functions:

	\itemize{
		\item \code{newbintree}: Creates a new binary tree object, containing data. data holds all of the nodes of the tree.

		\item \code{push.bintree}: A generic function that inserts an element into the binary tree. Check out genfunc.r and genfunc.rd for more details.

		\item \code{pop.bintree}: A generic function that discards the smallest element from the binary tree . Check out genfunc.r and genfunc.rd for more details.

		\item \code{rec_print}: Recursively prints the value of the current node (row_number) before calling itself on the current node’s children.

		\item \code{print.bintree}: A generic function that prints out the elements in the binary tree according to the order the elements were inserted in. Nothing will output if binarytree is empty.
	}
}
	
\examples{
	#Example 1

	#pushes 2,1,3
	#pops four times
	#an empty bintree will print out nothing
	#attempting a pop on an empty bintree will produce an error
	#push reassigns the new bintree to the old variable automatically
	print("Example 1: ")
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

	#Example 2

	#pushes 3,5,2,7,-5,-90,11
	#pops twice
	#prints out resulting bintree

	#push reassigns the new bintree to the old variable automatically
	#after all pushes have occurred, bintree will be printed
	#after each pop bintree will be printed
	print("Example 2: ")
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
}

\author{Sally Ly, Wai Ying Li, Haley Sanders}