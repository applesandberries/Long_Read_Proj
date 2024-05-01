# read command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# assign file paths to variables
A_to_A <- args[1]
B_to_B <- args[2]
A_to_B <- args[3]

# print the file paths (for debugging)
cat("File paths received:")
cat(A_to_A, B_to_B, A_to_B, sep = "\n")

library(ggplot2)
library(readr)

# read full-to-full ANI values for strain A (AtoA)
AtoA <- read_tsv(A_to_A, col_names = FALSE)
AtoA_ANI <- data.frame(AtoA)
AtoA_ANI <- AtoA_ANI[,3]

# read full-to-full ANI values for strain B (BtoB)
BtoB <- read_tsv(B_to_B, col_names = FALSE)
BtoB_ANI <- data.frame(BtoB)
BtoB_ANI <- BtoB_ANI[,3]

# read full-to-full ANI values for strain A to strain B (AtoB)
AtoB <- read_tsv(A_to_B, col_names = FALSE)
AtoB_ANI <- data.frame(AtoB)
AtoB_ANI <- AtoB_ANI[,3]

# choose one sub-to-full ANI value to add as a line
line_value <- AtoB_ANI[1]  

# create data frame for plotting full-full A to A comparison
df_AtoA <- data.frame(ANI = AtoA_ANI, Type = "A-to-A")

# create data frame for plotting full-full B to B comparison
df_BtoB <- data.frame(ANI = BtoB_ANI, Type = "B-to-B")

# create data frame for plotting full-sub A to B comparison
df_AtoB <- data.frame(ANI = AtoB_ANI, Type = "A-to-B")

# combine data frames
df_combined <- rbind(df_AtoA, df_BtoB, df_AtoB)

# filter out 100% ANIs
df_combined <- df_combined[df_combined$ANI < 100, ]

# create plot
ggplot(df_combined, aes(x = ANI, fill = Type)) +
  geom_density(alpha = 0.5) +
  geom_vline(aes(xintercept = line_value), color = "red", size = 1) + 
  labs(title = "Comparison of Full-to-Full and Full-to-Sub ANI Values",
       x = "ANI Values (Bootstrapped)",
       y = "Density",
       fill = "Comparison Type") +
  theme_minimal()



