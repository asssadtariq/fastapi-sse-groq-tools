"""This is a tool to check the availability of appointments of a dealership on a given date."""

from datetime import datetime, timedelta


def check_appointment_availability(dealership_id: str, date: str):
    """
    Args:
        dealership_id (str): The ID of the dealership.
        date (str): The date in YYYY-MM-DD format.
    """

    assert dealership_id, "Dealership ID is required."
    assert date, "Date is required."

    if date and date.lower() == "today":
        date = str(datetime.now().strftime("%Y-%m-%d"))

    try:
        appointment_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    dealership_availability = {
        "1": ["09:00", "09:30", "10:00", "11:00", "14:00", "15:30"],
        "2": ["10:00", "11:30", "13:00", "16:00"],
        "3": ["10:00", "12:30", "13:00", "18:00"],
    }

    if dealership_id not in dealership_availability:
        return f"Dealership ID {dealership_id} not found."

    available_slots = dealership_availability[dealership_id]

    start_time = datetime.combine(appointment_date, datetime.min.time()).replace(hour=9)
    end_time = datetime.combine(appointment_date, datetime.min.time()).replace(hour=17)
    time_slots = []

    current_time = start_time
    while current_time < end_time:
        slot = current_time.strftime("%H:%M")
        if slot in available_slots:
            time_slots.append(slot)
        current_time += timedelta(minutes=30)

    return (
        ",".join(time_slots) if time_slots else "No available slots for the given date."
    )
