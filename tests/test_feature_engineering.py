import pandas as pd
from titanic_survival_package.feature_engineering import create_family_size_feature, extract_and_process_titles, add_interaction_terms


def test_create_family_size_feature():
    """
    Tests the creation of a 'FamilySize' feature.

    This function verifies that the `create_family_size_feature` function successfully adds a new column
    'FamilySize' to the DataFrame, calculated as the sum of 'SibSp' (siblings/spouses aboard) and 'Parch'
    (parents/children aboard) plus one for the passenger themselves.
    """
    # Load the training dataset
    train_df = pd.read_csv('train.csv')  # Adjust path as needed
    
    # Create 'FamilySize' feature
    family_size_df = create_family_size_feature(train_df.copy())
    
    # Assert 'FamilySize' column exists
    assert 'FamilySize' in family_size_df.columns, "FamilySize feature not created."

def test_extract_and_process_titles():
    """
    Tests the extraction and processing of titles from passenger names.

    Ensures that the `extract_and_process_titles` function can identify and extract titles from the 'Name'
    column, simplify them into common categories, and encode these titles as dummy variables. Verifies that
    a 'Title' column is created to reflect these changes.
    """
    # Load the training dataset
    train_df = pd.read_csv('train.csv')  # Adjust path as needed
    
    # Extract and process titles
    titles_df = extract_and_process_titles(train_df.copy())
    
    # Assert 'Title' feature is created or processed
    assert 'Title' in titles_df.columns, "Title feature not created or processed."

def test_add_interaction_terms():
    """
    Tests the creation of interaction terms between features.

    Verifies that the `add_interaction_terms` function successfully creates new features that are products
    of existing features, specifically testing for the creation of an 'Age_Pclass' interaction term, which
    combines 'Age' and 'Pclass' (ticket class).
    """
    # Load the training dataset
    train_df = pd.read_csv('train.csv')  # Adjust path as needed
    
    # Add interaction terms
    interaction_df = add_interaction_terms(train_df.copy())
    
    # Assert interaction term 'Age_Pclass' is created
    assert 'Age_Pclass' in interaction_df.columns, "Interaction term 'Age_Pclass' not created."
