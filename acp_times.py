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
    speeds = {
                200: 15,
                400: 15,
                600: 15,
                1000: 11.428,
                1300: 13.333
    }
    if control_dist_km == 0:
        return arrow.get(brevet_start_time).format("ddd M/D H:mm")

    for min_speed in speeds:
        if control_dist_km <= min_speed:
            control_open = control_dist_km / speeds[min_speed]
            hrs = math.floor(control_open)
            mins = round((control_open - hrs) * 60)
            rusa = "{}H{}".format(hrs, mins)
            return arrow.get(brevet_start_time).shift(hours=hrs, minutes=mins).format("ddd M/D H:mm")


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
    """
    return arrow.get(brevet_start_time).format("ddd M/D H:mm")


