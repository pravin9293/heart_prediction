import pickle
import numpy as np
import config

class HeartDisease():

    def __init__(self, age,sex,cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
        self.age = age
        self.sex = sex 
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal

        return

    def load_model(self):
        # load the model file
        with open(config.MODEL, 'rb') as f:
            self.model =  pickle.load(f)
            print("Model ::", self.model)

        # load normal scaler file
        with open(config.NORMAL_SCAL,'rb') as f:
            self.normal_scal = pickle.load(f)
            print("Normal Scaler ::", self. normal_scal)

    def get_heart_disease_prediction(self):
        self.load_model()

        test_array = np.array([self.age, self.sex, self.cp, self.trestbps, self.chol, self.fbs, self.restecg, 
        self.thalach, self.exang, self.oldpeak, self.slope, self.ca, self.thal], ndmin = 2)
        print("Test array : ", test_array)

        scaled_array = self.normal_scal.transform(test_array)
        # print("Scaled Array : ", scaled_array)

        pred_class = self.model.predict(scaled_array)[0]
        print("Hart Disease Predicted class is :", pred_class)


        return pred_class