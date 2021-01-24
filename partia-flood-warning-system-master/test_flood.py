from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key  # noqa

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    tol=0.8
    x=stations_level_over_threshold(stations, tol)
    y=[]
    for station, ratio in x:
        y.append((station.name,ratio))
    #assert that correct tol is taken
    for i in range(len(y)):
        assert y[i][1]>=tol

from floodsystem.flood import stations_highest_rel_level
def test_stations_highest_rel_level():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)
    N=10
    x = stations_highest_rel_level(stations, N)
    y=[]
    for station, ratio in x:
        y.append((station.name,ratio))
    #check that top 10 are taken
    a=sorted_by_key(y,1)
    a.reverse()
    assert a==y