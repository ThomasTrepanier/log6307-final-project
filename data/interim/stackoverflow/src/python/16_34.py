async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)

    req_data = req.get_json()
    img_url = req_data['img_url']
    payload = {"img_url": img_url}
    
    instance_id = await client.start_new(req.route_params["functionName"], None, payload)

    logging.info(f"Started orchestration with ID = '{instance_id}'.")

    return client.create_check_status_response(req, instance_id)
