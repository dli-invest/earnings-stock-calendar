import os

calendarId = os.environ.get("CALENDAR_ID")
if calendarId == None:
    raise Exception("Missing CALENDAR_ID in env vars")
scopes = ["https://www.googleapis.com/auth/calendar"]
service_file_path = "stocks.json"
