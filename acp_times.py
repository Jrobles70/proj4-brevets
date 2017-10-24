"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#


def open_time( control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    # Add correct math for times
    max_speeds = {
        200: 34,
        400: 32,
        600: 30,
        1000: 28,
        1300: 26
    }

    brevet_open_default = {
        200: (5, 53),
        300: (9, 0),
        400: (12, 8),
        600: (18, 48),
        1000: (33, 5)
    }
    control_open = arrow.get(brevet_start_time)

    if control_dist_km == 0:
        return control_open.format("ddd M/D H:mm")

    if (control_dist_km >= brevet_dist_km) & (control_dist_km <= (brevet_dist_km * 1.1)):
        hrs, mins = brevet_open_default[brevet_dist_km]
        return control_open.shift(hours=hrs, minutes=mins).format("ddd M/D H:mm")

    if control_dist_km > (brevet_dist_km * 1.1):
        return ""

    control_dist_km = round(control_dist_km)
    start_time = 0
    first_key = next (iter (max_speeds.values()))
    last_key = 0

    for key in max_speeds:
        if control_dist_km > key:
            start_time += (key - last_key) / max_speeds[key]
            last_key = key
        else:
            if control_dist_km <= first_key:
                start_time += control_dist_km / first_key
            else:
                start_time += (control_dist_km - last_key) / max_speeds[key]
            if start_time != 0:
                hrs = math.floor(start_time)
                mins = round((start_time - hrs) * 60)
                rusa = "{}H{}".format(hrs, mins)
                return control_open.shift(hours=hrs, minutes=mins).format("ddd M/D H:mm")



def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
       13:30 for 200 KM, 20:00 for 300 KM, 27:00 for 400 KM, 40:00 for 600 KM, and 75:00 for 1000 KM
    """

    min_speeds = {
        200: 15,
        400: 15,
        600: 15,
        1000: 11.428,
        1300: 13.333
    }

    brevet_close_default = {
        200: (13, 30),
        300: (20, 0),
        400: (27, 0),
        600: (40, 0),
        1000: (75, 0)
    }

    control_close = arrow.get(brevet_start_time)

    if control_dist_km == 0:
        return arrow.get(brevet_start_time).shift(hours=1).format("ddd M/D H:mm")

    if (control_dist_km >= brevet_dist_km) & (control_dist_km <= (brevet_dist_km * 1.1)):
        hrs, mins = brevet_close_default[brevet_dist_km]
        return control_close.shift(hours=hrs, minutes=mins).format("ddd M/D H:mm")

    if control_dist_km > (brevet_dist_km * 1.1):
        return ""

    control_dist_km = round(control_dist_km)


    start_time = 0
    first_key = next (iter (min_speeds.values()))
    last_key = 0

    for key in min_speeds:
        if control_dist_km > key:
            start_time += (key - last_key) / min_speeds[key]
            last_key = key
        else:
            if control_dist_km <= first_key:
                start_time += control_dist_km / first_key
            else:
                start_time += (control_dist_km - last_key) / min_speeds[key]
            if start_time != 0:
                hrs = math.floor(start_time)
                mins = round((start_time - hrs) * 60)
                rusa = "{}H{}".format(hrs, mins)
                print("HOURS: {} MINS: {}, RUSA: {}, STARTTIME: {}".format(hrs, mins, rusa, start_time))
                return control_close.shift(hours=hrs, minutes=mins).format("ddd M/D H:mm")
