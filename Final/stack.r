# stack data structure class

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
	stack 
} # end push

pop.stack <- function(stack, name) {
	if (stack$numItems == 0) {
		stop("No items in the stack. Stop.", call.=FALSE)
	}
	popped <- stack$Items[stack$numItems]
	stack$Items <- stack$Items[-stack$numItems]
	stack$numItems <- stack$numItems - 1
	assign(name, stack, envir=.GlobalEnv)
	popped
} # end pop

# print(stack) will dispatch to print.stack
print.stack <- function(stack, name) {
	if (stack$numItems != 0) {
		print(stack$Items)
	}
} # end print.stack()