\name{newqueue,push.queue,pop.queue,print.queue}
\alias{newqueue}
\alias{push.queue}
\alias{pop.queue}
\alias{print.queue}

\title{Queue Data Structure}

\description{A class of functions for queue}

\usage{
	newqueue()
	push(queue, item, name)
	pop(queue, name)
	print(queue)
}

\arguments{
	\item{que}{An object of the class "queue"}
	\item{item}{Value to insert into the queue}
	\item{name}{A string of the global variable name to save the queue object in}
}

\details{An R version of a queue class, implementing FIFO. This was written for the final term project for ECS 145.
	
Here is an overview of the functions:

	\itemize{
		\item \code{newqueue}: Creates a new queue object, containing numItems, and Items. numItems is a counter of the number of items in the queue. Items holds all the elements of the queue.

		\item \code{push.queue}: A generic function that appends an element to the end of the queue. Check out genfunc.r and genfunc.rd for more details.

		\item \code{pop.queue}: A generic function that removes the first element from the queue and returns the removed element. Check out genfunc.r and genfunc.rd for more details.

		\item \code{print.queue}: A generic function that prints out the elements in the queue according to the order the elements were inserted in. Nothing will output if queue is empty.
	}
}

\examples{
	#Example 1

	#pushes in 1,2,3,4
	#pops twice
	#push 5
	#pop once
	#prints out resulting queue

	#push returns the new queue structure but automatically updates the queue so there is no need for reassignment
	#queue will be printed after a series of pushes or pops to see what is happening 
	print("Example 1: ")
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


	#Example 2
	
	#pushes in 1,2
	#pop three times
	#an empty queue will print out nothing
	#pop will stop and print out an error

	#*push returns the new queue structure but automatically updates the queue so there is no need for reassignment

	print("Example 2: ")
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
}

\author{Sally Ly, Wai Ying Li, Haley Sanders}