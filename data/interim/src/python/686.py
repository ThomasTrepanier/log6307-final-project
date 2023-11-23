class Agent:
    def __init__(self, description, environment_graph):
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        self.description = description
        self.environment_graph = environment_graph
        self.memory_stream = []
        self.location_path = []

    def get_description(self):
        return self.description

    def get_memory_stream(self):
        return self.memory_stream

    def get_environment_graph(self):
        return self.environment_graph

    def get_location_path(self):
        return self.location_path

    def generate_action(self):
        prompt = f"You are currently at {' > '.join(self.location_path)}. Given everything you currently know, including: \n\n" 
        prompt += self.get_description() + "\n\n"
        for memory in self.memory_stream[-100:]:
            prompt += memory + "\n\n"
        for area in self.environment_graph:
            prompt += area + ":\n"
            for subarea in self.environment_graph[area]:
                prompt += "    " + subarea + "\n"
        prompt += "\nWhat would you like to do next?"
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(
            input_ids, 
            max_length=200,
            temperature=0.8,
            top_p=0.8
        )
        next_action = self.tokenizer.decode(output[0], skip_special_tokens=True)
        self.memory_stream.append(f'Action: {next_action}')  # Store the action in memory
        return next_action

    def react(self, observation):
        self.memory_stream.append(f'Observation: {observation}')  # Store the observation in memory
        prompt = self.get_description() + "\n\n"
        for memory in self.memory_stream[-100:]:
            prompt += memory + "\n\n"
        for area in self.environment_graph:
            prompt += area + ":\n"
            for subarea in self.environment_graph[area]:
                prompt += "    " + subarea + "\n"
        prompt += f"\nObservation: {observation}\n\nShould you react to this observation?" 
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(
            input_ids, 
            max_length=200,
            temperature=0.8,
            top_p=0.8
        )
        reaction = self.tokenizer.decode(output[0], skip_special_tokens=True)
        if reaction.lower().strip() == "yes":
            next_action = self.generate_action()  # Generate a new action
            return f'Reaction: {reaction}. New action: {next_action}'
        else:
            return f'Reaction: {reaction}. Continuing with previous action.'

# Usage
description = "I am a student studying sociology at Oak Hill College. I am currently writing a research paper on the effects of gentrification in low-income communities."
environment_graph = { /* ... */ }  # Same as your previous example
agent = Agent(description, environment_graph)
print(agent.generate_action())
print(agent.react('You saw a rare bird in the
