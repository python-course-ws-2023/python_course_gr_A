import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_dataset(filepath):
    """
    Loads a dataset from the specified filepath.
    
    Parameters:
    - filepath (str): The path to the CSV file containing the dataset.
    
    Returns:
    - DataFrame: A pandas DataFrame containing the loaded dataset.
    """
    return pd.read_csv(filepath)

def demonstrate_preprocessing(filepath):
    
    # Set the aesthetics for the plots
    sns.set(style="whitegrid")
    
    # Survival rate by Sex
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 3, 1)
    sns.barplot(x='Sex', y='Survived', data=filepath)
    plt.title('Survival Rate by Sex')

    # Survival rate by Pclass
    plt.subplot(1, 3, 2)
    sns.barplot(x='Pclass', y='Survived', data=filepath)
    plt.title('Survival Rate by Pclass')

    # Survival rate by Embarked
    plt.subplot(1, 3, 3)
    sns.barplot(x='Embarked', y='Survived', data=filepath)
    plt.title('Survival Rate by Embarked')

    # Show the plots
    plt.tight_layout()
    plt.show()

    # Handling Missing Data: 'Age', 'Cabin', and 'Embarked'
    # Displaying the percentage of missing data for these columns
    missing_percentage = filepath.isnull().mean() * 100
    missing_percentage = missing_percentage[missing_percentage > 0]
    missing_percentage.sort_values(inplace=True, ascending=False)

    # Plotting the missing data percentages
    plt.figure(figsize=(8, 4))
    missing_percentage.plot.bar()
    plt.title('Percentage of Missing Data by Feature')
    plt.xlabel('Features')
    plt.ylabel('Percentage of Missing Data')
    plt.show()
    
    pass
    

def fill_missing_values(dataframe):
    """
    Fills missing values in the 'Age' and 'Embarked' columns of the DataFrame. 
    'Cabin' column is dropped due to high number of missing values.
    
    Parameters:
    - dataframe (DataFrame): The pandas DataFrame whose missing values are to be filled.
    
    Returns:
    - DataFrame: The DataFrame with missing values filled and 'Cabin' column dropped.
    """
    dataframe['Age'].fillna(dataframe['Age'].median(), inplace=True)
    dataframe['Embarked'].fillna(dataframe['Embarked'].mode()[0], inplace=True)
    dataframe.drop(columns='Cabin', inplace=True)
    return dataframe

def preprocess_data(dataframe):
    """
    Preprocesses the test data to align with the training data format. 
    This includes filling missing values, computing 'FamilySize', mapping 'Sex' and 'Embarked' to numeric values, 
    and one-hot encoding 'Embarked' and 'Sex' columns if necessary.
    
    Parameters:
    - test_df (DataFrame): The test data DataFrame to preprocess.
    - train_df (DataFrame): The training data DataFrame used as a reference for filling missing values.
    
    Returns:
    - DataFrame: The preprocessed test data DataFrame.
    """
    # Conditional handling for 'Cabin' column before dropping it
    if 'Cabin' in dataframe.columns:
        dataframe['CabinType'] = dataframe['Cabin'].apply(lambda x: x[0] if pd.notna(x) else 'Unknown')
        dataframe.drop(columns=['Cabin'], inplace=True)
        
    # Filling missing values using median from the training DataFrame
    median_age = dataframe['Age'].median()
    median_fare = dataframe['Fare'].median()
    dataframe['Age'].fillna(median_age, inplace=True)
    dataframe['Fare'].fillna(median_fare, inplace=True)
    
    # Computing 'FamilySize'
    dataframe['FamilySize'] = dataframe['SibSp'] + dataframe['Parch'] + 1
    
    # Mapping 'Sex' and 'Embarked' to numeric values
    dataframe['Sex'] = dataframe['Sex'].map({'male': 0, 'female': 1})
    dataframe['Embarked'] = dataframe['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    """"
    # One-hot encoding 'Embarked' and 'Sex' columns if applicable
    if 'Embarked' in dataframe.columns and 'Sex' in dataframe.columns:
        dataframe = pd.get_dummies(dataframe, columns=['Embarked', 'Sex'], prefix=['Embarked', 'Sex'], drop_first=False)
    """

    
    return dataframe




