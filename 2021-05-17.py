def doodle_ripoff(*availabilities, meeting_length: int = 60) -> dict:
    """Make a Doodle Ripoff

    Return the earliest available time slot for a meeting together

    Schedule look like:
    Keys are Mo, Tu, We, Th, Fr because we don't do weekend meetings.
    Each day is a list of tuples with a start time and end time
    dict("Mo": [(start, end), (start, end), ...])

    The times are encoded as military time with minutes as decimal.
    3:30 PM is 15.30
    1:45 AM is 1.45

    e.g.:
    ("Max", {"Mo": [(9.00, 11.00), (11.30, 12.00), (15.30, 18.00)], "We": [(8.00, 20.30)]})

    Args:
        availabilities (str, dict(tuple(int, int))): Name and individual schedule
        meeting_length (int, optional): meeting length in minutes. Defaults to 60.
    """
    common_schedule = common_slots(availabilities)
    filtered_schedule = filter_slots(common_schedule, meeting_length)
    return get_earliest(filtered_schedule)


def common_slots(availabilities) -> dict:
    """Get common schedule from all availabilities

    Args:
        availabilities (list(dict)): List of dictionaries with availabilities

    Returns:
        dict: Return common schedule
    """
    open_slot = {"Mo": [], "Tu": [], "We": [], "Th": [], "Fr": []}

    # Go through all availabilities
    for i, (name, slots) in enumerate(availabilities):
        # Fill open slots with first person
        if i == 0:
            open_slot.update(slots)
            continue
        # Iterate through days
        for day in open_slot.keys():
            new_slots = []
            # Process individual slot per day
            for slot in slots.get(day, []):
                start, end = slot
                # Compare slots to open slots in day and update list with common availability
                for open_start, open_end in open_slot[day]:
                    new_start = max((start, open_start))
                    new_end = min((end, open_end))
                    if new_start < new_end:
                        new_slots.append((new_start, new_end))
            open_slot[day] = new_slots
    return open_slot


def filter_slots(schedule: dict, meeting_length: int) -> dict:
    """Go through schedule and filter for meeting length

    Args:
        schedule (dict): Common schedule 
        meeting_length (int): Meeting length in minutes

    Returns:
        dict: Slots with adequate time
    """
    # Go through common schedule
    for day, slots in schedule.items():
        remaining_slots = []
        # Filter available slots for length
        for slot in slots:
            start, end = map(to_minutes, slot)
            if (end - start) >= meeting_length:
                remaining_slots.append(slot)
        schedule[day] = remaining_slots
    return schedule


def get_earliest(schedule: dict) -> dict:
    """Return earliest meeting slot

    Args:
        schedule (dict): Dictionary with available slots

    Returns:
        dict: Dictionary with day and earliest slot
    """
    # Schedule is presorted, so return earliest
    for day, slots in schedule.items():
        if slots:
            return {day: min(slots)}


def to_minutes(time: float) -> int:
    """Convert time to minutes

    Args:
        time (float): Time in 15.30 format

    Returns:
        int: Minutes on day
    """
    hour = int(time)
    minutes = (time - hour) * 100
    return int(hour * 60 + minutes)


if __name__ == "__main__":

    name_1 = "tina"
    name_2 = "jerome"
    name_3 = "franz"
    name_4 = "ally"

    avail_1 = {
        "Mo": [(9.00, 11.00), (11.30, 12.00), (15.30, 18.00)],
        "We": [(8.00, 20.30)],
    }
    avail_2 = {"Mo": [(10.00, 15.00)], "Tu": [(10.00, 12.45)]}
    avail_3 = {"Tu": [(9.00, 11.00), (15.30, 17.45)], "Fr": [(8.00, 20.30)]}
    avail_4 = {
        "Fr": [(9.00, 11.00), (14.30, 17.15)],
        "Mo": [(10.30, 11.45)],
        "We": [(9.30, 10.30), (12.00, 12.30), (15.30, 16.00)],
    }

    print((name_1, avail_1), (name_2, avail_2))
    print(doodle_ripoff((name_1, avail_1), (name_2, avail_2)))
    print(doodle_ripoff((name_1, avail_1), (name_2, avail_2), meeting_length=30))

    print()
    print((name_2, avail_2), (name_3, avail_3))
    print(doodle_ripoff((name_2, avail_2), (name_3, avail_3)))

    print()
    print((name_3, avail_3), (name_4, avail_4))
    print(doodle_ripoff((name_3, avail_3), (name_4, avail_4)))


    print()
    print((name_1, avail_1), (name_4, avail_4))
    print(doodle_ripoff((name_1, avail_1), (name_4, avail_4)))

    print()
    print((name_1, avail_1), (name_2, avail_2), (name_4, avail_4))
    print(
        doodle_ripoff(
            (name_1, avail_1), (name_2, avail_2), (name_4, avail_4), meeting_length=15
        )
    )

    print()
    print((name_1, avail_1), (name_3, avail_3), (name_3, avail_3), (name_4, avail_4))
    print(
        doodle_ripoff(
            (name_1, avail_1), (name_2, avail_2), (name_3, avail_3), (name_4, avail_4)
        )
    )

