require(ggplot2)
require(skimr)
require(bbplot)
setwd("~/Development/pr-tweets")

data_dir <- 'data/results/'

verb.spanish.modified <- read.csv("~/Development/pr-tweets/data/results/VERB_Spanish_modified.csv")
draw_plots(verb.spanish.modified, "Verb", "Spanish")
adv.spanish.modified <- read.csv("~/Development/pr-tweets/data/results/ADV_Spanish_modified.csv")
draw_plots(adv.spanish.modified, "Adverb", "Spanish")
noun.spanish.modified <- read.csv("~/Development/pr-tweets/data/results/NOUN_Spanish_modified.csv")
draw_plots(noun.spanish.modified, "Noun", "Spanish")
adj.spanish.modified <- read.csv("~/Development/pr-tweets/data/results/ADJ_Spanish_modified.csv")
draw_plots(adj.spanish.modified, "Adjective", "Spanish")

verb.english.modified <- read.csv("~/Development/pr-tweets/data/results/VERB_English_modified.csv")
draw_plots(verb.english.modified, "Verb", "English")
adv.english.modified <- read.csv("~/Development/pr-tweets/data/results/ADV_English_modified.csv")
draw_plots(adv.english.modified, "Adverb", "English")
noun.english.modified <- read.csv("~/Development/pr-tweets/data/results/NOUN_English_modified.csv")
draw_plots(noun.english.modified, "Noun", "English")
adj.english.modified <- read.csv("~/Development/pr-tweets/data/results/ADJ_English_modified.csv")
draw_plots(adj.english.modified, "Adjective", "English")



draw_plots <- function(df, xlabel, language){
  df[,1] <- factor(df[,1], df[,1])
  # plot only the top 15
  df <- df[1:min(10, nrow(df)),]
  ggplot(data=df, aes(x=df[,1], y=value)) +
    geom_bar(stat = 'identity') +
    labs(title=sprintf("Top %ss from a sample of tweets containing the hashtag \"#RickyRenunció\"", tolower(xlabel)),
         subtitle = sprintf("As learned by spaCy's %s language model", language)) +
    bbc_style() +
    theme(axis.title = element_text(size = 18), 
          plot.margin = unit(c(1.0,1.5,1.0,1.0), "cm"),
          axis.text.x = element_text(angle = 45, hjust = 1),
          axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0))) +
    xlab(xlabel) + ylab('Value')
}




