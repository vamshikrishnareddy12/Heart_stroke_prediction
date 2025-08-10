import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/heart_disease_data.csv")

df['target'].value_counts()

X = df.drop(columns=['target','num'],axis=1)
X

Y = df['target']
Y

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2, stratify = Y,random_state=42)

X.shape

X_train.shape

Y.shape

Y_train.shape

model = LogisticRegression()

model.fit(X_train, Y_train)

# accuracy score on training data

X_train_prediction = model.predict(X_train)
training_accuracy = accuracy_score(X_train_prediction, Y_train)
training_accuracy

# accuracy score on testing data

X_test_prediction = model.predict(X_test)
testing_accuracy = accuracy_score(X_test_prediction, Y_test)
print(testing_accuracy)

# Tuple of the feature data --> Which is my input
input_data = (51,1,3,125,213,0,0,125,1,1.4,2,1,2)

# Converting it into a numpy array
input_data = np.asarray(input_data) 

# Reshaping into requred input form
input_data = input_data.reshape(1,-1) 

# With the input I am predicting 
prediction = model.predict(input_data)
prediction 

if prediction[0] == 0:
    print("Good News the patient doesn't have any heart disease")
else: 
    print("The Patient should visit the doctor")

pickle.dump(model, open("model.pkl", "wb"))