import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv') 
    
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    plt.scatter(x,y)
  
    # Create first line of best fit
    lgs=linregress(x,y)
    x_ss = pd.array([i for i in range (1880,2050)])
    y_ss = lgs.slope*x_ss + lgs.intercept
    plt.plot(x_ss,y_ss,'b')
  
    # Create second line of best fit
    N_df= df[df['Year'] >= 2000]
    N_x = N_df['Year']
    N_y = N_df['CSIRO Adjusted Sea Level']

    N_lgs=linregress(N_x,N_y)
    N_x_ss = pd.array([i for i in range (2000,2050)])
    N_y_ss = N_lgs.slope*N_x_ss + N_lgs.intercept
    plt.plot(N_x_ss,N_y_ss,'black')    
  
    # Add labels and title
    plt.title ('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()