import os
import time
import requests
from dotenv import load_dotenv
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

load_dotenv()

API_KEY = os.getenv("SMARTLEAD_API_KEY")


def create_session_with_retries():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["POST"],
        raise_on_status=False
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


session = create_session_with_retries()


def schedule_update(campaign_id, timezone, days_of_the_week, start_hour, end_hour, min_time_btw_emails,
                    max_new_leads_per_day):
    url_schedule = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/schedule?api_key={API_KEY}"
    url_status = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/status?api_key={API_KEY}"

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    payload_schedule = {
        "timezone": timezone,
        "days_of_the_week": days_of_the_week,
        "start_hour": start_hour,
        "end_hour": end_hour,
        "min_time_btw_emails": min_time_btw_emails,
        "max_new_leads_per_day": max_new_leads_per_day,
    }

    try:
        response = session.post(url_schedule, json=payload_schedule, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Failed to update schedule: {e}")
        return

    if not data.get("ok"):
        print("Failed to update schedule: API responded with an error")
        return

    try:
        response = session.post(url_status, json={"status": "PAUSED"}, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error pausing campaign: {e}")
        return

    if not data.get("ok"):
        print("Failed to pause the campaign")
        return

    time.sleep(10)
    print("Campaign paused successfully")

    try:
        response = session.post(url_status, json={"status": "START"}, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error starting campaign: {e}")
        return

    if not data.get("ok"):
        print("Failed to start the campaign")
        return

    time.sleep(10)
    print("Campaign rescheduled successfully")
    print("\nAll changes saved!\n\nbr,\nNightmare")
