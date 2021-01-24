import matplotlib
import numpy as np

def polyfit(dates, levels, p):

    try:
        x = matplotlib.dates.date2num(dates)
        if x[0]==None:
            return None
        p_coeff = np.polyfit(x - x[0], levels, p)
        poly = np.poly1d(p_coeff)
    except Exception:
        return None
    return (poly,x)




def analyse(dates, levels, p, ratio):
    if ratio==None or levels==None or dates==None or polyfit(dates,levels,p)==None:
        return "Unable to analyse"
    try:
        poly, d0 = polyfit(dates,levels,p)
        dydx=np.polyder(poly)
        trend=dydx(d0[-1])
        if ratio>1:
            return (4,ratio,trend)
        elif trend>0 and ratio > 0.75:
            return (3,ratio,trend)
        elif trend > 0 and ratio > 0.5 and ratio < 0.75 or trend<0 and ratio > 0.75:
            return (2,ratio,trend)
        else:
            return (1,ratio,trend)
    
    except Exception:
        return "Unable to analyse"
    


    
