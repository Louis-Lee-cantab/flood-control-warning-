import datetime
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_river
from haversine import haversine
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def test_stations_by_distance():

  # Build list of stations
    stations = build_station_list()
    p=(52.2053, 0.1218)
    x=stations_by_distance(stations,p)
    NoneType = type(None)
    #assert that the data types of each element in the tuples are correct and that they are sorted by distance
    for n in range(len(x)):
        assert isinstance(x[n][0],str)
        assert isinstance(x[n][1],str) or isinstance(x[n][1],NoneType)
        assert isinstance(x[n][2],float)
        if n!=(len(x)-1):
          assert x[n][2]<=x[n+1][2]




def test_stations_within_radius():
    # Build list of stations
    stations = build_station_list()
    centre=(52.2053, 0.1218)
    r=10
    x=stations_within_radius(stations, centre, r)
    assert len(x)==10
 
def test_rivers_with_station():
  stations = build_station_list()
  riverswithstation=rivers_with_station(stations)
  #check that there are no duplicates
  assert len(riverswithstation)==len(set(riverswithstation))
  #check that it is a list
  assert isinstance(riverswithstation,list)
  #check that it returns demonstration prog result
  assert riverswithstation[:1]==['Addlestone Bourne']

def test_stations_by_river():
  #check that it retirns demo prg result
  stations = build_station_list()
  stationsbyriver=stations_by_river(stations)
  assert stationsbyriver['River Thames']==['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock', 'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock', 'Clifton Lock', 'Cookham Lock', 'Cricklade', 'Culham Lock', 'Days Lock', 'Ewen', 'Eynsham Lock', 'Farmoor', 'Godstow Lock', 'Goring Lock', 'Grafton Lock', 'Hannington Bridge', 'Hurley Lock', 'Iffley Lock', 'Kings Lock', 'Kingston', 'Maidenhead', 'Mapledurham Lock', 'Marlow Lock', 'Marsh Lock', 'Molesey Lock', 'Northmoor Lock', 'Old Windsor Lock', 'Osney Lock', 'Penton Hook', 'Pinkhill Lock', 'Radcot Lock', 'Reading', 'Romney Lock', 'Rushey Lock', 'Sandford-on-Thames', 'Shepperton Lock', 'Shifford Lock', 'Shiplake Lock', 'Somerford Keynes', 'Sonning Lock', 'St Johns Lock', 'Staines', 'Sunbury  Lock', 'Sutton Courtenay', 'Teddington Lock', 'Thames Ditton Island', 'Trowlock Island', 'Walton', 'Whitchurch Lock', 'Windsor Park']


from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():
  stations = build_station_list()
  #try for 6 days
  N=6
  x=rivers_by_station_number(stations,N)
  assert len(x)>=N
  for a in x:
    #check that elements of list are tuples
    assert type(a)==tuple

from floodsystem.station import inconsistent_typical_range_stations 

def test_typical_range_consistent():
  stations = build_station_list()
  #try for addlestone
  for a in stations:
    if a.name=="Addlestone":
      assert a.typical_range == None or a.typical_range[0]>a.typical_range[1]
    else:
      pass
def test_inconsistent_typical_range_stations():
  stations = build_station_list()
  for a in inconsistent_typical_range_stations(stations):
    #check that each entry in the list has inconsistent range
    assert a.typical_range == None or a.typical_range[0]>a.typical_range[1]


