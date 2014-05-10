
args <- commandArgs(TRUE)

input_cov_matrix=args[1]
input_x=args[2]
input_y=args[3]

print(input_cov_matrix)
print(input_x)
print(input_y)

###########################################
#read files in
###########################################
cov.matrix<-as.matrix(read.csv(input_cov_matrix, header=TRUE))
print(cov.matrix)
#x<-as.matrix(read.csv(input_x, header=FALSE))
x<-read.csv(input_x, header=FALSE)
print(x)

#y<-as.matrix(read.csv(input_y, header=FALSE))
y<-read.csv(input_y, header=FALSE)
print(y)
class(y)
dim(y)
print(y[1])
###########################################
#test files
###########################################
cov.matrix
x
y

############################################
#select column names from the varibale names files
#############################################
const<-"sums"
sumsrow<-which(rownames(cov.matrix) == const)
sumscol<-which(colnames(cov.matrix) == const)
ycol<-which(colnames(cov.matrix) == y[1])
print(ycol)
yrow<-which(rownames(cov.matrix) == y[1])
print(yrow)

xcol<-rep(NA, length(x))
xrow<-rep(NA, length(x))

for (i in 1:length(x)){
xcol[i]<-which(colnames(cov.matrix) == x[i])
xrow[i]<-which(rownames(cov.matrix) == x[i])
}

print(xcol)
print(xrow)


sums1<-cov.matrix[sumsrow,c(sumscol,xcol)]
xrows<-cov.matrix[xrow,c(sumscol,xcol)]


#########################################
#create XTX and XTY
##########################################
xtx<-rbind(sums1, xrows)
rownames(xtx)<-c(const, x) #XtX
Y<-cov.matrix[yrow,c(sumscol,xcol)] #XtY

#######################################
#calculate coeffs
#######################################
X<-solve(xtx)
	coeff<-X %*% Y
	print(coeff)