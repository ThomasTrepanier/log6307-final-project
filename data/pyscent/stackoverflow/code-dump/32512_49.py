class MyModelPredict(object):
    def __init__(self, model):
        self._estimator_type = 'classifier'
        
    def predict(self, X):
        return your_custom_prediction

model = MyModelPredict()
plot_confusion_matrix(model, X, y_true)
