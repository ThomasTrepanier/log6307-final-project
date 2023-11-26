class ModelNames(str, Enum):
    gpt2 = 'gpt2'
    distilgpt2 = 'distilgpt2'
    gpt2_xl = 'gpt2-XL'
    gpt2_large = 'gpt2-large'

print(ModelNames.gpt2) # 'ModelNames.gpt2'
print(ModelNames.gpt2 is str) # False
print(ModelNames.gpt2_xl.name) # 'gpt2_xl'
print(ModelNames.gpt2_xl.value) # 'gpt2-XL'
