x <- factor(c('no', 'yes', 'no', 'yes', 'no'))
print(x)
# [1] no  yes no  yes no 
# Levels: no yes

print(table(x))
# x
# no yes 
# 3   2

print(attributes(x))
# $levels
# [1] "no"  "yes"

# $class
# [1] "factor"