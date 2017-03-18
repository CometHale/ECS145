#Contains functions to create a new instance of a stack, print, and push/pop functions
#name is the global variable to save the stack as

newstack <- function() {
	stack <- list()
	class(stack) <- 'stack'
	stack$numItems <- 0 # no items in stack
	stack$Items <- c(NA)
	stack # return
} # end stack constructor

push.stack <- function(stack, element, name) {
	if(stack$numItems == 0){
		stack$Items <- c(element)
	}
	else stack$Items <- c(stack$Items, element)
	stack$numItems <- stack$numItems + 1
	assign(name, stack, envir=.GlobalEnv)
	stack # automatically calls print.stack if not assigned
} # end push, returns the stack obj

pop.stack <- function(stack, name) {
	if (stack$numItems == 0) {
		stop("No items in the stack. Stop.", call.=FALSE)
	}
	popped <- stack$Items[stack$numItems]
	stack$Items <- stack$Items[-stack$numItems]
	stack$numItems <- stack$numItems - 1
	assign(name, stack, envir=.GlobalEnv)
	popped # automatically calls print.default if not assigned
} # end pop, returns popped value

# print(stack) will dispatch to print.stack
print.stack <- function(stack) {
	if (stack$numItems != 0) {
		print(stack$Items)
	}
} # end print.stack()