from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import numpy as np

def tune_hyperparameters_grid(model, X, y, parameters):
    """
    Performs hyperparameter tuning using Grid Search Cross Validation. This method exhaustively 
    searches through all specified parameter combinations in 'parameters'.

    Parameters:
    - model (estimator): The machine learning model/estimator for which hyperparameters are to be optimized.
    - X (array-like): Feature dataset used for training the model.
    - y (array-like): Target values corresponding to 'X'.
    - parameters (dict): Dictionary with parameters names (str) as keys and lists of parameter settings to try as values.

    Returns:
    - dict: The best parameter setting found on the given data.
    - float: Mean cross-validated score of the best_estimator.
    """
    grid_search = GridSearchCV(model, parameters, cv=5, scoring='accuracy', error_score='raise')
    grid_search.fit(X, y)
    return grid_search.best_params_, grid_search.best_score_

def tune_hyperparameters_random(model, X, y, parameters, n_iter=10):
    """
    Performs hyperparameter tuning using Randomized Search Cross Validation. This method samples 
    'n_iter' parameter settings from the specified 'parameters' distributions.

    Parameters:
    - model (estimator): The machine learning model/estimator for which hyperparameters are to be optimized.
    - X (array-like): Feature dataset used for training the model.
    - y (array-like): Target values corresponding to 'X'.
    - parameters (dict): Dictionary where keys are parameter names and values are distributions or lists of parameters to sample.
    - n_iter (int, optional): Number of parameter settings that are sampled. n_iter trades off runtime vs quality of the solution.

    Returns:
    - dict: The best parameter setting found on the given data.
    - float: Mean cross-validated score of the best_estimator.
    """
    random_search = RandomizedSearchCV(model, parameters, n_iter=n_iter, cv=5, scoring='accuracy', random_state=42, error_score='raise')
    random_search.fit(X, y)
    return random_search.best_params_, random_search.best_score_
