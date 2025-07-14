import requests

def general_settings(campaign_id, follow_up_percentage):

    url = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/settings?api_key=e920f24b-340f-4ac3-8b69-7e25fd64b40c_f0kdipx"

    payload = {
        "track_settings": ["DONT_TRACK_LINK_CLICK"],
        "stop_lead_settings": "REPLY_TO_AN_EMAIL",
        "send_as_plain_text": False,
        "follow_up_percentage": follow_up_percentage,
        "enable_ai_esp_matching": False,
        "out_of_office_detection_settings": {
            "ignoreOOOasReply": True,
            "autoReactivateOOO": False,
            "reactivateOOOwithDelay": "7",
            "autoCategorizeOOO": True
        },
        "force_plain_text": False,
        "auto_pause_domain_leads_on_reply": True,
        "ignore_ss_mailbox_sending_limit": True,
        "bounce_autopause_threshold": "4",
        "ai_categorisation_options": [1, 2, 4, 5, 6]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.text ==  '{"ok":true}':
        print(f"\nSuccessfully Updated Campaign: {campaign_id}")

    else:
        print(response.text)
