# read command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# assign file path to variable
file_path <- args[1]

library(readr)

# read the TSV file
full_full <- readr::read_tsv(file_path, col_names = FALSE)
full_fullANI <- data.frame(full_full)
full_fullANI <- full_fullANI[,3]

# fit a linear model
l <- lm(full_fullANI ~ 1)  # (1 means no predictor variables, just the intercept)

# perform ANOVA
anova(l)

# check the normality of residuals
shapiro.test(l$residuals)

# check the homogeneity of variances
#bartlett_result <- bartlett.test(l$resid, rep(1, length(full_fullANI)))  # '1' represents the single strain

# Use nonparametric ANOVA, aka kruskal.test
#kruskal_result <- kruskal.test(full_fullANI, rep(1, length(full_fullANI)))

# LSD Test
library(agricolae)
an.m <- aov(full_fullANI ~ 1)
l <- LSD.test(an.m, "full_full", p.adj = "bonferroni")
l

# Bootstrap
all <- full_fullANI 
boot <- sample(all, size = 10000, replace = TRUE) # Bootstrap
d <- density(boot) # Kernel density estimation
d

library(ggplot2)
library(dplyr)

# Create data frame for bootstrapped values
df <- data.frame(boot)

# Create density plot
plot <- ggplot(df, aes(x = boot)) +
  geom_density(fill = "#69b3a2", color = "#e9ecef", alpha = 0.8) +
  ggtitle("Density plot of ANI value for full_full") +
  xlab("ANI values (bootstrapped)")

# Save plot as an image file
download_dir <- path.expand("~/Downloads/")  # Path to Downloads directory
plot_path <- file.path(download_dir, "density_plot.png")  # Full path for the plot
ggsave(plot_path, plot)

# Print the path where the plot is saved
print(plot_path)
