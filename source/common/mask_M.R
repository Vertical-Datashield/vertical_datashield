#####
#Mask a matrix
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
masked_matrix_out=args[3]


###########################################
#read files in
###########################################

a<-read.csv(data_matrix_in, header=TRUE)
ma<-read.csv(masking_matrix_in, header=TRUE)

###########################################
#product
###########################################
ama<-t(a) * ma

###########################################
# write AMa to file somewhere
###########################################
#write.table(ama, row.names=FALSE, sep=",", file = output_ama)
write.table(ama, row.names=FALSE, sep=",", file = masked_matrix_out)


