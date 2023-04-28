"""
## Airtable
Allows for the interfacing of the House of Smoothies Airtable. get_status() and
post_status() take dock name and field name to read and write from table.
"""

from typing import Any

import requests

API_KEY = "keyKf7fEzdNw4S7qi"
BASE_ID = "appdQp07FQeU5VXnL"
SHEET_NAME = "Dock States"

# Defines headers for post authorization
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# Creates basic urls
BASE_URL = f"https://api.airtable.com/v0/{BASE_ID}/{SHEET_NAME}"
GET_URL = BASE_URL + f"?api_key={API_KEY}"


def main():
    # Specifies dock name, then field name
    print(get_status("Portioning A", "Robot Processing"))

    post_status("Portioning A", "Robot Processing", True)


def _get_record_data(record_name: str) -> tuple[dict, str]:
    """
    Acquires field and id from specified record.
    """
    # Gets response from URL and converts to dictionary
    response = requests.get(url=GET_URL).json()
    # Error handling
    if "error" in response:
        raise ConnectionError(f"Airtable error occured: {response['error']}")
    # For each record:
    for record in response["records"]:
        # Acquires fields and record is
        fields = record["fields"]
        record_id = record["id"]
        # If specified record:
        if fields["Name"] == record_name:
            return fields, record_id
        else:
            raise ValueError("Record does not exist in table!")
    # Returns if no records exist
    print("WARNING: No records exist in table!")
    return {}, ""


def get_status(record_name: str, field_name: str) -> bool:
    """
    Acquires value from Airtable from field under record. Returns boolean value.

    ### Parameters
        record_name: Name of dock for data to be gathered
        field_name: Name of dock state
    """
    fields, _ = _get_record_data(record_name)
    # Only returns value if field is present
    if field_name in fields:
        return bool(fields[field_name])
    else:
        raise ValueError("Field does not exist in record!")


def post_status(record_name: str, field_name: str, value: bool) -> requests.Response:
    """
    Posts value to field under record. Returns with path response.

    ### Parameters
        record_name: Name of dock for data to be gathered
        field_name: Name of dock state
        value: Value to be set in field
    """
    # Acquires record ID
    _, record_id = _get_record_data(record_name)
    # Builds posting URL
    post_url = BASE_URL + f"/{record_id}"
    # Builds appropriate data to post
    data = {"fields": {field_name: int(value)}}
    # Posts the data
    return requests.patch(url=post_url, json=data, headers=HEADERS)


# Runs main code if file is run from console but NOT if included as library.
if __name__ == "__main__":
    main()