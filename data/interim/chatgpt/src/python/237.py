import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Initialize the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Load a model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# You will need to have your training and evaluation datasets ready.
# Let's assume you have two text files: `train.txt` and `eval.txt`.
# Each line of these files is a separate example.

def load_dataset(train_path, test_path, tokenizer):
    train_dataset = TextDataset(
          tokenizer=tokenizer,
          file_path=train_path,
          block_size=128)
     
    test_dataset = TextDataset(
          tokenizer=tokenizer,
          file_path=test_path,
          block_size=128) 

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )
    return train_dataset, test_dataset, data_collator

train_dataset, test_dataset, data_collator = load_dataset('train.txt', 'eval.txt', tokenizer)

# Define the training arguments
training_args = TrainingArguments(
    output_dir='./results',          # output directory
    overwrite_output_dir=True,      # overwrite the content of the output directory
    num_train_epochs=3,              # number of training epochs
    per_device_train_batch_size=32,  # batch size for training
    per_device_eval_batch_size=64,   # batch size for evaluation
    eval_steps = 400,                # Number of update steps between two evaluations.
    save_steps=800,                  # after # steps model is saved 
    warmup_steps=500,                # number of warmup steps for learning rate scheduler
    )

# Create a Trainer instance
trainer = Trainer(
    model=model,                         # the instantiated Transformers model to be trained
    args=training_args,                  # training arguments, defined above
    train_dataset=train_dataset,         # training dataset
    eval_dataset=test_dataset,           # evaluation dataset
    data_collator=data_collator,
    prediction_loss_only=True,
)

# Train the model
trainer.train()

# Save the model
trainer.save_model()
