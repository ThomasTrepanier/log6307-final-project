from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["line_db"]
collection = db["line_data"]

def store_line_data(people, time_taken):
    data = {"people": people, "time_taken": time_taken}
    collection.insert_one(data)
    return "Data stored successfully."

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
