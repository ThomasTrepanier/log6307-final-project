class Agent:
    def __init__(self, agent_id, summary_description, environment_url):
        self.agent_id = agent_id
        self.summary_description = summary_description
        self.environment_url = environment_url
        self.logger = logging.getLogger(__name__)
        
     # Connect to ChromaDB
    self.client = chromadb.Client()  
    
    # Create a collection for this agent's memory
    self.memory = self.client.get_or_create_collection(f"agent_{self.agent_id}")  
    
    # Create index on memory collection
    if self.memory.count() > 0:
        self.memory.create_index()
        
    def generate_action(self):
        # Call new update_objectives() function 
        update_objectives()
        
        # Get updated objective and proceed as before...
        objective = get_current_objective(self.agent_id) 
        room_objects = requests.get(f"{self.environment_url}/room_objects").json()
        previous_action = get_previous_action()
        event = get_current_event() or "none"
        
        # Generate next action based on summary and memories
        action = generate_action(self.summary_description, relevant_memories, self.environment_url)
        self.logger.info(f"Action: {action}")
        return action 
