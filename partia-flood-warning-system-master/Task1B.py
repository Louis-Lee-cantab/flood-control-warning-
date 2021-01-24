# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():

    # Build list of stations
    stations = build_station_list()
    #state coordinate
    p=(52.2053, 0.1218)
    x=stations_by_distance(stations,p)
    #print nearest 10 stations
    print (x[:10])
    #print furthest 10 stations
    print (x[-10:])

   


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
