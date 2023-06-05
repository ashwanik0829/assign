import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def process_csv_and_generate_model(csv_file_path, target_column):
    df = pd.read_csv(csv_file_path)

    # Split the data into features (X) and target (y)
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    evaluation_results = model.score(X_test, y_test)
    return model, evaluation_results
