##########################################
#Multiply a matrix by its transpose.
##########################################

##########################################
#Read in the arguements. Im expecting the
#path to the matix here.
##########################################
args <- commandArgs(TRUE)

matrix_in=args[1]
matrix_out=args[2]

###########################################
#read files in
###########################################
a<-as.matrix(read.csv(matrix_in, header=TRUE))

###########################################
#product at * a
###########################################
ata<-t(a)%*%a

###########################################
# write AMa to file somewhere
###########################################
write.table(ata, row.names=FALSE, col.names=FALSE, sep=",", file = matrix_out)
