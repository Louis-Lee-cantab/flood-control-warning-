import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from .analysis import polyfit

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')


    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    poly, d0 = polyfit(dates, levels, p)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.title(station)

    plt.plot(d0, levels, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    d1 = np.linspace(d0[0], d0[-1], 30)
    plt.plot(d1, poly(d1 - d0[0]))

    # Display plot
    plt.show()
