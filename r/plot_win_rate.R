library(jsonlite)  

# deserialize ranked fighter json into data frame
fighters = fromJSON(txt = "./text/ranked_fighters.txt")


abbreviate_weight_class = function(weight_class) {
  
}

fighters$win_rate = fighters$wins/(fighters$wins + fighters$draws + fighters$losses)





pd <- position_dodge(width = 0.5)
g = ggplot(fighters, aes(x = weight_class, y = win_rate, colour = weight_class)) + geom_point(position = position_jitter(width = 0.2))
g + theme(legend.position="none")  + labs(x = "Weight class", y = "Win-rate", title = "UFC top 15 win-rate by weight class")

  # geom_errorbar(aes(ymax = high, ymin = lo), width = 0.15, position = pd)  +
  # labs(x = 'cohort', y = 'CTR', title = 'win rate by weight class') 
  # geom_jitter(width = 0.3)
  
gg_sl_main
