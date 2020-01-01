from ..travelplanner import Passenger, Route, Journey
import numpy as np
import math
import pytest
from pathlib import Path

DIR = Path(__file__).parent


def test_walk_time():
    p = Passenger((1, 1), (5, 8), 10)
    expected = math.sqrt((1-5)**2 + (1-8)**2) * 10
    walk_time = p.walk_time()
    assert walk_time == pytest.approx(expected, 0.01)


def test_timetable():

    f = open(DIR / "route.csv", "w")
    f.write("10,8,A\n10,9,\n10,10,\n10,11,\n9,11,\n8,11,\n7,11,\n7,10,\n7,9,\n6,9,\n5,9,\n4,9,\n3,9,\n2,9,\n2,8,\n2,7,\n2,6,B\n2,5,\n2,4,\n2,3,\n2,2,\n2,1,\n1,1,\n0,1,\n0,2,\n0,3,C\n")
    f.close()

    r = Route(DIR / "route.csv")
    result = r.timetable()
    expected = {'A': 0, 'B': 160, 'C': 250}
    assert result == expected

    r = Route(DIR / "route.csv", 20)
    result = r.timetable()
    expected = {'A': 0, 'B': 320, 'C': 500}
    assert result == expected


def test_travel_time():
    john = Passenger(start=(0, 2), end=(8, 1), speed=15)
    mary = Passenger(start=(8, 2), end=(2, 4), speed=23)
    connor = Passenger(start=(10, 8), end=(1, 2), speed=28)
    route = Route(DIR / "route.csv")
    journey = Journey(route, [john, mary, connor])
    id = 0
    results = []

    for passenger in journey.passengers:
        results.append(journey.travel_time(id))
        id += 1

    expected = [{'bus': 0, 'walk': 120.93386622447824}, {
        'bus': 0, 'walk': 145.46477236774547}, {'bus': 250, 'walk': 39.59797974644666}]

    assert expected == results
