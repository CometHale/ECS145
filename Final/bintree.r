
newbintree <- function(array,mintree=FALSE){

	#allow for input vector
	#allow for mintree or maxtree?

	if(mintree){
		if(missing(array)){
			new_tree <- matrix(c(NA,NA,NA), nrow=1,ncol=3)
		}
		else{
			array <- sort(array, decreasing=TRUE)
			count <- 0
			for(elem in array){
				if(count < 4){
					
				}
				else{
					count <- 0
				}
			}
			new_tree <- matrix()
		}
		
		classes <- c("binarytree", "mintree")
	}
	else{
		if(missing(array)){
			new_tree <- matrix(c(NA,NA,NA), nrow=1,ncol=3)
		}
		else{
			array <- sort(array)
			new_tree <- matrix()
		}

		classes <- c("binarytree", "maxtree")
	}

	
	
	class(new_tree) <- classes
}# constructor