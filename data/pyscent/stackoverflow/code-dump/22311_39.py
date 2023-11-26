symptoms = ['blood', 'pressure', 'high blood', 'blood pressure', 'high blood pressure']


def removeSubstring(data):
    for symptom in data[:-1]:
        if symptom in data[-1]:
            print("Removing: ", symptom)
            data.remove(symptom)
    print(data)


removeSubstring(symptoms)
