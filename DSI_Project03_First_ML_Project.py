#Import needed packages
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

#Import the input data set
data_set = pd.read_csv("video_game_data.csv")

#Split data into input and output objects
X = data_set.drop({"completion_time"}, axis = 1) #Removing the column 'completion_time' and so used drop() and axis as 1
y = data_set["completion_time"]

#Split data into test and train sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) #splitting the data into 20% in test set and remaining in train set hence used test_size = 0.2. Random_state = 42 means if somebody else too use the same value, the prediction result should be the same for both

#Instantiate RandomForesr Model object
regressor = RandomForestRegressor(random_state = 42)

#Train the model
regressor.fit(X_train,y_train)

#Predict the model
y_pred = regressor.predict(X_test)

#Creating a dataframe
df = pd.DataFrame({"Actual" : y_test,
                   "Predicted" : y_pred})

#Calculating Accuracy
r2_score(y_test, y_pred)
