# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine
def stations_by_distance(stations, p):
    """1.B  In the submodule geo implement a function that, 
    given a list of station objects and a coordinate p,
     returns a list of (station, distance) tuples, where distance (float) is the distance of the station (MonitoringStation) from the coordinate p. 
    The returned list should be sorted by distance. """
    #create empty list
    stationsorteddistance=[]
    #looop over all stations
    for station in stations:
        #compute distance for each station
        distance=float(haversine(p,station.coord))
        #for each station create tuple containing station name and distance)
        s = (station.name, station.town, distance)
        #append each new entry to the list
        stationsorteddistance.append(s)
    #sort the list according to station distance
    stationsorteddistance=sorted_by_key(stationsorteddistance,2)
    return stationsorteddistance




def stations_within_radius(stations, centre, r):
    """1.C  In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within 
    radius r of a geographic coordinate x. The required function signature is:"""
    stationradius=[]
    for station in stations:
        #compute distance for each station
        distance=float(haversine(centre,station.coord))
        #append entry if the distance falls within stated radius
        if distance<=r:
            s = (station.name)
            stationradius.append(s)
#sort with ascending distance
    stationradius.sort()
    return stationradius




def rivers_with_station(stations):
    """1D.  In the submodule geo develop a function that, given a list of station objects, 
    returns a container (list/tuple/set) with the names of the rivers with a monitoring station"""
    riverswithstation=set()
    #loop over each station and check for entries that contain a river
    for station in stations:
        if station.river!=None:
            #add entry if there is a river
            riverswithstation.add(station.river)
            #sort in alphabetical order
    return sorted(riverswithstation)


def stations_by_river(stations):
    """print the names of the stations located on the following rivers in alphabetical order:"""
    riverswithstation=rivers_with_station(stations)
    stationsbyriver={}
    for river in riverswithstation:
        listofstations=[]

        for station in stations:
            #loop over stations and append to list if station corresponds to appropriate river
            if station.river==river:
                listofstations.append(station.name)
        #sort alphabetically
        stationsbyriver[river]=sorted(listofstations)
    return stationsbyriver



def rivers_by_station_number(stations, N):
    """1E.  Determine the N rivers with the greatest number of monitoring stations. 
    It should return a list of (river name, number of stations) tuples, sorted by the number of stations. 
    In the case that there are more rivers with the same number of stations as the N th entry, include these rivers in the list"""  
    stationsbyriver=stations_by_river(stations)
    convertedlist=[]
    for river, stations in stationsbyriver.items():
        #loop and find number of stations for each river
        convertedlist.append((river,len(stations)))

            #sort according to number of stations
    convertedlist=sorted_by_key(convertedlist,1)
    #reverse the list so that can start with river with greatest umber of stations
    convertedlist.reverse()
    copy=convertedlist
    #create final list without repeats first
    final=copy[:N]
    for x in range(N,len(copy)):
        #loop over and use copy for comprison
        if copy[x][1]==final[-1][1]:
            #after comparing, if there are rivers with same no of stations not in final, append to final
            final.append(copy[x])

    """
    for x in range (N):
        max=copy[:1][0][1]
        counter=0
        for y in copy:
            if y[1]==max:
                final.append(y)
                counter+=1
        for z in range (counter):
            del copy[0]"""

    return final



        





