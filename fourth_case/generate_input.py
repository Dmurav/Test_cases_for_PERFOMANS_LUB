from csv import DictWriter
from random import randint

BEGIN_HOUR = 8
END_HOUR = 20
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600


workday_sec = (END_HOUR - BEGIN_HOUR) * SECONDS_PER_HOUR


def generate_rows(count=1000, min_interval=5):

    def interval_to_time(interval_sec):
        hour = BEGIN_HOUR + interval_sec // SECONDS_PER_HOUR
        minute = (interval_sec % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
        second = (interval_sec % SECONDS_PER_HOUR) % SECONDS_PER_MINUTE
        return "{hour:0>2}:{minute:0>2}:{second:0>2}".format(hour=hour, minute=minute, second=second)

    for i in range(1, count + 1):
        # how many minutes visitor spent
        interval_sec = randint(5 * SECONDS_PER_MINUTE, 30 * SECONDS_PER_MINUTE)
        # when visitor came in
        came_in = randint(0, workday_sec - interval_sec)
        # when visitor came out
        came_out = came_in + interval_sec
        yield {
            'id': i,
            'came_in': interval_to_time(came_in),
            'came_out': interval_to_time(came_out),
        }


if __name__ == '__main__':
    with open('input.csv', 'w') as f:
        csv_writer = DictWriter(f, fieldnames=['id', 'came_in', 'came_out'])
        csv_writer.writeheader()
        csv_writer.writerows(generate_rows())
