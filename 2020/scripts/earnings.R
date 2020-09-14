### !!! IMPORTANT !!! ###
### Set your working directory to the filepath of this file using setwd()

### DATA ###

# Load the data set
GetData <- function(datafile) {
  earnings <- read.csv(datafile)
  # z-standardize height
  earnings$z_height <- with(earnings, (height - mean(height))/sd(height))
  earnings
}


# File to write output of lm
write2file <- function(fname, regformula, regdata) {
  fitted.model <- lm(formula = regformula, data = regdata)
  sink(file = fname, append = FALSE) # create an empty file named fname
  print(Sys.time(), quote = FALSE)
  print(summary(fitted.model))
  closeAllConnections()
  fitted.model
}


### REGRESSIONS ###

# Load data
earnings <- GetData("~/Desktop/earnings.csv")

### Linear Models ###

# [1] Regress earnings on height
reg01 <- function() {
  # fit a linear model to the data
  fitted.model <- write2file("reg01.txt", earn ~ height, earnings)
  
  # graph the data and the regression line
  png("reg01.png") # open a png file
  plot(earnings$height, earnings$earn, xlim = c(40, 90), xlab = "height", ylab = "earnings")
  abline(fitted.model, col = "red") # plot the regression line
  dev.off() # close the file
}

# [2] Regress earnings (in thousands of dollars) on height
reg02 <- function() {
  # fit a linear model to the data
  fitted.model <- write2file("reg02.txt", earnk ~ height, earnings)
  
  # graph the data and the regression line
  png("reg02.png") # open a png file
  plot(earnings$height, earnings$earnk, xlim = c(40, 90), xlab = "height", ylab = "earnings")
  abline(fitted.model, col = "red") # plot the regression line
  dev.off() # close the file
}


# [3] Same as [2] plus a control for male/female differences
reg03 <- function() {
  fitted.model <- write2file("reg03.txt", earnk ~ height + male, earnings)
  png("reg03.png")
  plot(earnings$height, earnings$earnk, xlim = c(50,90), ylim = c(-10, 200), xlab = "height", ylab = "earnings")
  model.coefs <- coef(fitted.model)
  abline(a = model.coefs[1], b = model.coefs[2], col = "red")
  abline(a = model.coefs[1] + model.coefs[3], b = model.coefs[2], col = "blue")
  dev.off()
}

# [4] Same as [3] plus a height x male interaction
reg04 <- function() {
  fitted.model <- write2file("reg04.txt", earnk ~ height + male + height:male, earnings)
  png("reg04.png")
  plot(earnings$height, earnings$earnk, xlim = c(50,90), ylim = c(-10, 200), xlab = "height", ylab = "earnings")
  model.coefs <- coef(fitted.model)
  abline(a = model.coefs[1], b = model.coefs[2], col = "red")
  abline(a = model.coefs[1] + model.coefs[3], b = model.coefs[2] + model.coefs[4], col = "blue")
  dev.off()
}


### Log-Linear Models ###

# [5] Regress log earnings on height
reg05 <- function() {
  earn.nonzero <- subset(earnings, earn>0)
  fitted.model <- write2file("reg05.txt", log(earn) ~ height, earn.nonzero)
  png("reg05.png")
  plot(earn.nonzero$height, log(earn.nonzero$earn), xlab = "height", ylab = "log earnings")
  abline(fitted.model)
  dev.off()
}

# [6] Same as [5] but using base 10 logarithm instead of natural log
reg06 <- function() {
  earn.nonzero <- subset(earnings, earn>0)
  fitted.model <- write2file("reg06.txt", log10(earn) ~ height, earn.nonzero)
  png("reg06.png")
  plot(earn.nonzero$height, log10(earn.nonzero$earn), xlab = "height", ylab = "log10 earnings")
  abline(fitted.model)
  dev.off()
}

# [7] Same as [5] plus a control for male/female differences
reg07 <- function () {
  earn.nonzero <- subset(earnings, earn>0)
  fitted.model <- write2file("reg07.txt", log(earn) ~ height + male, earn.nonzero)
  png("reg07.png")
  plot(earn.nonzero$height, log(earn.nonzero$earn), xlab = "height", ylab = "log earnings")
  model.coefs <- coef(fitted.model)
  abline(a = model.coefs[1], model.coefs[2], col = "red")
  abline(a = model.coefs[1] + model.coefs[3], b = model.coefs[2], col = "blue")
  dev.off()
}

# [8] Regress log earnings on log height plus a control for male/female differences
reg08 <- function() {
  earn.nonzero <- subset(earnings, earn>0)
  fitted.model <- write2file("reg08.txt", log(earn) ~ log(height) + male, earn.nonzero)
  png("reg08.png")
  plot(log(earn.nonzero$height), log(earn.nonzero$earn), xlab = "height", ylab = "log earnings")
  model.coefs <- coef(fitted.model)
  abline(a = model.coefs[1], model.coefs[2], col = "red")
  abline(a = model.coefs[1] + model.coefs[3], b = model.coefs[2], col = "blue")
  dev.off()
}

# [9] Same as [7] plus a height x male interaction
reg09 <- function() {
  earn.nonzero <- subset(earnings, earn>0)
  fitted.model <- write2file("reg09.txt", log(earn) ~ height + male + height:male, earn.nonzero)
  png("reg09.png")
  plot(earn.nonzero$height, log(earn.nonzero$earn), xlab = "height", ylab = "log earnings")
  model.coefs <- coef(fitted.model)
  abline(a = model.coefs[1], model.coefs[2], col = "red")
  abline(a = model.coefs[1] + model.coefs[3], b = model.coefs[2] + model.coefs[4], col = "blue")
  dev.off()
}

# [10] Same as [9] but with standardized height
reg10 <- function() {
  earn.nonzero <- subset(earnings, earn>0)
  fitted.model <- write2file("reg10.txt", log(earn) ~ z_height + male + z_height:male, earn.nonzero)
  png("reg10.png")
  plot(earn.nonzero$z_height, log(earn.nonzero$earn), xlab = "z-standardized height", ylab = "log earnings")
  model.coefs <- coef(fitted.model)
  abline(a = model.coefs[1], model.coefs[2], col = "red")
  abline(a = model.coefs[1] + model.coefs[3], b = model.coefs[2] + model.coefs[4], col = "blue")
  dev.off()
}

reg01()
reg02()
reg03()
reg04()
reg05()
reg06()
reg07()
reg08()
reg09()
reg10()




