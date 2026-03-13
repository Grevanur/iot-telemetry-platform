def detect_anomaly(event):

    if event["temperature"] > 90:
        return True

    if event["battery_level"] < 15:
        return True

    if event["signal_strength"] < -85:
        return True

    return False