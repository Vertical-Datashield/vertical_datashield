#####
#generate masking vector
#####

##########################################
# arguments to be read in from elsewhere
##########################################
args <- commandArgs(TRUE)

output=args[1]

###########################################
# create mask and write to the output file
###########################################
mask <- runif(1, 1, 10)
write.table(mask, row.names=FALSE, sep=",", file = output)

