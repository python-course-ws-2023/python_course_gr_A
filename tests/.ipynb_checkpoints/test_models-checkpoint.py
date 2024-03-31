from titanic_survival_package.models import ModelTrainer, ModelEvaluator
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import numpy as np


def test_model_training_and_evaluation():
    """
    Tests the training and evaluation of RandomForestClassifier using the ModelTrainer and ModelEvaluator classes.

    This function demonstrates the process of initializing a model trainer with predefined hyperparameters,
    training the model on a subset of the data for efficiency, and evaluating its performance on a separate validation set.
    The function asserts the accuracy type to ensure the evaluation returns a floating-point number, indicative of the model's performance.
    """
    # Dataset creation for testing purposes
    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Define best hyperparameters obtained from previous tuning efforts
    best_params = {
        'n_estimators': [100],  # Example: Number of trees in the forest
        'max_depth': [None],  # Example: Maximum depth of the trees
        'min_samples_split': [2],  # Example: Minimum number of samples required to split an internal node
        'min_samples_leaf': [1]  # Example: Minimum number of samples required to be at a leaf node
    }

    # Initialize the ModelTrainer with a RandomForestClassifier and the best hyperparameters
    model_trainer = ModelTrainer(RandomForestClassifier(random_state=42), best_params)

    # Load training and validation sets here (not shown for brevity)
    # For example purposes, using X_train, y_train, X_val, y_val

    # Train the RandomForestClassifier model on a subset of the training data for quick testing
    trained_model = model_trainer.train(X_train[:100], y_train[:100])

    # Evaluate the trained model on a subset of the validation data
    accuracy = ModelEvaluator.evaluate_model(trained_model, X_val[:20], y_val[:20])

    # Assert the type of the accuracy to ensure the evaluation process returns a floating-point number
    assert isinstance(accuracy, np.float64) or isinstance(accuracy, float), "Model evaluation did not return accuracy as a floating-point number."

    print("Model training and evaluation test passed.")
