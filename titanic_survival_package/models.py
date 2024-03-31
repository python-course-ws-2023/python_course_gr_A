from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler
from .data_preprocessing import preprocess_data, load_dataset, fill_missing_values
from .feature_engineering import create_family_size_feature, drop_unnecessary_features, extract_and_process_titles, add_interaction_terms
from sklearn.pipeline import Pipeline
import pandas as pd

class ModelTrainer:
    """
    A class dedicated to training machine learning models using GridSearchCV for hyperparameter optimization.

    Attributes:
    - model (estimator): The machine learning estimator to be trained.
    - param_grid (dict): A dictionary specifying the parameter grid for hyperparameter tuning.
    - best_model (estimator, optional): Stores the best estimator after training.
    """
    def __init__(self, model, param_grid):
        
        self.model = model
        self.param_grid = param_grid
        self.best_model = None

    def train(self, X, y):
        """
        Trains the model using GridSearchCV with the provided parameters.

        Parameters:
        - X (array-like): Feature data used for training.
        - y (array-like): Target values.

        Returns:
        - The best estimator after performing grid search.
        """
        grid_search = GridSearchCV(self.model, self.param_grid, cv=5, scoring='accuracy')
        grid_search.fit(X, y)
        self.best_model = grid_search.best_estimator_
        return self.best_model

    def evaluate(self, X_test, y_test):
        """
        Evaluates the trained model on a test dataset.

        Parameters:
        - X_test (array-like): Feature data for testing.
        - y_test (array-like): Actual target values for the test data.

        Returns:
        - Accuracy score of the model on the test data.
        """
        predictions = self.best_model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy

class ModelEvaluator:
    """
    Provides a static method for evaluating machine learning models.
    """
    @staticmethod
    def evaluate_model(model, X_test, y_test):
        """
        Static method to evaluate the accuracy of a model on a test set.

        Parameters:
        - model (estimator): The trained machine learning model.
        - X_test (array-like): Test data features.
        - y_test (array-like): True labels for the test data.

        Returns:
        - Accuracy score of the model on the test data.
        """
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy

def train_stacking_model(X_train, y_train):
    """
    Trains a stacking ensemble model using pre-defined base learners and a final estimator.

    Parameters:
    - X_train (array-like): Training data features.
    - y_train (array-like): Training data labels.

    Returns:
    - The trained stacking model.
    """
    base_models = [
        ('random_forest', RandomForestClassifier(n_estimators=250, min_samples_split=2, min_samples_leaf=4, max_depth=5, random_state=42)),
        ('gradient_boosting', GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42))
    ]

    final_estimator = LogisticRegression(C=1.0, max_iter=200, solver='liblinear', random_state=42)
    stacking_model = StackingClassifier(estimators=base_models, final_estimator=final_estimator, cv=5, n_jobs=-1, passthrough=True)
    stacking_model.fit(X_train, y_train)
    return stacking_model


# Function to generate submission file
def generate_submission(test_data_path, submission_file_path):
    
    # Prepare and save submission DataFrame
    test_data_path.to_csv(submission_file_path, index=False)
    print(f"Submission file saved to {submission_file_path}")
    