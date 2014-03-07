#####
#AMa
#####

##########################################
# these arguments to be read in from elsewhere e.g. fn_a_in <- commandArgs(7)
##########################################
args <- commandArgs(TRUE)

fn_ma_in=args[1]
fn_a_in=args[2]
fn_ama_out=args[3]


###########################################
#read files in
###########################################

a<-read.csv(fn_a_in, header=TRUE)
ma<-read.csv(fn_ma_in, header=TRUE)

###########################################
#product
###########################################
ama<-t(a) * ma

###########################################
# write AMa to file somewhere
###########################################
#write.table(ama, row.names=FALSE, sep=",", file = output_ama)
write.table(ama, row.names=FALSE, sep=",", file = fn_ama_out)


