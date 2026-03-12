from datetime import datetime


def log_event(event_type, message):

    with open("logs/sales_log.txt", "a") as log_file:

        log_file.write(f"{datetime.now()} | {event_type} | {message}\n")