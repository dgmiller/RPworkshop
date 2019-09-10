# Simulate fake response data

library(here)
library(caret)
library(rstan)

df <- read.csv(here::here('survey', 'doe.csv'))
head(df)
df$price <- as.character(df$price)
df$screensize <- as.character(df$screensize)
df$memorygb <- as.character(df$memorygb)

# need to one-hot encode the data
dfx <- dummyVars(" ~ .", data = df)
newdf <- data.frame(predict(dfx, newdata = df))
head(newdf)

stan_data <- list(A = max(nedf$altID),
                  L = dim(newdf)[2] - 4,
                  T = max(newdf$qID),
                  R = max(newdf$respID),
                  C = 1,
                  X = X,
                  Y = Y,
                  Z = Z,
                  mu_mean = 0,
                  mu_scale = 5,
                  alpha_mean = 0,
                  alpha_scale = 10,
                  lkj_param = 2)

fit <- stan(file = 'hbmnl.stan', data = stan_data)