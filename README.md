# meraxes 🍹

The Tufts ME35 Final Project, which was to create a Smoothie Bar, needed a banana-chopping robot. That's where Meraxes comes in. Also includes re-developed Airtable API implementation.

## ☁️ Airtable Usage

The status of docks can be easily acquired with `get_status()` and . It takes a sheet name, a record name, and field name to narrow down the table search:

```python
def get_status(
    sheet_name: str, record_name: str, field_name: str,
) -> bool:
```

`post_status()` can posts a value to a specified sheet under a record and field and returns a request response:

```python
def post_status(
    sheet_name: str, record_name: str, field_name: str, value: bool
) -> requests.Response:
```

Both functions will raise an error if no such field or record exists.

## 🩹 Helper functions

Other helper functions are included for specific sheets; `set_dock()` and `post_dock()` operate specifically for the *Dock States* sheet.
