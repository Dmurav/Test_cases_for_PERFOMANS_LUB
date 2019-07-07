from collections import defaultdict
from csv import DictReader
from sys import argv


def solve(data):
    # maps time moment to visitors number change
    count_deltas = defaultdict(lambda: 0)
    for row in data:
        count_deltas[row['came_in']] += 1
        count_deltas[row['came_out']] -= 1

    # collect moments when visitors number changed
    # moments[0] - time when first visitors came in
    # moments[-1] - time when last visitors came out
    moments = sorted(count_deltas.keys())

    # counting visitors for each moment from start
    count = 0
    known_max = 0
    intervals = []
    for i in range(len(moments) - 1):
        start = moments[i]
        end = moments[i + 1]
        count += count_deltas[start]
        if count > known_max:
            # new max found
            known_max = count
            intervals = [(start, end)]
        elif count == known_max:
            # same max value again - append another interval
            intervals.append((start, end))

    return known_max, intervals


def read_data(filename):
    with open(filename) as f:
        csv_reader = DictReader(f)
        return list(csv_reader)


def main():
    if len(argv) < 2:
        filename = 'input.csv'
    else:
        filename = argv[1]

    data = read_data(filename)
    max_count, intervals = solve(data)

    print("Maximal number of visitors was", max_count)
    print("Time intervals:")
    for start, end in intervals:
        print(start, end)

if __name__ == '__main__':
    main()
