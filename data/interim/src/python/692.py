import torch 
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

class Agent:
    def __init__(self, summary_description, environment_graph):
        self.summary_description = summary_description
        self.memory_stream = []
        self.environment_graph = environment_graph
        self.location_path = []
        self.daily_plan = []  
        self.weekly_plan = []  
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        self.context_info = {
            "health_status": "good", 
            "resources": "sufficient",
            "milestones": {"milestone1": "incomplete", "milestone2": "complete"}  # Example context information
        }

    # All the remaining methods...

    def generate_weekly_plan(self):
        # Generate a new weekly plan, following a similar process to daily and weekly plan generation
        # Include more context in the prompt
        prompt = (self.summary_description + " Your health status is: " + self.context_info["health_status"] + 
                  ". Your resources status is: " + self.context_info["resources"] +
                  ". Here are your current weekly goals and progress: " + self.context_info["milestones"]["milestone1"] + 
                  ". Generate a new plan for the upcoming week.")
        plan = self.generate_action(prompt)
        self.weekly_plan.append(plan)
        return plan
