#ProbA.r

#secretencoder: encodes message into picture

#secretdecoder: decodes secret message (user should know startpix, stride, consec, etc)

library(pixmap)

convertToGreyIntensity <- function(msg) {
  substr <- strsplit(msg,'')[[1]][1:nchar(msg)] # splits up the string into a vector of individual characters
  unicode <- sapply(substr, utf8ToInt) # convert each char to Unicode code points
  unicode[length(unicode) + 1] <- 0 # adds a null to the end of the unicode msg
  encodedMsg <- unicode / 128
  return (encodedMsg)
} # converts a string to a vector of grey intensity floats for each char in the string

convertToChar <- function(encodedMsg) {
# encodedMsg is a vector of grey intensities that represents a char
  unicode <- round(encodedMsg * 128, digits=0)
  #print(unicode)
  msg <- sapply(unicode, intToUtf8)
  return (msg)
} # converts a vector of grey intensity floats into chars

consecChange <- function(currIndex, consec, indices, pixels) {
  # vector index of the starting column of the row
  c <- currIndex - consec*length(pixels[,1])
  if (col(pixels)[currIndex] - consec < 1 || c<=0) {
    c <- row(pixels)[currIndex] 
  }

  # vector index of the starting row of the column
  r <- currIndex - consec 
  # if the starting row# of the consecutive column indices vector is < 1 or the
  # starting vector index of the consecutive column indices vector is <= 0...
  # ex. [,1] [,2] [,3] [,4]
  # [1,]  1    4    7   10 
  # [2,]  2    5    8   *11*
  # [3,]  3    6    9   12
  # currIndex = 11, consec = 3, r = currIndex-consec = 11-3=8
  # row(pixels)[currIndex] = 2, so row(pixels)[currIndex] - consec = 2 - 3 < 1
  # enters the if statement and calculates r:
  # r = (4-1)*(3) + 1 = 10, so 10 is the starting index of the consecutive column indices vector
  if (row(pixels)[currIndex] - consec < 1 || r <= 0) {
    r <- (col(pixels)[currIndex]-1)*length(pixels[,1]) + 1
  }

  # check every combination of consec contiguous pixels
  while (c <= currIndex && r <= currIndex){
    #print("bye")
    if ((row(pixels)[r]+consec) <= length(pixels[,1]))
    {
      consecColIndices <- r:(r + consec)
      #sameCol <- col(pixels)[currIndex] == col(pixels)[consecColIndices] # a boolean vector of whether the consecutive indices are in the same column
      if (sum(consecColIndices %in% indices) > consec){
        return (TRUE)
      }
    }

    if ((col(pixels)[c]+consec*length(pixels[,1])) <= length(pixels[1,]))
    {
      consecRowIndices <- c:(c + consec*length(pixels[,1]))
      #sameRow <- row(pixels)[currIndex] == row(pixels)[consecRowIndices] # a boolean vector of whether the consecutive indices are in the same row
      if (sum(consecRowIndices %in% indices) > consec) {
        return (TRUE)
      }
    }
    
    c <- c + length(pixels[,1])
    r <- r + 1
  }
  #print("hi")
  return (FALSE)
} # checks if there are more than consec pixels changed in a row or a column

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
  return (larger)
} # determines GCD is 1 or not

