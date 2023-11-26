from fastapi import FastAPI, Request, HTTPException, Depends
import time

# Initialize FastAPI app
app = FastAPI()

# In-memory storage for request counters
request_counters = {}

# Custom RateLimiter class with dynamic rate limiting values per route
class RateLimiter:
    def __init__(self, requests_limit: int, time_window: int):
        self.requests_limit = requests_limit
        self.time_window = time_window

    async def __call__(self, request: Request):
        client_ip = request.client.host
        route_path = request.url.path

        # Get the current timestamp
        current_time = int(time.time())

        # Create a unique key based on client IP and route path
        key = f"{client_ip}:{route_path}"

        # Check if client's request counter exists
        if key not in request_counters:
            request_counters[key] = {"timestamp": current_time, "count": 1}
        else:
            # Check if the time window has elapsed, reset the counter if needed
            if current_time - request_counters[key]["timestamp"] > self.time_window:
                # Reset the counter and update the timestamp
                request_counters[key]["timestamp"] = current_time
                request_counters[key]["count"] = 1
            else:
                # Check if the client has exceeded the request limit
                if request_counters[key]["count"] >= self.requests_limit:
                    raise HTTPException(status_code=429, detail="Too Many Requests")
                else:
                    request_counters[key]["count"] += 1

        # Clean up expired client data (optional)
        for k in list(request_counters.keys()):
            if current_time - request_counters[k]["timestamp"] > self.time_window:
                request_counters.pop(k)

        return True

# Include the custom RateLimiter dependency on specific routes
@app.get("/limited", dependencies=[Depends(RateLimiter(requests_limit=10, time_window=60))])
async def limited_endpoint():
    return {"message": "This endpoint has rate limiting (10 requests per 60 seconds)."}

@app.get("/limited/other", dependencies=[Depends(RateLimiter(requests_limit=5, time_window=60))])
async def limited_other_endpoint():
    return {"message": "This endpoint has rate limiting (5 requests per 60 seconds)."}

@app.get("/unlimited")
async def unlimited_endpoint():
    return {"message": "This endpoint has no rate limiting."}
