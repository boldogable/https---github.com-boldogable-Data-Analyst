import pandas as pd
from sklearn.linear_model import LinearRegression

def load_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    return data

def fit_linear_regression_model(X, y):
    # Fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict(model, X):
    # Make predictions using the model
    predictions = model.predict(X)
    return predictions

def main():
    # Load the data
    data = load_data('data.csv')

    # Select independent variables and target variable
    X = data[['independent_variable1', 'independent_variable2']]
    y = data['target_variable']

    # Fit the model
    model = fit_linear_regression_model(X, y)

    # Predict
    predictions = predict(model, X)

    # Print predictions
    print(predictions)

if __name__ == '__main__':
    main()
