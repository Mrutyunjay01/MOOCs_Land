# c() function is used to create vectors of objects
x <- c(0.5, 0.6)
print(x)

# vecotr() fun creates empty vectors
y <- vector(mode='numeric', length = 10L)
print(y)

# Mixing objects
# coerce occurs and make all the objects of same class
z <- c(1.7, 'a', TRUE)
print(z)

# Explicit coercioin
# objects can be explicitly coerced from one class to another using as.* fun if available
x <- 0:6
class(x)
as.numeric(x)
# 0 1 2 3 4 5 6
as.logical(x)
# FALSE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
as.character(x)
# "0" "1" "2" "3" "4" "5" "6"

### Nonsensical coercion results NAs


#### Lists
x <- list(1, 'a', TRUE, 1 + 4i)
print(x)