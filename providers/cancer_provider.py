# models

class CancerProvider():
    def __init__(self):
        self.cancers = {
            "Рак": {
                "image": "path",
                "model_path": "path",
                "model": None,
            }
        }
    
    def predict(self, type):
        pass