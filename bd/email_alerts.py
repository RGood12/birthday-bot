import requests
from bd.secrets import API_KEY

def send_alert(subject, body):
    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": "Birthday Bot <onboarding@resend.dev>",
            "to": ["r.goodson12@gmail.com"],
            "subject": subject,
            "text": body,
        },
        timeout=10,
    )

    response.raise_for_status()

