from titanic_survival_package.data_preprocessing import load_dataset, fill_missing_values, preprocess_data

def test_load_dataset():
    """
    Tests the loading of a dataset from a CSV file.

    Ensures that the `load_dataset` function can successfully load data from a given file path
    and that the resulting DataFrame is not empty.
    """
    # Load training data and verify it's not empty
    train_df = load_dataset('train.csv')
    assert not train_df.empty, "Failed to load training data. The DataFrame is empty."

def test_fill_missing_values():
    """
    Tests the handling of missing values within a dataset.

    Verifies that the `fill_missing_values` function correctly fills or handles all missing values
    within the dataset, ensuring no missing values remain.
    """
    # Load training data
    train_df = load_dataset('train.csv')
    
    # Apply missing value handling
    preprocessed_df = fill_missing_values(train_df.copy())
    
    # Assert no missing values remain
    assert preprocessed_df.isnull().sum().max() == 0, "Missing values were not properly handled."

def test_preprocess_test_data():
    """
    Tests the preprocessing of test data to align with the training data format.

    Ensures that the `preprocess_test_data` function applies similar preprocessing steps to the test
    data as were applied to the training data, including handling missing values and feature engineering,
    and verifies that no unexpected missing values remain after preprocessing.
    """
    # Load training data and test data
    train_df = load_dataset('train.csv')
    test_df = load_dataset('test.csv')
    
    # Preprocess test data using training data as a reference
    test_preprocessed_df = preprocess_data(test_df.copy())
    
    # Check for any remaining missing values
    missing_values = test_preprocessed_df.isnull().sum()
    print(missing_values[missing_values > 0])
    
    # Assert no missing values remain after preprocessing
    assert test_preprocessed_df.isnull().sum().max() == 0, "Test data still contains missing values after preprocessing."
