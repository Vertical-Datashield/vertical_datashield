#####
#Sum the rows of a matrix
#####

##########################################
#Read in the args. Im expecting
#Input data matrix
#Output locaion
##########################################
args <- commandArgs(TRUE)

data_matrix_in=args[1]
sums_out=args[2]


###########################################
#read files in
###########################################

a<-read.csv(data_matrix_in, header=FALSE)

#print("in mask_MT.R")
#print(a)
#print(ma)

sums <- colSums(a) 


print(sums)

###########################################
# write AMa to file somewhere
###########################################
#write.table(ama, row.names=FALSE, sep=",", file = output_ama)
write.table(sums, row.names=FALSE, col.names=FALSE, sep=",", file = sums_out)

