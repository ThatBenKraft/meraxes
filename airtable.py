"""
## Airtable
Allows for the interfacing of the House of Smoothies Airtable. get_status() and
post_status() take dock name and field name to read and write from table.
"""

import requests

__author__ = "Ben Kraft"
__copyright__ = "None"
__credits__ = "Ben Kraft"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Kraft"
__email__ = "benjamin.kraft@tufts.edu"
__status__ = "Prototype"

# Defines airtable information
# cmon don't do bad stuff with this
API_KEY = "keyKf7fEzdNw4S7qi"
BASE_ID = "appdQp07FQeU5VXnL"

# Creates basic urls
BASE_URL = f"https://api.airtable.com/v0/{BASE_ID}"

# Defines headers for post authorization
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


def _get_record_data(sheet_name: str, record_name: str) -> tuple[dict, str]:
    """
    Acquires field and id from specified Airtable sheet under record.
    """
    # Gets response from URL and converts to dictionary
    get_url = BASE_URL + f"/{sheet_name}?api_key={API_KEY}"

    response: dict = requests.get(url=get_url).json()
    # Error handling
    if "error" in response:
        raise ConnectionError(f"Airtable error occured: {response['error']}")
    # For each record:
    for record in response["records"]:
        # Acquires fields and record is
        fields: dict = record["fields"]
        record_id: str = record["id"]
        # If specified record:
        if fields["Name"] == record_name:
            return fields, record_id
    # If record is not found
    raise ValueError("Record does not exist in table!")


def get_status(sheet_name: str, record_name: str, field_name: str) -> bool:
    """
    Acquires value from specified Airtable sheet under specified record and field.
    Returns boolean value.
    ### Parameters
        sheet_name: Name of sheet to pull information from
        record_name: Name of record for data to be gathered
        field_name: Name of record state
    """
    fields, _ = _get_record_data(sheet_name, record_name)
    # Only returns value if field is present
    if field_name in fields:
        return bool(fields[field_name])
    else:
        raise ValueError("Field does not exist in record!")


def post_status(
    sheet_name: str, record_name: str, field_name: str, value: bool
) -> requests.Response:
    """
    Posts value to specified sheet under record and field. Returns with path response.
    ### Parameters
        sheet_name: Name of sheet of which to post information
        record_name: Name of record for data to be gathered
        field_name: Name of record state
        value: Value to be set in field
    """
    # Acquires record ID
    _, record_id = _get_record_data(sheet_name, record_name)
    # Builds posting URL
    post_url = BASE_URL + f"/{sheet_name}/{record_id}"
    # Builds appropriate data to post
    data = {"fields": {field_name: int(value)}}
    # Posts the data
    return requests.patch(url=post_url, json=data, headers=HEADERS)


"""
================================
        HELPER FUNCTIONS
================================
"""


def get_dock(record_name: str, field_name: str) -> bool:
    """
    Posts value to dock sheet under record and field. Returns with path response.
    ### Parameters
        record_name: Name of dock for data to be gathered
        field_name: Name of dock state
    """
    return get_status("Dock States", record_name, field_name)


def post_dock(record_name: str, field_name: str, value: bool) -> requests.Response:
    """
    Posts value to doc sheet under record and field. Returns with path response.
    ### Parameters
        record_name: Name of dock for data to be gathered
        field_name: Name of dock state
        value: Value to be set in field
    """
    return post_status("Dock States", record_name, field_name, value)


def get_order(record_name: str, field_name: str) -> bool:
    """
    Posts value to order sheet under record and field. Returns with path response.
    ### Parameters
        record_name: Name of order for data to be gathered
        field_name: Name of order state
    """
    return get_status("Order Information", record_name, field_name)


def post_order(record_name: str, field_name: str, value: bool) -> requests.Response:
    """
    Posts value to order sheet under record and field. Returns with path response.
    ### Parameters
        record_name: Name of order for data to be gathered
        field_name: Name of order state
        value: Value to be set in field
    """
    return post_status("Order Information", record_name, field_name, value)


"""
==============================
        EXAMPLE SYNTAX
==============================

value = get_dock("Start Station", "Transport Present")
print(value)
post_dock("Start Station", "Transport Present", not value)

# OR...

value = get_status("Dock States", "Portioning A", "Robot Processing")
print(value)
post_status("Dock States", "Portioning A", "Robot Processing", not value)
"""
