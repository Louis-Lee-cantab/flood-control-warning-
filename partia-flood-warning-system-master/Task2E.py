# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # Fetch data over past 2 days
    dt = 10
    x=stations_highest_rel_level(stations,5)
    for station, ratio in x:
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        print(station.name)
        plot_water_levels(station, dates, levels)
        



if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
