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


def create_table(input_str: str) -> str:
    """Creates table."""
    table_data = create_schedule_string(input_str)
    max_time_width = len(max([x[0] for x in table_data], key=len))
    max_action_width = len(max([x[1] for x in table_data], key=len))
    table = []
    print(table_data)
    if len(table_data) == 0:
        return "----------------------\n"
    line = "-" * (max_time_width + max_action_width + 7)  # 7 tuleneb: 4 tühikud, 2 ääred ja 1 keskel
    header = f"| {'time':>{max_time_width}} | {'items':<{max_action_width}} |"
    table.append(line)
    table.append(header)
    table.append(line)
    for activity_tuple in table_data:
        table.append(f"| {activity_tuple[0]:>{max_time_width}} | {activity_tuple[1]:<{max_action_width}} |")
    table.append(line)
    print(table)
    return "\n".join(table)


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
    print(create_table("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst"))
