def sign_url():
    from google.cloud import storage
    from datetime import datetime, timedelta

    import google.auth
    credentials, project_id = google.auth.default()

    # Perform a refresh request to get the access token of the current credentials (Else, it's None)
    from google.auth.transport import requests
    r = requests.Request()
    credentials.refresh(r)

    client = storage.Client()
    bucket = client.get_bucket('EXAMPLE_BUCKET')
    blob = bucket.get_blob('libraries/image_1.png')
    expires = datetime.now() + timedelta(seconds=86400)

    # In case of user credential use, define manually the service account to use (for development purpose only)
    service_account_email = "YOUR DEV SERVICE ACCOUNT"
    # If you use a service account credential, you can use the embedded email
    if hasattr(credentials, "service_account_email"):
        service_account_email = credentials.service_account_email

    url = blob.generate_signed_url(expiration=expires,service_account_email=service_account_email, access_token=credentials.token)
    return url, 200
