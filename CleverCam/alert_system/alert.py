from twilio.rest import Client

class AlertSystem:
    def __init__(self, account_sid, auth_token, twilio_number, receiver_whatsapp_number):
        # Twilio API client setup
        self.client = Client(account_sid, auth_token)
        self.twilio_number = f'whatsapp:{twilio_number}'  # Twilio sandbox WhatsApp number
        self.receiver_whatsapp_number = f'whatsapp:{receiver_whatsapp_number}'  # Recipient's WhatsApp number

    def send_alert(self, subject, message):
        # Combine subject and message into a single alert message
        alert_message = f"*{subject}*\n{message}"

        # Send the WhatsApp message
        try:
            message = self.client.messages.create(
                body=alert_message,
                from_=self.twilio_number,
                to=self.receiver_whatsapp_number
            )
            print(f"WhatsApp alert sent: {subject}")
        except Exception as e:
            print(f"Failed to send WhatsApp alert: {e}")
