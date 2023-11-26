import chromadb
import requests

from chromadb import Client

# Initialize ChromaDB client 
client = chromadb.Client()

# Collection to store agent objectives  
objectives_collection = client.get_or_create_collection("agent_objectives")   

# Placeholder objectives for agents
agent1_objective = "Explore the environment and learn through interaction." 
agent2_objective = "Collaborate with other agents to solve complex problems."

# Load objectives into database   
objectives_collection.add(        
    documents=[agent1_objective, agent2_objective],      
    metadatas=[{"agent_id": 1}, {"agent_id": 2}] 
)  

# Get an agent's objective by ID
def get_current_objective(agent_id):
    objective = objectives_collection.query({      
        "where": {     
        "agent_id": agent_id      
        } 
    })[0]["document"]
    return objective

# New function to update objectives using Claude API  
def update_objectives():
# Request recent events and agent summaries from environment   
    events = requests.get("http://environment_url/recent_events").json()
    summaries = requests.get("http://environment_url/agent_summaries").json()
    
# Construct prompt for Claude including recent events and summaries 
    prompt = "Recent Events: " + " ".join(events) + "\n\n"
    prompt += "Agent Summaries: \n" + "\n\n".join(summaries)
    
# Request objective updates from Claude  
    new_objectives = requests.post(
        "https://api.claude.ai/objectives", 
        json={
            "prompt": prompt,
            "number": 2  # Number of objectives per agent
        }
    ).json()
    
# Update objectives in database  
    objectives_collection.update(
        documents=new_objectives,
        metadatas=[{"agent_id": 1}, {"agent_id": 2}] 
    )
