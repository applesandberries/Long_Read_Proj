library(ggplot2)

generate_ani_comparison_plot <- function(A_to_A, B_to_B, A_to_B) {
  # Read full-to-full ANI values for A to A comparison
  AtoA <- readr::read_tsv(A_to_A, col_names = FALSE)
  AtoA_ANI <- data.frame(AtoA)
  AtoA_ANI <- AtoA_ANI[,3]
  
  # Read full-to-full ANI values for B to B comparison
  BtoB <- readr::read_tsv(B_to_B, col_names = FALSE)
  BtoB_ANI <- data.frame(BtoB)
  BtoB_ANI <- BtoB_ANI[,3]
  
  # Read full-to-sub ANI values for A to B comparison
  AtoB <- readr::read_tsv(A_to_B_, col_names = FALSE)
  AtoB_ANI <- data.frame(AtoB)
  AtoB_ANI <- AtoB_ANI[,3]
  
  # Choose one sub-to-full ANI value to add as a line
  line_value <- AtoB_ANI[1]  
  
  # Create data frame for plotting full-full A to A comparison
  df_AtoA <- data.frame(ANI = AtoA_ANI, Type = "A-to-A")
  
  # Create data frame for plotting full-full B to B comparison
  df_BtoB <- data.frame(ANI = BtoB_ANI, Type = "B-to-B")
  
  # Create data frame for plotting full-sub A to B comparison
  df_AtoB <- data.frame(ANI = AtoB_ANI, Type = "A-to-B")
  
  # Combine data frames
  df_combined <- rbind(df_AtoA, df_BtoB, df_AtoB)
  
  # Filter out 100% ANIs
  df_combined <- df_combined[df_combined$ANI < 100, ]
  
  # Create plot
  p <- ggplot(df_combined, aes(x = ANI, fill = Type)) +
    geom_density(alpha = 0.5) +
    geom_vline(aes(xintercept = line_value), color = "red", size = 1) + 
    labs(title = "Comparison of Full-to-Full and Full-to-Sub ANI Values",
         x = "ANI Values (Bootstrapped)",
         y = "Density",
         fill = "Comparison Type") +
    theme_minimal()
  
  print(p)
}

# Example usage
generate_ani_comparison_plot("/path/to/A_to_A_ANI.txt", "/path/to/B_to_B_ANI.txt", "/path/to/A_to_B_ANI.txt")
