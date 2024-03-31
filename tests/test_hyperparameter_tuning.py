import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from titanic_survival_package.hyperparameter_tuning import tune_hyperparameters_grid


def test_tune_hyperparameters_grid():
    """
    Tests the hyperparameter tuning using grid search on RandomForestClassifier.

    This function demonstrates how to preprocess the Titanic dataset, split it into training and validation sets,
    and apply standard scaling. It then performs a grid search to find the best hyperparameters for a
    RandomForestClassifier. It asserts the types of the outputs to ensure the tuning process returns the expected
    format and values.
    """
    # Example preprocessing steps
    def preprocess_data(df):
        """
        Prepares the Titanic dataset for modeling.

        Fills missing values, encodes categorical variables, and drops unnecessary columns.
        """
        df['Age'].fillna(df['Age'].median(), inplace=True)
        df['Embarked'].fillna('S', inplace=True)  # Assuming 'S' is the most common embarkation port
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
        df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
        df.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
        return df

    # Load and preprocess the dataset
    train_df = pd.read_csv('train.csv')  # Update the path as needed
    train_df = preprocess_data(train_df)

    # Define features and target
    features = train_df.drop(['Survived'], axis=1)
    target = train_df['Survived']

    # Splitting dataset into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(features, target, test_size=0.2, random_state=42)

    # Scaling the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    # Define parameter grid for tuning
    param_grid = {'n_estimators': [10, 20], 'max_depth': [3, 4]}

    # Perform hyperparameter tuning
    best_params, best_score = tune_hyperparameters_grid(RandomForestClassifier(random_state=42), X_train_scaled, y_train, param_grid)

    # Assert the types of tuning results
    assert isinstance(best_params, dict), "Tuning did not return a dictionary of best parameters."
    assert isinstance(best_score, float), "Tuning did not return a best score as float."
    print("Hyperparameter tuning test passed.")
