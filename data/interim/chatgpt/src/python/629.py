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

    def invalidate_plan(self, scope):
        if scope == "whole day":
            self.daily_plan = []
        else:
            # More nuanced rule-based mechanism...
            if scope == "morning":
                self.daily_plan = [p for p in self.daily_plan if p["time"].startswith("afternoon") or p["time"].startswith("evening")]
            elif scope == "afternoon":
                self.daily_plan = [p for p in self.daily_plan if p["time"].startswith("morning") or p["time"].startswith("evening")]
            elif scope == "evening":
                self.daily_plan = [p for p in self.daily_plan if p["time"].startswith("morning") or p["time"].startswith("afternoon")]

    def check_weekly_plan(self):
        # More specific triggers...
        if self.context_info["health_status"] == "poor" or self.context_info["resources"] == "low" or self.context_info["milestones"]["milestone1"] == "incomplete":
            self.weekly_plan = []
            new_weekly_plan = self.generate_weekly_plan()
            return "Invalidated weekly plan and generated a new one: " + new_weekly_plan
        else:
            return "Weekly plan remains the same."

    def generate_weekly_plan(self):
        # Generate a new weekly plan, following a similar process to daily and weekly plan generation
        prompt = self.summary_description + " Here are your current weekly goals and progress: " + self.context_info["milestones"]["milestone1"] + ". Generate a new plan for the upcoming week."
        plan = self.generate_action(prompt)
        self.weekly_plan.append(plan)
        return plan
