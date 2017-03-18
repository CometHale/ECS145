#Contains functions to create a new instance of a binary tree, print, and push/pop functions

newbintree <- function(){
	#max binary tree
	tree <- matrix(c(NA,NA,NA), nrow=1,ncol=3)
	class(tree) <- "binarytree"
	tree
}# constructor

push.bintree <- function(tree,item,name){

	left_children <- tree[,2]
	right_children <- tree[,3]
	missing_rchild <- which(is.na(right_children))[1]
	missing_lchild <- which(is.na(left_children))[1]

	if(is.na(tree[1,1])){ #first push
		tree[1,1] <- item
	}
	else{
		new_node <- c(item,NA,NA)

		if(item < tree[missing_lchild,1]){ #add item as a lhs child
			tree <- rbind(tree,new_node[])
			tree[missing_lchild,2] <- nrow(tree)
		}

		if(item > tree[missing_rchild,1]){ #add item as a rhs child
			tree <- rbind(tree,new_node[])
			tree[missing_rchild,3] <- nrow(tree)
		}
	}

	assign(name, tree, envir=.GlobalEnv)
}

pop.bintree <- function(tree,name){

	if(nrow(tree) != 1){
		values <- tree[,1] # values of all of the nodes
		minimum <- min(values)
		min_row <- which(values == minimum)
		tree <- tree[-min_row,] #remove the node representing the minimum value

		#update child node row numbers
		for(row in c(1:nrow(tree))){
			left_child <- tree[row,2]
			right_child <- tree[row,3]
			
			if(!is.na(left_child)){
				if(tree[row,2] >= min_row){
					tree[row,2] <- NA
				}
			}
			
			if(!is.na(right_child)){
				if(tree[row,3] >= min_row){
					tree[row,3] <- NA
				}
			}

		}

		if( nrow(tree) >= min_row ){ #there were rows below minimum's row

			for(row in c(min_row:nrow(tree))){
				left_children <- tree[,2]
				right_children <- tree[,3]

				missing_rchild <- which(is.na(right_children))[1] #find the first row that doesn't have an rhs child
				missing_lchild <- which(is.na(left_children))[1] #find the first row that doesn't have an lhs child

				if(tree[row,1] > tree[missing_rchild,1]){
					tree[missing_rchild,3] <- row
				}
				else if(is.na(missing_rchild)){
					if(tree[row,1] < tree[missing_lchild,1]){
						tree[missing_lchild,2] <- row
					}
				}
			}
		}
		
	}
	else{ #empty binary tree
		if(is.na(tree[1,1])){
			stop("No items in the binarytree. Stop.", call.=FALSE)
		}
		else{
			tree[1,1] <- NA
		}
	}

	assign(name, tree, envir=.GlobalEnv)
}

rec_print <- function(tree, row_number){

	node <- tree[row_number,1]
	left_child <- tree[row_number,2]
	right_child <- tree[row_number,3]

	if(!is.na(node)){
		print(node)	
	}

	if(row_number == nrow(tree)){ # base case
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

	if(is.na(tree[1,1])){
		print("")
		return
	}
	
	rec_print(tree,1)

}