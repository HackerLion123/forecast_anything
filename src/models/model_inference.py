from src.helper.metrics import rmsle, wape, rmsse



class ModelInference:
    def __init__(self, model):
        self.model = model

    def predict(self, input_data):
        # Perform inference using the model
        predictions = self.model(input_data)
        return predictions
    
    def _model_baseline(self, actuals, forecasts):
        # Calculate baseline metrics for model evaluation
        metrics = 
        return metrics