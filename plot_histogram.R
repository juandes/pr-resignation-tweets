require(ggplot2)
require(skimr)
require(bbplot)

df  <- read.csv("data/results/sentences_sentiment.csv")
skim(df)

ggplot(df, aes(score)) +
  geom_histogram(bins = 20) +
  ggtitle("Histogram of sentiment values", 
          subtitle = "Calculated from a sample of tweets containing the hashtag #RickyRenunció") +
  geom_vline(xintercept = mean(df$score))
  bbc_style() +
  xlab("score") +
  ylab("count") +
  theme(axis.title = element_text(size = 18), 
        plot.margin = unit(c(1.0,1.5,1.0,1.0), "cm"),
        axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)))
skim(df$score)

