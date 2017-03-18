#Contains functions to create a new instance of a binary tree, print, and push/pop functions

newbintree <- function(){
	#max binary tree
	tree <- list()
	class(tree) <- "bintree"
	tree$data <- matrix(c(NA,NA,NA), nrow=1,ncol=3)
	return(tree)
}# constructor

push.bintree <- function(tree,item,name){

	left_children <- tree$data[,2]
	right_children <- tree$data[,3]
	missing_rchild <- which(is.na(right_children))[1]
	missing_lchild <- which(is.na(left_children))[1]

	if(is.na(tree$data[1,1])){ #first push
		tree$data[1,1] <- item
	}
	else{
		new_node <- c(item,NA,NA)

		if(item > tree$data[missing_rchild,1]){ #add item as a rhs child
			tree$data <- rbind(tree$data,new_node[])
			tree$data[missing_rchild,3] <- nrow(tree$data)
		}
		else if(item < tree$data[missing_lchild,1]){ #add item as a lhs child
			tree$data <- rbind(tree$data,new_node[])
			tree$data[missing_lchild,2] <- nrow(tree$data)
		}

		
	}

	assign(name, tree, envir=.GlobalEnv)
}

pop.bintree <- function(tree,name){

	if(nrow(tree$data) - 1 > 1){
		values <- tree$data[,1] # values of all of the nodes
		minimum <- min(values)
		min_row <- which(values == minimum)
		tree$data <- tree$data[-min_row,] #remove the node representing the minimum value

		#update child node row numbers
		for(row in c(1:nrow(tree$data))){
			left_child <- tree$data[row,2]
			right_child <- tree$data[row,3]
			
			if(!is.na(left_child)){
				if(tree$data[row,2] >= min_row){
					tree$data[row,2] <- NA
				}
			}
			
			if(!is.na(right_child)){
				if(tree$data[row,3] >= min_row){
					tree$data[row,3] <- NA
				}
			}

		}

		if( nrow(tree$data) >= min_row ){ #there were rows below minimum's row

			for(row in c(min_row:nrow(tree$data))){
				left_children <- tree$data[,2]
				right_children <- tree$data[,3]

				missing_rchild <- which(is.na(right_children))[1] #find the first row that doesn't have an rhs child
				missing_lchild <- which(is.na(left_children))[1] #find the first row that doesn't have an lhs child

				if(tree$data[row,1] > tree$data[missing_rchild,1]){
					tree$data[missing_rchild,3] <- row
				}
				else if(is.na(missing_rchild)){
					if(tree$data[row,1] < tree$data[missing_lchild,1]){
						tree$data[missing_lchild,2] <- row
					}
				}
			}
		}
		
	}
	else{ #empty binary tree
		if(is.na(tree$data[1,1])){
			stop("No items in the binarytree. Stop.", call.=FALSE)
		}
		else{
			tree$data[1,1] <- NA
		}
	}

	assign(name, tree, envir=.GlobalEnv)
}

rec_print <- function(tree, row_number){

	node <- tree$data[row_number,1]
	left_child <- tree$data[row_number,2]
	right_child <- tree$data[row_number,3]

	if(!is.na(node)){
		print(node)	
	}

	if(row_number == nrow(tree$data)){ # base case
		return
	}

	if(!is.na(left_child)){
		rec_print(tree,left_child)
	}
	if(!is.na(right_child)){
		rec_print(tree,right_child)
	}

}

print.bintree <- function(tree){

	if(is.na(tree$data[1,1])){
		return
	}
	
	rec_print(tree,1)

}