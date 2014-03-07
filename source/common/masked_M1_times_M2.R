#! /usr/bin/env Rscript

#####
#To generate A.B
# ma_at * b
#####
##########################################
# these arguments to be read in from elsewhere e.g. fn_a_in <- commandArgs(7)
##########################################
args <- commandArgs(TRUE)

fn_b_in=args[3]
fn_ma_at_in=args[2]

fn_ma_atb_out=args[4]


###########################################
#read files in
###########################################

b<-as.matrix(read.csv(fn_b_in, header=TRUE))
ma_at<-read.csv(fn_ma_at_in, header=TRUE)

###########################################
#product at * a
#product ma * ata
###########################################
ma_atb<-ma_at*b

#print(ma_atb)

###########################################
# write AMa to file somewhere
###########################################
write.table(ma_atb, row.names=FALSE, col.names=FALSE, sep=",", file = fn_ma_atb_out)
