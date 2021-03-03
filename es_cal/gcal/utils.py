### Extract json file from variable
import base64
import os
import pickle
from urllib.request import urlopen


def decode_json(filepath="stocks.json"):
    """
    Description: Generates a pathname to the service account json file
      needed to access the google calendar
    """
    # Check for stocks file
    if os.path.exists(filepath):
        return filepath
    creds = os.environ.get("GOOGLE_SERVICE_CREDS")
    if creds is None:
        print("CREDENTIALS NOT AVAILABLE")
        exit(1)
    # get base64 string
    message_bytes = base64.b64decode(creds)
    decoded_string = message_bytes.decode("ascii")
    # Output to decoded string to json file
    with open(filepath, "w") as service_file:
        service_file.write(decoded_string)
    return filepath


def get_tickers():
    url = "https://github.com/FriendlyUser/cad_tickers_list/blob/main/static/latest/tickers?raw=true"
    data = pickle.load(urlopen(url))
    # split ending from string
    data = [ticker.split(".")[0] for ticker in data]
    return data


def split_string(string: str):
    if " " not in string:
        return string
    string_list = string.split()
    return string_list[1]