from itertools import islice

def create(ids):
    policy = {
        'Statement': []
    }
    i = iter(ids)
    while True:
        chunk = list(islice(i, 200))
        if not chunk:
            break
        policy['Statement'].append({
            'Principal': {
                'AWS': list(map(lambda id: f"arn:aws:iam::{id}:root", chunk))
            }
        })
    return policy
