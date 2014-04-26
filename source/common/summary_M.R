#####
#Calculate the summary data of a matrix
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

a<-read.csv(data_matrix_in, header=TRUE)


num_rows <- nrow(a)
num_cols <- ncol(a)

col_names <- colnames(a)

summary=rbind(num_rows,num_cols,col_names)

#print(sums)

###########################################
# write to file somewhere
###########################################
write.table(summary, row.names=TRUE, col.names=FALSE, sep=",", file = sums_out)


