import hmac
import time
from hashlib import sha256

import requests
import stripe

webhook_url = 'https://your-site/api/stripe/webhook/'
stripe_secret = 'YOUR_STRIPE_WEBHOOK_SIGN_SECRET'  # whsec_..
webhook_json_file = 'PATH_TO_JSON_FILE_WITH_WH_DATA/webhook_example.json'


def generate_stripe_signature_header(payload: str):
    timestamp_utc = int(time.time())
    signed_payload = "%d.%s" % (timestamp_utc, payload)
    v1_sig = compute_signature(signed_payload, secret=stripe_secret)
    return f't={timestamp_utc},v1={v1_sig}'


def compute_signature(payload: str, secret):
    """Take from stripe"""
    mac = hmac.new(
        secret.encode("utf-8"),
        msg=payload.encode("utf-8"),
        digestmod=sha256,
    )
    return mac.hexdigest()


with open(webhook_json_file, 'r') as f:
    payload = f.read()

signature = generate_stripe_signature_header(payload=payload)

headers = {
    'STRIPE-SIGNATURE': signature,  
    'Content-Type': 'application/json',
}

session = requests.Session()
session.headers.update(**headers)
response = session.post(webhook_url, data=payload)

print(response.content)
print(response.status_code)
response.raise_for_status()
