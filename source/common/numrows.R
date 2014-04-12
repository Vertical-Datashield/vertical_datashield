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
num_rows_out=args[2]


###########################################
#read files in
###########################################

a<-read.csv(data_matrix_in, header=FALSE)

num_rows <- numrows(a) 


#print(sums)

###########################################
# write to file somewhere
###########################################
write.table(num_rows, row.names=FALSE, col.names=FALSE, sep=",", file = num_rows_out)


