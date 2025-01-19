import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

def preprocess_and_train():
    # Load data
    data = pd.read_csv("ecommerce_data.csv")
    
    # Data preprocessing
    data["Price"] = data["Price"].str.replace(',', '').astype(float)
    data["Rating"] = data["Rating"].astype(float)
    data = data.dropna()

    X = data[["Rating"]]
    y = data["Price"]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train models
    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(X_train, y_train)
    
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    
    # Evaluate models
    rf_pred = rf_model.predict(X_test)
    lr_pred = lr_model.predict(X_test)
    print("Random Forest MSE:", mean_squared_error(y_test, rf_pred))
    print("Linear Regression MSE:", mean_squared_error(y_test, lr_pred))
    
    # Save the best model to a pickle file
    with open("model.pkl", "wb") as file:
        pickle.dump(rf_model, file)
    
    print("Model saved as model.pkl")

if __name__ == "__main__":
    preprocess_and_train()
