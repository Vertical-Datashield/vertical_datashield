vertical_datashield
===================

Starting to play with possible infrastructure designs for vertical datashield


This set up needs the source dir, the data dir, and a temp dir sitting at the same level. The temp dir actually gets built on the fly.

The controller starts it all off. The design choice here is that the python code does the main plumbing, and the R scripts do stuff with the data. As it stands the R scripts are kind of place holders - they will get more complex over time (which is one of the reasons it's not all just python).

I've recently generalised most of the code so it sits in 'common', the way it is called then governs what it does. This needs to be done further.

There is a bit of cheating going on here. The controller script runs code which makes files and stores them in directories corresponding to individual entities. The copying process which takes some intermediate data from one place to another would be moved out to being e.g. an API call, or an SCP etc. For not it is just convenient to demarkate the data like this.


A note on nomenclature:

Assuming two biobanks
A=biobank A
B=biobank B
C=client
M=general matrix
M_A=matrix from A
v=masking vector
m_a=masking vector for A
T=transpose e.g. AT
