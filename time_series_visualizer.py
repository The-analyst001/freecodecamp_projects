import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv' , parse_dates=['date'] ).set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) | (df['value'] <= df['value'].quantile(0.975)) ]


def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(18,6)) 
    plt.plot(df.index , df['value'] , 'r', linewidth=1)
    plt.title ('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month']=df.index.month
    df['year']=df.index.year
    df_bar = df.groupby(['year','month']) ['value'].mean().unstack()
    
    # Draw bar plot
    fig = df_bar.plot.bar(legend = True , figsize = (8,8) ,xlabel='Years' , ylabel=('Average Page Views'))
    plt.legend(['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'Sepember', 'October', 'November', 'December'] , title = 'Months')
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig ,axs=plt.subplots(1,2,figsize=(12,6))
    axs[0] =sns.boxplot(x=df_box['year'],y=df_box['value'],ax=axs[0])
    axs[1] =sns.boxplot(x=df_box['month'],y=df_box['value'],ax=axs[1] , order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

    axs[0].set_title ('Year-wise Box Plot (Trend)')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')

     
    axs[1].set_title ('Month-wise Box Plot (Seasonality)')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
