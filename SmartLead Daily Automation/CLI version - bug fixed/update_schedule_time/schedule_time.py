import requests
import time


def schedule_update(campaign_id, timezone, days_of_the_week,start_hour, end_hour,min_time_btw_emails, max_new_leads_per_day):

    url = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/schedule?api_key=e920f24b-340f-4ac3-8b69-7e25fd64b40c_f0kdipx"

    payload = {
        "timezone": timezone,
        "days_of_the_week": days_of_the_week,
        "start_hour": start_hour,
        "end_hour": end_hour,
        "min_time_btw_emails": min_time_btw_emails,
        "max_new_leads_per_day": max_new_leads_per_day,
        # "schedule_start_time": "2025-05-19T08:29:25.978Z"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    api_response_1 = requests.post(url, json=payload, headers=headers)
    time.sleep(1)

    if api_response_1.text ==  '{"ok":true}':
        print(f"\nSuccessfully Updated Schedule Time on Campaign: {campaign_id}")
        url = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/status?api_key=e920f24b-340f-4ac3-8b69-7e25fd64b40c_f0kdipx"

        payload = {"status": "PAUSED"}
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        api_response_2 = requests.post(url, json=payload, headers=headers)
        time.sleep(1)

        if api_response_2.text == '{"ok":true}':
            url = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/status?api_key=e920f24b-340f-4ac3-8b69-7e25fd64b40c_f0kdipx"

            payload = {"status": "START"}
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            api_response_3 = requests.post(url, json=payload, headers=headers)
            time.sleep(1)
            if api_response_3.text == '{"ok":true}':
                print("All Changes Saved!")
            else:
                print("Something wrong when starting the campaign")
    else:
        print(api_response_1.text)

