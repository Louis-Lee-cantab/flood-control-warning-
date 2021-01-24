from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    riverswithstation=rivers_with_station(stations)
    print(len(riverswithstation))
    riverswithstation=(riverswithstation)
    print(riverswithstation[:10])


    stationsbyriver=stations_by_river(stations)
    print(stationsbyriver["River Thames"])

    


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
