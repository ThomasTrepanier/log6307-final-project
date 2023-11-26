def orchestrator_function(context: df.DurableOrchestrationContext):
    input_context = context.get_input()
    img_url = input_context.get('img_url')

    some_response= yield context.call_activity('MyActivity', img_url)
    
    return [some_response]
