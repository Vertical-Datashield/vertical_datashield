#####
#generate masking vector
#####

##########################################
# arguments to be read in from elsewhere
##########################################
args <- commandArgs(TRUE)

output=args[1]
n=as.numeric(args[2])

###########################################
# create mask and write to the output file
###########################################
#n, min, max

#This will make a vector of n*n length
n_squared=n*n
mask <- runif(n_squared, 1, 10)
#mask <- diag(2)

#Turn it into a nxn matrix
dim(mask)<-c(n,n)

#mask <- runif(1, 1, 10)
write.table(mask, row.names=FALSE, col.names=FALSE, sep=",", file = output)


