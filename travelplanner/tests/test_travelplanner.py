from ..travelplanner import Passenger, Route, Journey
import numpy as np
import math
import pytest


def test_walk_time():
    p = Passenger((1, 1), (5, 8), 10)
    expected = math.sqrt((1-5)**2 + (1-8)**2) * 10
    walk_time = p.walk_time()
    assert walk_time == pytest.approx(expected, 0.01)
