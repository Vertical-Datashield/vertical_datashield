#####
#To generate A.A or B.B
# ma * at * a
#####

##########################################
# these arguments to be read in from elsewhere e.g. fn_a_in <- commandArgs(7)
##########################################
args <- commandArgs(TRUE)

fn_a_in=args[1]
#fn_ma_in=args[1]
fn_ma_ata_out=args[2]

###########################################
#read files in
###########################################

a<-as.matrix(read.csv(fn_a_in, header=TRUE))
#ma<-read.csv(fn_ma_in, header=TRUE)

###########################################
#product at * a
#product ma * ata
###########################################
ata<-t(a)%*%a

#ma_ata<-ma * ata

###########################################
# write AMa to file somewhere
###########################################
write.table(ata, row.names=FALSE, col.names=FALSE, sep=",", file = fn_ma_ata_out)
