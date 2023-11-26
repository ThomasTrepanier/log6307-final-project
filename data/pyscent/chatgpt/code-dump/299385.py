import hashlib

# Define constants
ID_SIZE = 16

class Record:
    def __init__(self, timestamp, id):
        self.timestamp = timestamp
        self.id = id[:ID_SIZE]

    def fingerprint(self):
        return hashlib.md5(self.id.encode()).digest()[:ID_SIZE]

class Range:
    def __init__(self, lower_bound, upper_bound, mode, payload):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.mode = mode
        self.payload = payload

    def split(self, num_splits):
        """Split the range into smaller ranges (if applicable)."""
        # This is a basic implementation that equally divides the range
        split_ranges = []
        interval = (self.upper_bound.timestamp - self.lower_bound.timestamp) // num_splits
        for i in range(num_splits):
            new_lower = self.lower_bound.timestamp + i * interval
            new_upper = new_lower + interval
            split_ranges.append(Range(new_lower, new_upper, "Fingerprint", None))
        return split_ranges

def generate_fingerprint(records):
    """Generate a fingerprint for a range of records."""
    combined = b"".join([record.fingerprint() for record in records])
    return hashlib.md5(combined).digest()[:ID_SIZE]

def reconcile(client_records, server_records):
    """Main reconciliation function."""
    # Initially, let's assume client initiates the reconciliation
    client_ranges = [Range(0, float('inf'), "Fingerprint", None)]

    # Start reconciliation loop
    for client_range in client_ranges:
        # If mode is Fingerprint, compare fingerprints
        if client_range.mode == "Fingerprint":
            client_fingerprint = generate_fingerprint(client_records)
            server_fingerprint = generate_fingerprint(server_records)
            
            if client_fingerprint != server_fingerprint:
                # Split range and continue
                client_ranges.extend(client_range.split(2))
            else:
                # No reconciliation needed for this range
                pass
        elif client_range.mode == "IdList":
            # More advanced logic for IdList and IdListResponse would go here
            pass

    # After loop, you'd have fully reconciled ranges
    # This is a very basic approach and needs more detailed logic for full functionality

# Sample records for testing
client_records = [Record(1, "abcd"), Record(2, "efgh"), Record(3, "ijkl")]
server_records = [Record(1, "abcd"), Record(2, "efgh"), Record(4, "mnop")]

# Initiate reconciliation
reconcile(client_records, server_records)
