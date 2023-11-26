class TwentyNewsgroupsDataset(Dataset):
    def __init__(self, texts, targets, vectorizer):
        self.texts = texts
        self.targets = targets
        self.vectorizer = vectorizer
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.targets[idx]
        bow_vector = torch.tensor(self.vectorizer.transform([text]).toarray())
        return bow_vector, label

# Then, when creating your datasets:
vectorizer = CountVectorizer().fit(train_texts)
train_dataset = TwentyNewsgroupsDataset(train_texts, train_labels, vectorizer)
test_dataset = TwentyNewsgroupsDataset(test_texts, test_labels, vectorizer)
