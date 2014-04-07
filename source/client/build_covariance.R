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

#Get the sums together in a vector
sums <- c(t(sum.a), t(sum.b))

#Join the various parts for the main matrix in columns
aa.ab<-cbind(a.a, a.b)
ba.bb<-cbind(b.a, b.b)

#Join the rows. We are putting the sums at the top.
cov.matrix<-rbind(sums,aa.ab, ba.bb)

print(cov.matrix)

#Add the sums to the front col
#stick a value in the first element
temp <- c(1,sums)
cov.matrix <- cbind(temp, cov.matrix)

#rename stuff. This is a major hack.
columnname=c("sums","weight.c","age.c","ht.c","bmi.c")
rowname=c("sums","weight.c","age.c","ht.c","bmi.c")
colnames(cov.matrix) <- columnname
rownames(cov.matrix) <- rowname

cov.matrix=as.matrix(cov.matrix)

print(cov.matrix)

###########################################
# write AMa to file somewhere
###########################################
#write.table(ama, row.names=FALSE, sep=",", file = output_ama)
#write.table(cov.matrix, row.names=FALSE, col.names=FALSE, sep=",", file = 'covariance_out.csv')


#ds.glm<-function(y,x){
  x<-"ht.c"
  y<-"weight.c"

  const<-"sums"

  sumsrow<-which(rownames(cov.matrix) == const)
  sumscol<-which(colnames(cov.matrix) == const)
  ycol<-which(colnames(cov.matrix) == y)
  yrow<-which(rownames(cov.matrix) == y)
  xcol<-which(colnames(cov.matrix) == x)
  xrow<-which(rownames(cov.matrix) == x)

  sums1<-cov.matrix[sumsrow,c(sumscol,xcol)]
  xrows<-cov.matrix[xrow,c(sumscol,xcol)]
  Y<-cov.matrix[yrow,c(sumscol,ycol)]

  xtx<-rbind(sums1, xrows)
  rownames(xtx)<-c(const, x)



  X<-solve(xtx)
  Y<-cov.matrix[yrow,c(sumscol,ycol)]
print(X)
print(Y)

class(cov.matrix)
class(X)
class(Y)

coeff<-X %*% Y
  print(coeff)
#}

#ds.glm("weight.c", "ht.c")
