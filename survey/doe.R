# Script to build conjoint survey using formr
# this is doe.R
library(here)

# get the full factorial design

ff <- expand.grid(
  rank = seq(1,25,1),
  gradtime = seq(4, 7, 1),
  stipend = seq(20,50,5),
  placement = seq(1,25,1)
)

# Sample from full factorial to populate doe
N    <- 4500
rows <- sample(x=seq(nrow(ff)), size=N, replace=T)
doe  <- ff[rows,]

# Add meta data
nAltsPerQ <- 3 # Number of alternatives per question
nQPerResp <- 10 # Number of questions per respondent
nRowsPerResp   <- nAltsPerQ * nQPerResp 
nResp          <- nrow(doe) / nRowsPerResp # Expecting 500 respondents
doe$respID     <- rep(seq(nResp), each=nRowsPerResp)
doe$qID        <- rep(rep(seq(nQPerResp), each=nAltsPerQ), nResp)
doe$altID      <- rep(seq(nAltsPerQ), nResp*nQPerResp)
doe$obsID      <- rep(seq(nResp * nQPerResp), each=nAltsPerQ)
row.names(doe) <- seq(nrow(doe))

# Save design
write.csv(doe, here::here('survey', 'doe.csv'), row.names=F)