# Simulate fake response data

library(here)

df <- read.csv(here::here('survey', 'doe.csv'))
head(df)

# need to effect encode the data