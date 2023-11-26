from .database import objects_collection, agents_collection, events_collection

@socketio.on('update object')
def handle_object_update(data):
    ...

@socketio.on('delete object') 
def handle_object_delete(data):
    ...

@socketio.on('create event')  
def handle_event_creation(data):
    ...
