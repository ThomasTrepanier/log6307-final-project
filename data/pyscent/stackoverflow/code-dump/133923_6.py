from datetime import datetime

def parse_timestamp(datestring, formats):
    results = {'datestring': datestring, 'matches': []}
    for f in formats:
        try:
            d = datetime.strptime(datestring, f)
        except:
            continue
        results['matches'].append({'datetime': d, 'format': f})
    return results
