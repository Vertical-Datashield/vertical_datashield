#####
#UNmask a matrix
#####

##########################################
#Read in the args. Im expecting
#Masking matrix path
#Matrix to be masked path
#Output locaion
##########################################
args <- commandArgs(TRUE)

masking_matrix_in=args[1]
data_matrix_in=args[2]
unmasked_matrix_out=args[3]

###########################################
#read files in
###########################################

a<-read.csv(data_matrix_in, header=FALSE)
ma<-read.csv(masking_matrix_in, header=FALSE)

print (a)
print (ma)

###########################################
#solve it
###########################################
#ama<-t(a) * ma
unmasked_matrix<-solve(as.matrix(ma)) %*% as.matrix(a)


print (unmasked_matrix)

###########################################
# write AMa to file somewhere
###########################################
#write.table(ama, row.names=FALSE, sep=",", file = output_ama)
write.table(unmasked_matrix, row.names=FALSE, col.names=FALSE, sep=",", file = unmasked_matrix_out)


