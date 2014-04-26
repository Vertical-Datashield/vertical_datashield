#####
#Join all the bits up
#####

##########################################
#Read in the args. Im expecting
##########################################
args <- commandArgs(TRUE)

M1M1_path=args[1]
M1M2_path=args[2]
M2M1_path=args[3]
M2M2_path=args[4]
sum_M1_path=args[5]
sum_M2_path=args[6]
numrows_path=args[7]
covariance_out_path=args[8]


###########################################
#read files in
###########################################

a.a<-read.csv(M1M1_path, header=TRUE)
a.b<-read.csv(M1M2_path, header=TRUE)
b.a<-read.csv(M2M1_path, header=TRUE)
b.b<-read.csv(M2M2_path, header=TRUE)

sum.a<-read.csv(sum_M1_path, header=FALSE)
sum.b<-read.csv(sum_M2_path, header=FALSE)

numrows<-as.numeric(read.csv(numrows_path, header=FALSE))

###########################################
#Join them all up
###########################################

#Get the sums together in a vector
sums_vals <- c(t(sum.a), t(sum.b))

#Join the various parts for the main matrix in columns
aa.ab<-cbind(a.a, a.b)
ba.bb<-cbind(b.a, b.b)

#Join the rows. We are putting the sums at the top.
cov.matrix<-rbind(sums_vals,aa.ab, ba.bb)

#Add the sums to the front col
#stick a value in the first element
sums <- c(numrows,sums_vals)
cov.matrix <- cbind(sums, cov.matrix)

#rename the rows with the same names as the columns
rownames(cov.matrix) <- colnames(cov.matrix)

cov.matrix=as.matrix(cov.matrix)

print(cov.matrix)

write.table(cov.matrix, row.names=TRUE, col.names=TRUE, sep=",", file = covariance_out_path)


###########################################
# write AMa to file somewhere
###########################################
#write.table(ama, row.names=FALSE, sep=",", file = output_ama)
#write.table(cov.matrix, row.names=FALSE, col.names=FALSE, sep=",", file = 'covariance_out.csv')


#ds.glm<-function(y,x){
#  x<-"ht.c"
#  y<-"weight.c"

#  const<-"sums"

#  sumsrow<-which(rownames(cov.matrix) == const)
#  sumscol<-which(colnames(cov.matrix) == const)
#  ycol<-which(colnames(cov.matrix) == y)
#  yrow<-which(rownames(cov.matrix) == y)
#  xcol<-which(colnames(cov.matrix) == x)
#  xrow<-which(rownames(cov.matrix) == x)

#  sums1<-cov.matrix[sumsrow,c(sumscol,xcol)]
#  xrows<-cov.matrix[xrow,c(sumscol,xcol)]
#  Y<-cov.matrix[yrow,c(sumscol,ycol)]

#  xtx<-rbind(sums1, xrows)
#  rownames(xtx)<-c(const, x)



#  X<-solve(xtx)
#  Y<-cov.matrix[yrow,c(sumscol,ycol)]
#print(X)
#print(Y)

#class(cov.matrix)
#class(X)
#class(Y)

#coeff<-X %*% Y
#  print(coeff)
#}

#ds.glm("weight.c", "ht.c")
