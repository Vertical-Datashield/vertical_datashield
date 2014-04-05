#####
#Join all the bits up
#####

##########################################
#Read in the args. Im expecting
#Masking matrix path
#Matrix to be masked path
#Output locaion
##########################################
#args <- commandArgs(TRUE)

#masking_matrix_in=args[1]
#data_matrix_in=args[2]
#unmasked_matrix_out=args[3]




###########################################
#read files in
###########################################

a.a<-read.csv('../temp/client/A.A.unmasked.csv', header=FALSE)
a.b<-read.csv('../temp/client/A.B.unmasked.csv', header=FALSE)
b.a<-read.csv('../temp/client/B.A.unmasked.csv', header=FALSE)
b.b<-read.csv('../temp/client/B.B.unmasked.csv', header=FALSE)

sum.a<-read.csv('../temp/client/sum.height_2.csv', header=FALSE)
sum.b<-read.csv('../temp/client/sum.weight_2.csv', header=FALSE)

###########################################
#Join them all up
###########################################

sums <- rbind(sum.a, sum.b)

aa.ab<-cbind(a.a, a.b)
ba.bb<-cbind(b.a, b.b)

cov.matrix<-rbind(aa.ab, ba.bb)

#Add the sums to the front col
cov.matrix <- cbind(sums,cov.matrix)

#Add the sums to the 
#sums <- t(sums)
temp <- cbind(1,t(sum.a),t(sum.b))
#print(sums)
print(temp)
#sums <- unname(sums)
#cov.matrix <- unname(cov.matrix)
unname(temp)
unname(cov.matrix)
cov.matrix <- rbind(temp, cov.matrix)



#cov.matrix<-rbind(t(sums),aa.ab, ba.bb)
#cov.matrix<-cbind(sumscol,cov.matrix)
#rownames(cov.matrix)[1]<-"sums"
#colnames(cov.matrix)[1]<-"sums"


###########################################
# write AMa to file somewhere
###########################################
#write.table(ama, row.names=FALSE, sep=",", file = output_ama)
write.table(cov.matrix, row.names=FALSE, col.names=FALSE, sep=",", file = 'covariance_out.csv')


