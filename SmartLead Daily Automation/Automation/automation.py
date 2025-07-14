import datetime
from configs import campaign_schedules
from schedule_time import schedule_update


def run_daily_updates():
    today = datetime.datetime.today().weekday()

    for campaign_id, schedule_by_day in campaign_schedules.items():
        if today in schedule_by_day:
            schedule = schedule_by_day[today]
            schedule_update(
                campaign_id=campaign_id,
                timezone=schedule['timezone'],
                days_of_the_week=schedule['days_of_the_week'],
                start_hour=schedule['start_hour'],
                end_hour=schedule['end_hour'],
                min_time_btw_emails=schedule['min_time_btw_emails'],
                max_new_leads_per_day=schedule['max_new_leads_per_day']
            )


if __name__ == "__main__":
    run_daily_updates()
