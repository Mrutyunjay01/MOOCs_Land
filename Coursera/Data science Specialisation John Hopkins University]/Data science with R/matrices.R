# matrices are vectors with a dimension attribute
# the dimension attribute is itself is an integer vector of length 2(row, col)

x <- matrix(nrow = 2, ncol = 3)
print(x)

##
#     [,1] [,2] [,3]
#[1,]   NA   NA   NA
#[2,]   NA   NA   NA
##
dim(x) # 2 3
attributes(x)
# $dim
# [1] 2 3

# matrixes are constructed column wise
m <- matrix(1:6, nrow = 2, ncol = 3)
print(m)

# matrics can also be created directly from vectors by adding a dimension attribute
m <- 1:10
dim(m) <- c(2, 5)
print(m)

# column binding and row binding
x <- 1:3
y <- 10:12

# column binding
cbind(x, y)

# row binding
rbind(x, y)