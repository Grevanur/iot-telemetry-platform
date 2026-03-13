from kafka_alert_consumer import messages
from alert_rules import check_alert
from kafka_producer import send_alert


def run():

    for event in messages():

        alert = check_alert(event)

        if alert:

            alert_event = {
                "device_id": event["device_id"],
                "type": alert,
                "timestamp": event["timestamp"]
            }

            send_alert(alert_event)

            print("Alert generated", alert_event)


if __name__ == "__main__":
    run()