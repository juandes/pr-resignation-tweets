# this script is used to get the unique tweets
setwd("~/Development/pr-tweets")

library(readr)
tweets <- read_csv("Development/pr-tweets/tweets.txt", col_names = FALSE)
tweets$X2 <- NULL
tweets.unique <- unique(tweets)
write.table(tweets.unique, file = 'data/tweets_unique.txt', row.names = FALSE, col.names = FALSE, quote = FALSE)
