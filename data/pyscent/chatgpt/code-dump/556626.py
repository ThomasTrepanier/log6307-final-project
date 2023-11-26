import torch 
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

class Agent:
    def __init__(self, summary_description, environment_graph):
        self.summary_description = summary_description
        self.memory_stream = []
        self.environment_graph = environment_graph
        self.location_path = []
        self.daily_plan = []  # New: plan is now scoped to a day
        self.weekly_plan = []  # New: separate plan for the week
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    # Remaining functions stay the same...
    
    def generate_daily_plan(self):
        # Adapted: function now generates daily plans
        prompt = "Given your current situation and goals, create a plan for the upcoming day: \n\n"
        # Remaining part of the function stays the same...

    def generate_weekly_plan(self):
        # New: function to generate weekly plans
        prompt = "Given your current situation and goals, create a plan for the upcoming week: \n\n"
        # Remaining part of the function stays the same...

    def react(self, observation):
        # Adapted: function now only invalidates daily plan if necessary
        prompt = self.summary_description + "\n\n"
        # Remaining part of the function stays the same...
        if reaction == "Yes":
            self.daily_plan = []  # Invalidate current daily plan
            new_plan = self.generate_daily_plan()  # Generate a new daily plan
            return "Reacted by generating a new daily plan: " + new_plan
        else:
            return "Did not react."

