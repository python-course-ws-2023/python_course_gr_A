import pandas as pd

def create_family_size_feature(dataframe):
    """
    Adds a new feature 'FamilySize' to the DataFrame, calculated as the sum of 'SibSp' (siblings/spouse aboard) 
    and 'Parch' (parents/children aboard) plus one for the passenger themselves.
    
    Parameters:
    - dataframe (DataFrame): The pandas DataFrame to which the 'FamilySize' feature will be added.
    
    Returns:
    - DataFrame: The DataFrame with the new 'FamilySize' feature included.
    """
    dataframe['FamilySize'] = dataframe['SibSp'] + dataframe['Parch'] + 1
    return dataframe

def extract_and_process_titles(dataframe):
    """
    Extracts titles from the 'Name' column, simplifies common or rare titles, and encodes these titles into 
    dummy variables. The encoded titles are then appended to the DataFrame as new columns.
    
    Parameters:
    - dataframe (DataFrame): The pandas DataFrame from which titles are to be extracted and processed.
    
    Returns:
    - DataFrame: The DataFrame with new columns added for the encoded title dummy variables.
    """
    # Extraction of titles using regular expression
    dataframe['Title'] = dataframe['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    
    # Simplification of titles to consolidate rare or equivalent titles
    title_replacements = {
        'Lady': 'Rare', 'Countess': 'Rare', 'Capt': 'Rare', 'Col': 'Rare',
        'Don': 'Rare', 'Dr': 'Rare', 'Major': 'Rare', 'Rev': 'Rare', 'Sir': 'Rare',
        'Jonkheer': 'Rare', 'Dona': 'Rare', 'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'
    }
    dataframe['Title'] = dataframe['Title'].replace(title_replacements)
    
    # Encoding of titles into dummy variables and appending them to the DataFrame
    title_dummies = pd.get_dummies(dataframe['Title'], prefix='Title')
    dataframe = pd.concat([dataframe, title_dummies], axis=1)
    
    return dataframe

def add_interaction_terms(dataframe):
    """
    Creates and adds interaction terms to the DataFrame, specifically the interaction between 'Age' and 'Pclass',
    to potentially capture combined effects on survival.
    
    Parameters:
    - dataframe (DataFrame): The pandas DataFrame to which the interaction terms will be added.
    
    Returns:
    - DataFrame: The DataFrame with the new interaction terms included.
    """
    dataframe['Age_Pclass'] = dataframe['Age'] * dataframe['Pclass']
    return dataframe

def drop_unnecessary_features(dataframe):
    """
    Removes features from the DataFrame that are deemed unnecessary for modeling, 
    such as 'Ticket', 'Name', and 'PassengerId'.
    
    Parameters:
    - dataframe (DataFrame): The pandas DataFrame from which unnecessary features are to be dropped.
    
    Returns:
    - DataFrame: The DataFrame with specified features removed.
    """
    dataframe.drop(['Ticket', 'Name', 'Title'], axis=1, inplace=True)
    return dataframe
