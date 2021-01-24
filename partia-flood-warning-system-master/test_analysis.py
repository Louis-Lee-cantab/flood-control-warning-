from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
import numpy as np
import datetime as datetime

def test_analyse():
    stations = build_station_list()
    dt = 10
    stations=sorted(stations, key=lambda x: x.name)


    for station in stations[:10]:
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        p=4
        poly, d0 = polyfit(dates,levels,p)
        dydx=np.polyder(poly)
        assert dydx==np.poly1d.deriv(poly)
