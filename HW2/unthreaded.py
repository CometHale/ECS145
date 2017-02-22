import time

def linelengths(filenm):
    startTime = time.time()
    file = open(filenm, 'r')
    index = 0
    lenlist = sum(1 for i in file) * [0]

    file.seek(0)

    for line in file:
        lenlist[index] = len(line) - 1 # subtract 1 to not count EOL
        index += 1

    print("Unthreaded version took %s seconds." % (time.time() - startTime))

    #return lenlist
