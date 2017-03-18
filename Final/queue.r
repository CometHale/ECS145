#Contains functions to create a new instance of a queue, print, and push/pop functions

newqueue <- function() {
	que <- list()
  class(que) <- "queue"
	que$numItems <- 0 #no items in queue
	que$Items <- c(NA)
  que$NumQueue <- 0 #CHANGE LATER -gives each queue a 'number'
  return(que)
}

push.queue <- function(que, item, name) {  #name is the name of the queue/variable
  if (que$numItems == 0) {
    que$Items <- c(item)
  }
  else {
    que$Items <- c(que$Items, item)  
  }

  que$numItems <- que$numItems + 1 
  
  assign(name, que, envir=.GlobalEnv)

  return(que)
} #appends item to end of queue, returns the new object

pop.queue <- function(que, name) {
  if (que$numItems == 0) {
    stop("No items in the queue. Stop.", call.=FALSE)
  }
  popped <- que$Items[1]
  que$numItems <- que$numItems - 1
  que$Items <- que$Items[-1] #excludes first element ('pop')
  assign(name, que, envir=.GlobalEnv)

  return(popped)
} #removes item in front of queue, returns popped value

print.queue <- function(que) {
  if (que$numItems != 0) {
    print(que$Items)
  }
}