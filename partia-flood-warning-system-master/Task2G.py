import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit, analyse
from floodsystem.utils import sorted_by_key  # noqa

def run():

        # Build list of stations
        stations = build_station_list()

        update_water_levels(stations)
        # Fetch data over past 2 days
        dt = 10
        stations=sorted(stations, key=lambda x: x.name)


        severe=[]
        high=[]
        moderate=[]
        low=[]
        for station in stations[:10]:
                dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=dt))
                p=4
                risk = analyse(dates, levels, p, station.relative_water_level())
                if risk[0]==4:
                        severe.append((station,risk[1],risk[2]))
                if risk[0]==3:
                        high.append((station,risk[1],risk[2]))
                if risk[0]==2:
                        moderate.append((station,risk[1],risk[2]))
                if risk[0]==1:
                        low.append((station,risk[1],risk[2]))
                
                
        print("Severe:"+(str)(len(severe)))
        for station in severe:
                print("\n"+station[0].name+"   ratio:"+(str)(station[1])+"    trend:"+(str)(station[2]))
        print("\n\nHigh:"+(str)(len(high)))
        for station in high:
                print("\n"+station[0].name+"   ratio:"+(str)(station[1])+"    trend:"+(str)(station[2]))

        print("\n\nModerate:"+(str)(len(moderate)))
        for station in moderate:
                print("\n"+station[0].name+"   ratio:"+(str)(station[1])+"    trend:"+(str)(station[2]))

        print("\n\nLow:"+(str)(len(low)))
        for station in low:
                print("\n"+station[0].name+"   ratio:"+(str)(station[1])+"    trend:"+(str)(station[2]))


        



if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
