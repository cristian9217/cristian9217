# File: analisis_pharmacies.R
# Author: Cristian M. Pagan 
# Date: February 15, 2026
# Purpose: Load and analyze the pharmacy
# dataset for insights extraction in R.

df_pharmacy <- read.csv("data/cleaned_pharmacies_sales.csv")

if (!exists("df_pharmacy") || nrow(df_pharmacy) == 0) {
  stop("df_pharmacy is empty or not loaded.")
}

print("File was loaded with success and save as dataframe!")

# Show dataframe structure
print("Estructura del DataFrame")
sapply(df_pharmacy, class)

# Show first few rows
print("Primeras filas del DataFrame")
print(head(df_pharmacy))

# Calculate and display average age
average_age <- mean(df_pharmacy$Age, na.rm = TRUE)
sprintf("La edad promedio de los clientes es %.0f años", average_age)

# Distribution by city
city_distribution <- table(df_pharmacy$City_Client)
cat("Customer distribution by city (top 5):\n")
print(head(sort(city_distribution, decreasing = TRUE), 5))

# Aggregate total sales by product category
total_sales_category <- aggregate(Total_Sale ~ Category, df_pharmacy, sum)
cat("Total sales per product category: \n")
print(total_sales_category[order(total_sales_category$Total_Sale), ])

# Sum total sales by product and show top 1.
product_sales <- aggregate(Total_Sale ~ Name_Product, df_pharmacy, sum)
cat("Product with the highest total sales:\n")
print(product_sales[order(-product_sales$Total_Sale), ][1, ])

# Total sales grouped by Month and Month_Name
cat("Total sales by month:\n")
print(aggregate(Total_Sale ~ Month + Month_Name, df_pharmacy, sum))

# Total sales per season
cat("Total sales by season:\n")
print(aggregate(Total_Sale ~ Season, df_pharmacy, sum))

# Count customers by Type_Plan
cat("Type of Plan among customers:\n")
print(table(df_pharmacy$Type_Plan))

# Calculate total sales from products not covered by a plan
covered_sales <- sum(df_pharmacy$Total_Sale[df_pharmacy$Covered_Plan == "N"])
total_sales <- sum(df_pharmacy$Total_Sale)
percentage_covered <- (covered_sales / total_sales) * 100

sprintf("Total sales not covered by a plan: $%.2f\n", covered_sales)
sprintf("This represents %.2f%% of total sales\n", percentage_covered)

# Calculate average quantity purchased per customer
average_quantity <- mean(df_pharmacy$Quantity)
sprintf("Average quantity per customer is %.2f\n", average_quantity)

# Total sales by store location
city_sales <- aggregate(Total_Sale ~ Location_Store, df_pharmacy, sum)
cat("Total sales by location store:\n")
print(city_sales[order(city_sales$Total_Sale), ])

## Sales Distribution by Product Category ##
# Filter data for 2023
df_2023 <- subset(df_pharmacy, Year == 2023)

# Sum total sales by category
category_sales <- aggregate(Total_Sale ~ Category, df_2023, sum)

# Pie chart of sales distribution
pie(category_sales$Total_Sale, labels = category_sales$Category,
  main = "Sales Distribution by Product Category in 2023",
  col = rainbow(nrow(category_sales)),
  clockwise = TRUE)

## Boxplots of Age and Total Sales
# Select columns
boxplot_data <- df_pharmacy[, c("Age", "Total_Sale")]

# Create side-by-side boxplots
par(mfrow = c(1, 2))  # 1 row, 2 columns
boxplot(boxplot_data$Age, main = "Age", col = "lightblue")
boxplot(boxplot_data$Total_Sale, main = "Total Sales", col = "lightgreen")
mtext("Boxplots of Age and Total Sales", outer = TRUE, cex = 1.5)

# Reset layout
par(mfrow = c(1,1))
