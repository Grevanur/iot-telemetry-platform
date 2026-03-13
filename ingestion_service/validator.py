def validate_event(event):

    required = [
        "device_id",
        "timestamp",
        "temperature",
        "battery_level",
        "signal_strength"
    ]

    for field in required:
        if field not in event:
            return False

    return True