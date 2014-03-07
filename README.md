vertical_datashield
===================

Starting to play with possible infrastructure designs for vertical datashield


This set up needs the source dir, the data dir, and a temp dir sitting at the same level. The controller starts it all off. The design choice here is that the python code does the main plumbing, and the R scripts do stuff with the data. As it stands the R scripts are kind of place holders - they will get more complex over time (which is one of the reasons it's not all just python).