from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print station and latest level for first 5 stations in list
    tol=0.8
    x=stations_level_over_threshold(stations, tol)
    y=[]
    for station, ratio in x:
        y.append((station.name,ratio))
    print (y)

    # Alternative implementation
    # for station in [s for s in stations if s.name in names]:
    #     print("Station name and current level: {}, {}".format(station.name,
    #                                                           station.latest_level))


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()