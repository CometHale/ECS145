\name{pop,push}
\alias{pop}
\alias{push}

\title{Pop and Push Generic Functions}

\description{A file of pop and push generic functions used by the data structure classes.}

\usage{
	pop(dataStruct, name)
	push(dataStruct, item, name)
}

\arguments{
	\item{dataStruct}{An object of the class "stack", "queue", or "bintree"}
	\item{item}{Value to insert into the data structure}
	\item{name}{A string of the global variable name to save the data structure object in}
}

\details{Sets up generic functions, pop and push. In the data structure files, these functions will be used as pop.bintree(), pop.stack(), etc. By doing so, calling pop() or push() will dispatch to those functions. This was written for the final term project for ECS 145.
	
Here is an overview of the functions:

	\itemize{
		\item \code{pop}: A generic function that removes an element according to the nature of the data structure. 

		\item \code{push}: A generic function that inserts an element into the data structure.
	}

Check out the data structure files for example of how to use write using these generic functions.
}

\author{Sally Ly, Wai Ying Li, Haley Sanders}