"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    dict_schedule = {}
    for match in re.finditer(r"(\d{1,2})\D(\d{1,2})[ ]([a-zA-Z]+)", input_string):
        hour = int(match.group(1))
        minute = int(match.group(2))
        action = match.group(3)
        if 0 <= hour < 24 and 0 <= minute < 59:
            time = f"{hour:02}:{minute:02}"
            if time in dict_schedule:
                dict_schedule.get(time, []).append(action)
            else:
                dict_schedule[time] = [action]
    sorted_actions = sorted(dict_schedule.items(), key=lambda x: x[0])
    return str(sorted_actions)


def get_formatted_time(time: str) -> str:
    """Format 24 hour time to the 12 hour time."""
    units = time.split(":")
    hour = units[0]
    minute = units[1]
    ampm = ""
    if 0 <= int(hour) <= 11:
        ampm = "AM"
    elif int(hour) == 12:
        ampm = "PM"
    elif 12 < int(hour) < 24:
        ampm = "PM"
        hour = int(hour) - 12
    return f"{hour}:{minute:0>2} {ampm}"


def get_table_sizes(sorted: str) -> list:
    """Determines table size for time and action partition."""


def create_table(max_time_width: int, max_action_width: int) -> str:
    """Creates table."""
    table = []
    table.append("-" * (max_time_width + max_action_width + 7))  # 7 tuleneb: 4 tühikud, 2 ääred ja 1 keskel

    table.append("-" * (max_time_width + max_action_width + 7))


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
