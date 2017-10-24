from acp_times import open_time, close_time
5, 11, 42, 63
def test_start_closure():
    # Testing if starting times is correct
    assert open_time(0, 200, "2017-01-01 00:00") == "Sun 1/1 0:00"
    assert close_time(0, 200, "2017-01-01 00:00") == "Sun 1/1 1:00"

def test_end_closure():
    # Testing to make sure the correct close times come out for each brevet distance
    # 200 km
    assert open_time(200, 200, "2017-01-01 00:00") == "Sun 1/1 5:53"
    assert close_time(200, 200, "2017-01-01 00:00") == "Sun 1/1 13:30"

    #300 km
    assert open_time(300, 300, "2017-01-01 00:00") == "Sun 1/1 9:00"
    assert close_time(300, 300, "2017-01-01 00:00") == "Sun 1/1 20:00"

    #400 km
    assert open_time(400, 400, "2017-01-01 00:00") == "Sun 1/1 12:08"
    assert close_time(400, 400, "2017-01-01 00:00") == "Mon 1/2 3:00"

    #600 km
    assert open_time(600, 600, "2017-01-01 00:00") == "Sun 1/1 18:48"
    assert close_time(600, 600, "2017-01-01 00:00") == "Mon 1/2 16:00"

    #1000 km
    assert open_time(1000, 1000, "2017-01-01 00:00") == "Mon 1/2 9:05"
    assert close_time(1000, 1000, "2017-01-01 00:00") == "Wed 1/4 3:00"

def test_end_110_percent():
    assert open_time(220, 200, "2017-01-01 00:00") == "Sun 1/1 5:53"
    assert close_time(220, 200, "2017-01-01 00:00") == "Sun 1/1 13:30"

    assert open_time(330, 300, "2017-01-01 00:00") == "Sun 1/1 9:00"
    assert close_time(330, 300, "2017-01-01 00:00") == "Sun 1/1 20:00"

    assert open_time(440, 400, "2017-01-01 00:00") == "Sun 1/1 12:08"
    assert close_time(440, 400, "2017-01-01 00:00") == "Mon 1/2 3:00"

    assert open_time(660, 600, "2017-01-01 00:00") == "Sun 1/1 18:48"
    assert close_time(660, 600, "2017-01-01 00:00") == "Mon 1/2 16:00"

    assert open_time(1100, 1000, "2017-01-01 00:00") == "Mon 1/2 9:05"
    assert close_time(1100, 1000, "2017-01-01 00:00") == "Wed 1/4 3:00"

def test_end_closure_too_far():
    # Testing to make sure it catches distances that are longer than 10% past the brevet distance
    assert open_time(230, 200, "2017-01-01 00:00") == ""
    assert close_time(230, 200, "2017-01-01 00:00") == ""

    #300 km
    assert open_time(340, 300, "2017-01-01 00:00") == ""
    assert close_time(340, 300, "2017-01-01 00:00") == ""

    #400 km
    assert open_time(450, 400, "2017-01-01 00:00") == ""
    assert close_time(450, 400, "2017-01-01 00:00") == ""

    #600 km
    assert open_time(670, 600, "2017-01-01 00:00") == ""
    assert close_time(670, 600, "2017-01-01 00:00") == ""

    #1000 km
    assert open_time(1200, 1000, "2017-01-01 00:00") == ""
    assert close_time(1200, 1000, "2017-01-01 00:00") == ""

def test_closure():
    # Testing to make sure correct time is listed for valid closure distances
    assert open_time(150, 200, "2017-01-01 00:00") == "Sun 1/1 4:25"
    assert close_time(150, 200, "2017-01-01 00:00") == "Sun 1/1 10:00"

    #300 km
    assert open_time(250, 300, "2017-01-01 00:00") == "Sun 1/1 7:27"
    assert close_time(250, 300, "2017-01-01 00:00") == "Sun 1/1 16:40"

    #400 km
    assert open_time(350, 400, "2017-01-01 00:00") == "Sun 1/1 10:34"
    assert close_time(350, 400, "2017-01-01 00:00") == "Sun 1/1 23:20"

    #600 km
    assert open_time(550, 600, "2017-01-01 00:00") == "Sun 1/1 17:08"
    assert close_time(550, 600, "2017-01-01 00:00") == "Mon 1/2 12:40"

    #1000 km
    assert open_time(950, 1000, "2017-01-01 00:00") == "Mon 1/2 7:18"
    assert close_time(950, 1000, "2017-01-01 00:00") == "Tue 1/3 22:38"


