from mangum import Mangum

def handler(event, context):
    # Your application code here
    return Mangum(app)  # Assuming your app is a FastAPI/ASGI app
