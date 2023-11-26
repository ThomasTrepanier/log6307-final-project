import os
import json
from my_module import process_event  # Import your event processing logic from a separate module

def lambda_handler(event, context):
    # Parse the event data
    event_body = json.loads(event['body'])

    # Call your event processing logic
    result = process_event(event_body)

    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response

if __name__ == '__main__':
    # For local testing using python-lambda-local
    mock_event = {
        'body': '{"key": "value"}'
    }
    lambda_handler(mock_event, None)
