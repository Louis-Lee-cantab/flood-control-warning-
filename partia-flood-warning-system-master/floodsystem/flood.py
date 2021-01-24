from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    stationsleveloverthreshold=[]
    for station in stations:
        if station.relative_water_level() == None:
            continue
        if station.relative_water_level()>tol:
            stationsleveloverthreshold.append((station,station.relative_water_level()))

    stationsleveloverthreshold=sorted_by_key(stationsleveloverthreshold,1)
    stationsleveloverthreshold.reverse()
    return stationsleveloverthreshold



def stations_highest_rel_level(stations, N):
    stationsratio=[]
    for station in stations:
        if station.relative_water_level()==None:
            continue
        else:
            stationsratio.append((station,station.relative_water_level()))

#sort with highest at level at the start
    stationsratio=sorted_by_key(stationsratio,1)
    stationsratio.reverse()
    #take the top 10
    stationshighestratio=stationsratio[:N]
    return stationshighestratio


