##########################################
#Multiply a matrix by its transpose.
##########################################

##########################################
#Read in the arguements. Im expecting the
#path to the matix here.
##########################################
args <- commandArgs(TRUE)

masking_vector_in=args[1]
matrix_in=args[2]
matrix_out=args[3]

###########################################
#read files in
###########################################
a<-as.matrix(read.csv(matrix_in, header=TRUE))
v_m<-as.matrix(read.csv(masking_vector_in, header=TRUE))


###########################################
#product at * a
###########################################
ata<-t(a)%*%a

masked_ata <- v_m%*%ata

###########################################
# write AMa to file somewhere
###########################################
write.table(masked_ata, row.names=FALSE, col.names=FALSE, sep=",", file = matrix_out)