secretencoder <- function(imgfilename, msg, startpix, stride, consec=NULL) {
  #Extra reading on subsetting:http://adv-r.had.co.nz/Subsetting.html
	img <- try(read.pnm(imgfilename,cellres=1)) #try opening (if error, stop running)
	if (class(img) == "try-error") { 
		stop("Could not open file. Stopping script.", call. = FALSE) 
	}

  # extract pixel data 
  pixels <- img@grey
  encodedImg <- img

  if(length(pixels) < length(msg)){
    stop("Message is too long to be encoded into this image. Stopping script.", call. = FALSE)
  }

  if (!is.null(consec)){
    if(consec < 0 ){
      stop("Consec can not be negative. Stopping script.", call. = FALSE)
    }
    # check if stride is prime to img size since if they aren't relatively prime, then striding will keep landing in an already embedded pixel
    # without ever visiting a new pixel
    if (gcd(length(img@grey), stride) != 1) {
      warning("Stride should be relatively prime to image size.")
    }
    if(consec >= 0){
      #avoid character loss, as overwriting a pixel more than once is not allowed. 
      #Exposure as a secret message carrier is also mitigated by not allowing more than consec contiguous pixels in any row or column to be altered.

      encodedMsg <- convertToGreyIntensity(msg)
      #print(encodedMsg)

      #create an empty vector of indices in pixels to embed each char of the secret message in
      indices <- vector(length=length(encodedMsg))
      i <- 1 # index of indices, aka index of encoded chars in encoded msg
      currIndex <- startpix # index in pixel
      for (encodedChar in encodedMsg) {
        #print(i)
        #check to make sure none of the pixels are altered more than once and also check that no more than consec con
        while (currIndex %in% indices || consecChange(currIndex, consec, indices, pixels)) {
          currIndex <- (currIndex + stride) %% length(pixels)
          currIndex <- ifelse(currIndex == 0, length(pixels), currIndex)
          print(currIndex)
        }

        indices[i] <- currIndex
        pixels[indices[i]] <- encodedChar
        currIndex <- (currIndex + stride) %% length(pixels)
        currIndex <- ifelse(currIndex == 0, length(pixels), currIndex)
        i <- i + 1
      }
      #How do we define the lengths of a row or column?  <--- necessary to answer to make sure no more
      #than consec pixels are changed in any row or column

      # If, while inserting the message bytes, one of the above conditions occurs, (more than consec pixels are changed or there are repeated indices)
      # then move stride pixels further along and try inserting at that new spot.
      # Iterate until an eligible pixel is found or you run out of pixels.
    }
  }
  else{
    # user opts for quick and dirty encoding
    encodedMsg <- convertToGreyIntensity(msg)
    lastpix <- (length(encodedMsg) + ((startpix-1)%/%stride)) * stride # last pixel for the last char in msg to embed in without wrapping (lastpix can be > length(pixels))
    indices <- seq(startpix, lastpix, stride) %% length(pixels) # a vector of indices in pixels to encode the msg in, wraps around to the beginning if reached the end
    indices <- ifelse(indices == 0, length(pixels), indices) # changes any zeros to the last pixel # of the image
    pixels[indices]  <- encodedMsg # assigns each of the encoded chars to the corresponding indices, may overwrite without limits
  }    

  #print(indices)
  encodedImg@grey <- pixels
  write.pnm(encodedImg, file='encodedImg.pgm') # save 
  return (encodedImg)
}

secretdecoder <- function(imgfilename,startpix,stride,consec=NULL) {
  img <- try(read.pnm(imgfilename,cellres=1)) #try opening (if error, stop running)
  if (class(img) == "try-error") { 
    stop("Could not open file. Stopping script.", call. = FALSE) 
  }

  # extract pixel data 
  pixels <- img@grey

  # creates an empty vector to hold each encoded char of the msg
  encodedMsg <- vector()

  indices <- vector()
  currIndex <- startpix
  encodedChar <- pixels[currIndex]
  while (encodedChar != 0){ # constructs encodedMsg vector
    indices <- c(indices, currIndex)
    encodedMsg <- c(encodedMsg, encodedChar)

    # proceed to find the next char
    currIndex <- (currIndex + stride) %% length(pixels)
    currIndex <- ifelse(currIndex == 0, length(pixels), currIndex)

    if (!is.null(consec)){
      while (currIndex %in% indices || consecChange(currIndex, consec, indices, pixels)) {
        currIndex <- (currIndex + stride) %% length(pixels)
        currIndex <- ifelse(currIndex == 0, length(pixels), currIndex)
      }
    }
    encodedChar <- pixels[currIndex]
  }

  #print(indices)
  #print(encodedMsg)
  decodedMsg <- convertToChar(encodedMsg) # vector of individual chars of the original msg
  #print(decodedMsg)
  originalMsg <- paste(decodedMsg, collapse="") # concatenates the chars into string

  return (originalMsg)
}