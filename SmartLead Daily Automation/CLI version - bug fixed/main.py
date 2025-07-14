import pyfiglet
import colorama
import time
from termcolor import colored

from update_general_settings import general_settings
from update_schedule_time import schedule_time
from fetch_analytics_by_date_range import analytics_by_date_range
from Campaign_sequence_analytics import sequence_analytics

colorama.init()

def show_menu():
    banner = pyfiglet.figlet_format("Smart Lead API")
    print("=" * 80)
    print(colored(banner, "cyan"))
    print("by Nightmare")
    print("=" * 80)

    print("\nWelcome to the Smart Lead API CLI!")
    print("Initializing...\n")
    time.sleep(2)
    print("Please select the option you'd like to perform:\n")
    print("01. Update Campaign General Settings")
    print("02. Update Campaign Schedule Time")
    print("03. Fetch Analytics by Date Range")
    print("04. Get Campaign Sequence Analytics")
    print("05. Exit\n")

def get_user_choice():
    valid_options = {'1', '2', '3', '4', 'menu', '5'}
    while True:
        choice = input("Enter option number (01–05): ").strip()
        if choice in valid_options:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4")

def get_days_of_week_input():
    day_map = {
        "mon": 1,
        "tue": 2,
        "wed": 3,
        "thu": 4,
        "fri": 5,
        "sat": 6,
        "sun": 0
    }

    user_input = input("Enter days of the week (e.g., Mon,Tue,Wed): ")
    days = user_input.strip().lower().split(',')

    try:
        selected_days = [day_map[day.strip()] for day in days if day.strip() in day_map]
        if not selected_days:
            raise ValueError
        return selected_days
    except Exception:
        print("Invalid input. Please use abbreviations like Mon,Tue,...")
        return get_days_of_week_input()

def main_cli():
    show_menu()
    choice = get_user_choice()

    while True:
        if choice == '1':
            campaign_id = str(input("Enter Campaign ID: "))
            sending_priority = int(input("Enter follow up percentage: "))
            option1_results = general_settings.general_settings(campaign_id, sending_priority)
            return option1_results

        elif choice == '2':
            # timezone, days_of_the_week, start_hour, end_hour, min_time_btw_emails, max_new_leads_per_day
            campaign_id = str(input("Enter Campaign ID: "))
            timezone = str(input("Enter timezone: "))
            days_of_the_week = get_days_of_week_input()
            start_hour = str(input("Enter start time(HH:MM): "))
            end_hour = str(input("Enter end hour(HH:MM): "))
            min_time_btw_emails = int(input("Enter emails time gap: "))
            max_new_leads_per_day = int(input("Enter max new leads per day: "))

            option2_results = schedule_time.schedule_update(campaign_id, timezone,
                                                            days_of_the_week, start_hour, end_hour, min_time_btw_emails, max_new_leads_per_day)
            return option2_results

        elif choice == '5':
            exit(0)

        else:
            print("Invalid input. Try again")


if __name__ == "__main__":
    main_cli()
