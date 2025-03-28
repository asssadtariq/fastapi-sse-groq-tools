"""This file has a tool function to schedule an appointment."""


def schedule_appointment(
    user_id: str, dealership_id: str, date: str, time: str, car_model: str
) -> str:
    """
    Args:
        user_id (str): The ID of the user.
        dealership_id (str): The ID of the dealership.
        date (str): The date in YYYY-MM-DD format.
        time (str): The time in HH:MM format.
        car_model (str): The model of the car.
    """

    assert user_id, "User ID is required."
    assert dealership_id, "Dealership ID is required."
    assert date, "Date is required."
    assert time, "Time is required."
    assert car_model, "Car model is required."

    # return schedule the appointment
    return f"Appointment scheduled for {date} at {time} for user {user_id}, dealership id {dealership_id}, and model {car_model}."
