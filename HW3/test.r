source("ProblemA.r")

msg <- "Poem-a-Day is the original and only daily digital poetry series featuring over 200 new, previously unpublished poems by today's talented poets each year. On weekdays, poems are accompanied by exclusive commentary by the poets. The series highlights classic poems on weekends. Launched in 2006, Poem-a-Day is now distributed via email, web, and social media to 350,000+ readers free of charge and is available for syndication. For more information, contact poem-a-day@poets.org."

startpix <- 500
stride <- 11
cons <- 3
secretencoder("LLL.pgm", msg, startpix, stride, consec=cons)
text <- secretdecoder("encodedImg.pgm", startpix, stride, consec=cons)
print(text)