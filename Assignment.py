import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("DailyDelhiClimate.csv")
data.head()

# convert the date column to datetime format
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

# extract the year and month from the date column
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data = data[:-1]

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# 3 Visualization functions


# Define a linePlot which group the data by year and month and calculate the mean temperature
def linePlot(df):
    """
        It create a list of the unique years in the data
        then plot each year's mean temperature as a separate line
    """
    grouped = df.groupby(['year', 'month']).mean()['meantemp']
    years = df['year'].unique()
    fig, ax = plt.subplots(figsize=(10, 6))
    for year in years:
        ax.plot(month_names, grouped[year], label=year)
    ax.set_xlabel('Month')
    ax.set_ylabel('Mean Temperature (°C)')
    ax.set_title('Mean Temperature in Delhi from 2013 to 2016')
    ax.legend()
    plt.show()
    return

# Defining a func that create a histogram of the mean temperature with 12 bins
def histogramPlot(df):
    plt.hist(df['meantemp'], bins=12, edgecolor="black")
    plt.xlabel('Mean Temperature (°C)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Mean Temperature in Delhi from 2013 to 2016')
    plt.show()
    return

# Define a func that create a box plot of the mean temperature, grouped by year
def boxPlot(df):
    df.boxplot(column='meantemp', by='year')
    plt.xlabel('Year')
    plt.ylabel('Mean Temperature (°C)')
    plt.title('Distribution of Mean Temperature in Delhi by Year')
    plt.show()
    return


# 1. Line Plot
linePlot(data)
# 2. Histogram
histogramPlot(data)
#3. Box Plot
boxPlot(data)

