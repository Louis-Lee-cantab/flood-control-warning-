from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()
    x=inconsistent_typical_range_stations(stations)
    y=[]
    for station in x:
        y.append(station.name)
    print (y)




if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()


