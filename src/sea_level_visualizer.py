# Import required libraries
# Pandas: data loading and manipulation
# Matplotlib: plotting
# linregress: linear regression for trend analysis
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Load the EPA sea level dataset (1880–2013)
# float_precision is used to preserve numerical accuracy
df_1880_to_2013 = pd.read_csv('epa-sea-level.csv', float_precision="legacy")
df_1880_to_2013


# Create a scatter plot of observed sea level measurements
# X-axis: Year
# Y-axis: CSIRO Adjusted Sea Level
fig, ax = plt.subplots(figsize=(15, 5))
x = df_1880_to_2013['Year']
y = df_1880_to_2013['CSIRO Adjusted Sea Level']
ax.scatter(x, y)
ax.set(xlabel="Years", ylabel="CSIRO Adjusted Sea Level")


# Perform linear regression on the full dataset (1880–2013)
# This calculates the slope and intercept of the best-fit line
result = linregress(
    df_1880_to_2013['Year'],
    df_1880_to_2013['CSIRO Adjusted Sea Level']
)
result


# Plot the line of best fit over the original scatter plot
fig, ax = plt.subplots(figsize=(15, 5))
ax.scatter(x, y)
ax.set(xlabel="Years", ylabel="CSIRO Adjusted Sea Level")
ax.plot(
    df_1880_to_2013['Year'],
    result.slope * df_1880_to_2013['Year'] + result.intercept,
    'r'
)


# Filter the dataset to include only data from the year 2000 onward
# This allows analysis of more recent sea level trends
df_2000_to_2013 = df_1880_to_2013[df_1880_to_2013['Year'] >= 2000]
df_2000_to_2013


# Perform linear regression on the post-2000 data
result_1 = linregress(
    df_2000_to_2013['Year'],
    df_2000_to_2013['CSIRO Adjusted Sea Level']
)
result_1


# Plot both regression lines:
# - Full dataset trend
# - Post-2000 trend
fig, ax = plt.subplots(figsize=(15, 5))
ax.scatter(x, y)
ax.set(
    xlabel="Year",
    ylabel="Sea Level (inches)",
    title="Rise in Sea Level"
)
ax.plot(
    df_1880_to_2013['Year'],
    result.slope * df_1880_to_2013['Year'] + result.intercept,
    'g'
)
ax.plot(
    df_2000_to_2013['Year'],
    result_1.slope * df_2000_to_2013['Year'] + result_1.intercept,
    'red'
)


# Extend predictions to the year 2050 using regression
df = pd.read_csv("epa-sea-level.csv", float_precision="legacy")

plt.figure(1, figsize=(16, 9))
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], c="r")

# Regression using all available data
regress = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
last_year = df["Year"].max()

# Append future years up to 2050 for prediction
df = df.append([{"Year": y} for y in range(last_year + 1, 2050)])

plt.plot(
    df["Year"],
    regress.intercept + regress.slope * df["Year"],
    c="r",
    label="fit all"
)

# Regression using recent data (2000 onward)
df_recent = df.loc[(df["Year"] >= 2000) & (df["Year"] <= last_year)]
bestfit = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

df_recent = df_recent.append(
    [{"Year": y} for y in range(last_year + 1, 2050)]
)

plt.plot(
    df_recent["Year"],
    bestfit.intercept + bestfit.slope * df_recent["Year"],
    c="b",
    label="fit recent"
)

plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.savefig('sea_level_plot.png')


# Function used for automated testing / reuse
def draw_plot():
    """
    Generates a scatter plot of sea level data and overlays
    two regression lines:
    - One based on all historical data
    - One based on data from the year 2000 onward

    Returns:
        matplotlib.axes.Axes: Axis object for testing
    """
    df = pd.read_csv("epa-sea-level.csv", float_precision="legacy")

    plt.figure(1, figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], c="r")

    regress = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    last_year = df["Year"].max()
    df = df.append([{"Year": y} for y in range(last_year + 1, 2050)])

    plt.plot(
        df["Year"],
        regress.intercept + regress.slope * df["Year"],
        c="r",
        label="fit all"
    )

    df_recent = df.loc[(df["Year"] >= 2000) & (df["Year"] <= last_year)]
    bestfit = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    df_recent = df_recent.append(
        [{"Year": y} for y in range(last_year + 1, 2050)]
    )

    plt.plot(
        df_recent["Year"],
        bestfit.intercept + bestfit.slope * df_recent["Year"],
        c="b",
        label="fit recent"
    )

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.savefig('sea_level_plot.png')
    return plt.gca()
