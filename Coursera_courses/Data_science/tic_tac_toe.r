# The tic-tac-toe matrix has already been defined for you
ttt <- matrix(c("O", NA, "X", NA, "O", NA, "X", "O", "X"), nrow = 3, ncol = 3)

# define the double for loop
for (i in 1:nrow(ttt)) {
    for (j in 1:ncol(ttt)) {
        print(paste("On row",i,"and column",j,"board contains",ttt[i,j]))
    }
}