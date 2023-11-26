import anvil.server
from pymongo import MongoClient
import unittest

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["line_db"]
collection = db["line_data"]

@anvil.server.callable
def store_line_data(people, time_taken):
    data = {"people": people, "time_taken": time_taken}
    collection.insert_one(data)
    return "Data stored successfully."

@anvil.server.callable
def estimate_line_time(current_people):
    all_data = list(collection.find({}))
    total_people = 0
    total_time = 0
    
    for data in all_data:
        total_people += data["people"]
        total_time += data["time_taken"]
        
    if total_people == 0:
        return "Insufficient data."
    
    avg_time_per_person = total_time / total_people
    estimated_time = avg_time_per_person * current_people
    
    return f"Estimated time: {estimated_time} minutes"

# Unit Test
class TestLineFunctions(unittest.TestCase):
    
    def test_store_line_data(self):
        result = store_line_data(10, 20)
        self.assertEqual(result, "Data stored successfully.")
        
    def test_estimate_line_time(self):
        store_line_data(10, 20)
        store_line_data(20, 40)
        result = estimate_line_time(15)
        self.assertEqual(result, "Estimated time: 30.0 minutes")

if __name__ == "__main__":
    anvil.server.connect("YOUR_ANVIL_UPLINK_KEY")
    unittest.main()
