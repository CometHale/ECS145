#ProbA.r

#secretencoder: encodes message into picture

#secretdecoder: decodes secret message (user should know startpix, stride, consec, etc)

# encode <- function(stride,msg,startpix,pixels) {

# } # Does the message encoding

gcd <- function(num1, num2) {
  temp <- 1

  if (num1 > num2) {
    larger <- num1
    smaller <- num2
  }
  else {
    larger <- num2
    smaller <- num1
  }
  
  while(temp != 0) {
    temp <- larger %% smaller
    larger <- smaller
    smaller <- temp
  }
  return larger
} #determines GCD is 1 or not

secretencoder <- function(imgfilename, msg, startpix, stride, consec=NULL) {
  #Extra reading on subsetting:http://adv-r.had.co.nz/Subsetting.html
	img <- try(read.pnm(imgfilename)) #try opening (if error, stop running)
	if (class(img) == "try-error") { 
		stop("Could not open file. Stopping script.", call. = FALSE) 
	}

  if(consec < 0 ){
    stop("Consec can not be negative. Stopping script.", call. = FALSE)
  }
  # extract pixel data 
  pixels <- img@grey

  if(length(pixels) < length(msg)){
    stop("Message is too long to be encoded into this image. Stopping script.", call. = FALSE)
  }

  index <- startpix

  if (consec != NULL){
    #check if consec is prime to img size
    if (gcd(length(img@grey), as.numeric(consec)) != 1) {
      warning("consec should be relatively prime to image size.")
    }
    if(consec > 0){
      #avoid character loss, as overwriting a pixel more than once is not allowed. 
      #Exposure as a secret message carrier is also mitigated by not allowing more than consec contiguous pixels in any row or column to be altered.

      #create a vector of indices
      #check to make sure none of the indices are repeated

      #How do we define the lengths of a row or column?  <--- necessary to answer to make sure no more
      #than consec pixels are changed in any row or column

      # If, while inserting the message bytes, one of the above conditions occurs, (more than consec pixels are changed or there are repeated indices)
      # then move stride pixels further along and try inserting at that new spot.
       # Iterate until an eligible pixel is found or you run out of pixels.
    }
    else{ #consec is zero

    }
  }
  else{
    # user opts for quick and dirty encoding
    substr <- strsplit(msg,'')[[1]][1:nchar(msg)] # splits up the string into a vector of individual characters
    utf <- sapply(substr, utf8ToInt) # convert each char to Unicode code points
    utf <- utf / 128
    lastpix <- (nchar(msg) + ((startpix-1)%/%stride)) * stride # last pixel for the last char in msg to embed in without wrapping
    indices <- c(seq(startpix, lastpix, stride) %% length(pixels)) # a vector of indices in pixel to encode the msg in, wraps around to the beginning if reached the end
    pixels[indices]  <- utf
  }    
}