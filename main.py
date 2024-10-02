def add_time(start, duration, day=None):
    # List of days for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse start time
    time_part, meridiem = start.split()
    start_hours, start_minutes = map(int, time_part.split(':'))

    # Convert PM hours to 24-hour format
    if meridiem == "PM" and start_hours != 12:
        start_hours += 12
    elif meridiem == "AM" and start_hours == 12:
        start_hours = 0

    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Add time
    total_minutes = start_minutes + duration_minutes
    total_hours = start_hours + duration_hours + (total_minutes // 60)
    new_minutes = total_minutes % 60
    new_hours = total_hours % 24

    # Calculate how many days have passed
    days_passed = total_hours // 24

    # Convert back to 12-hour format
    new_meridiem = "AM" if new_hours < 12 else "PM"
    new_hours = new_hours % 12 or 12  # Convert 0 hours to 12

    # If a day is provided, find the new day
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        day_string = f", {new_day}"
    else:
        day_string = ""

    # Handle day count in the output
    if days_passed == 0:
        day_count_string = ""
    elif days_passed == 1:
        day_count_string = " (next day)"
    else:
        day_count_string = f" ({days_passed} days later)"

    # Format time with leading zeros for minutes
    return f"{new_hours}:{new_minutes:02d} {new_meridiem}{day_string}{day_count_string}"

# Example
print(add_time('11:43 AM', '00:20'))