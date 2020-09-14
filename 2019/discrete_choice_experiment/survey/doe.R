# Script to build conjoint survey using formr
# this is doe.R
library(here)

# get the full factorial design

ff <- expand.grid(
  price = c("$329", "$399", "$429", "$459", "$529", "$549", "$559", "$679"),
  screensize = c('7.9 in', '10.2 in'),
  memorygb = c("32 GB", "64 GB", "128 GB", "256 GB"),
  color = c('Rose Gold', 'Space Grey', 'Silver'),
  cellular = c("WiFi only", "WiFi + Cellular")
)

# Sample from full factorial to populate doe
nAltsPerQ <- 4 # Number of alternatives per question
nQPerResp <- 8 # Number of questions per respondent
nResp <- 500 # Number of respondents
nRowsPerResp   <- nAltsPerQ * nQPerResp 
N    <- nResp * nRowsPerResp
rows <- sample(x=seq(nrow(ff)), size=N, replace=T)
doe  <- ff[rows,]

# Add meta data
doe$respID     <- rep(seq(nResp), each=nRowsPerResp)
doe$qID        <- rep(rep(seq(nQPerResp), each=nAltsPerQ), nResp)
doe$altID      <- rep(seq(nAltsPerQ), nResp*nQPerResp)
doe$obsID      <- rep(seq(nResp * nQPerResp), each=nAltsPerQ)
row.names(doe) <- seq(nrow(doe))

# Save design
write.csv(doe, here::here('survey', 'doe.csv'), row.names=F)
