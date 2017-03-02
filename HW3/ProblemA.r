#ProbA.r

#secretencoder: encodes message into picture

#secretdecoder: decodes secret message (user should know startpix, stride, consec, etc)

gcd <- function(num1, num2) {
  temp <- 1

  if (num1 > num2) {
    larger = num1
    smaller = num2
  }
  else {
    larger = num2
    smaller = num1
  }
  
  while(temp != 0) {
    temp = larger %% smaller
    larger = smaller
    smaller = temp
  }
  return larger
} #determines GCD is 1 or not

secretencoder <- function(imgfilename, msg, startpix, stride, consec=NULL) {
	img <- try(read.pnm(imgfilename)) #try opening (if error, stop running)
	if (class(img) == "try-error") { 
		stop("Could not open file. Stopping script.", call. = FALSE) 
	}

  #check if consec is prime to img size
  if (gcd(length(img@grey), as.numeric(consec)) != 1) {
    warning("consec should be relatively prime to image size.")
  }
    
}