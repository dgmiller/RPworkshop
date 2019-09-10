# Simulate fake response data

library(here)
library(caret)

df <- read.csv(here::here('survey', 'doe.csv'))
head(df)

# need to one-hot encode the data
dfx <- dummyVars(" ~ .", data = df)
newdf <- data.frame(predict(dfx, newdata = df))
head(newdf)