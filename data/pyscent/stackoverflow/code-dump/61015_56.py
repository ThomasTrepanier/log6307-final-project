# python3
import sys

def compute_min_refills(distance, tank, stops):
    capacity_tank = tank
    refill = 0

    if capacity_tank >= distance:
        return 0
    if capacity_tank < stops[0] or (distance-stops[-1]) > capacity_tank:
        return -1

    for i in range(1, len(stops)):
        if (stops[i]-stops[i-1]) > capacity_tank:
            return -1
        if stops[i] > tank:
            tank = (stops[i-1] + capacity_tank)
            refill += 1
    if distance > tank:
        refill += 1

    return refill


    if __name__ == '__main__':
        d, m, _, *stops = map(int, sys.stdin.read().split())
        print(compute_min_refills(d, m, stops))
