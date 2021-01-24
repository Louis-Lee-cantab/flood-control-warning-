from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key  # noqa

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    N=10
    x = stations_highest_rel_level(stations, N)
    y=[]
    for station, ratio in x:
        y.append((station.name,ratio))
    print (y)

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
