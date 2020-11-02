from datetime import timedelta


def clock_to_time_delta(time):
    """
    Convert time to time delta object

    :param time: string formatted as HH:MM:SS

    :example:
        >>> clock_to_time_delta("12:00:00")
        ... datetime.timedelta(seconds=43200)

    :return: timedelta object
    """
    return timedelta(hours=int(time[0:2]), minutes=int(time[3:5]), seconds=int(time[6:8]))
