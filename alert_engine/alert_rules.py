def check_alert(event):

    if event["temperature"] > 95:
        return "HIGH_TEMP"

    if event["battery_level"] < 10:
        return "LOW_BATTERY"

    return None