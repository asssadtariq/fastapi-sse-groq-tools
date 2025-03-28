"""This module contains a function that returns the address of a dealership given its ID."""


def get_dealership_address(dealership_id: str) -> str:
    dealership_addresses = {
        "1": "123 Main St, Springfield, IL",
        "2": "456 Elm St, Shelbyville, IL",
        "3": "789 Oak St, Capital City, IL",
    }

    address = dealership_addresses.get(dealership_id)

    if address:
        return address
    else:
        return "Address not found for the given dealership ID."
