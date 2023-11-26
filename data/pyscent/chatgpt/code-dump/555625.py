import torch 
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

class Agent:
    def __init__(self, summary_description, environment_graph):
        self.summary_description = summary_description
        self.memory_stream = []
        self.environment_graph = environment_graph
        self.location_path = []
        self.plans = []  # New: plans are added as a class variable
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    # Remaining functions stay the same...
    
    def generate_plan(self):
        # New: function to generate long-term plans
        prompt = "Given your current situation and goals, create a plan for the upcoming week: \n\n"
        prompt += self.summary_description() + "\n\n"
        for memory in self.memory_stream[-100:]:
            prompt += memory + "\n\n"
        for area in self.environment_graph:
            prompt += area + ":\n"
            for subarea in self.environment_graph[area]:
                prompt += "    " + subarea + "\n"
        prompt += "\nWhat should you plan for the upcoming week?"
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(
            input_ids,
            max_length=200,
            temperature=0.8,
            top_p=0.8
        )
        plan = self.tokenizer.decode(output[0], skip_special_tokens=True)
        self.plans.append(plan)
        return plan

    def react(self, observation):
        # Adapted: function to generate a reaction and replan if necessary
        prompt = self.summary_description + "\n\n" 
        for memory in self.memory_stream[-100:]:
            prompt += memory + "\n\n"
        for area in self.environment_graph:
            prompt += area + ":\n"
            for subarea in self.environment_graph[area]:
                prompt += "    " + subarea + "\n"
        prompt += "\nObservation: " + observation + "\n\nShould you react to this observation?"
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(
            input_ids,
            max_length=200,
            temperature=0.8,
            top_p=0.8
        )
        reaction = self.tokenizer.decode(output[0], skip_special_tokens=True)
        if reaction == "Yes":
            self.plans = []  # Invalidate current plans
            new_plan = self.generate_plan()  # Generate a new plan
            return "Reacted by generating a new plan: " + new_plan
        else:
            return "Did not react."
