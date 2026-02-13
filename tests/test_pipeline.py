import pandas as pd
from src.extract import extract_data
from src.transform import clean_data

def test_extract_data():
    df = extract_data("raw_bangladesh_data/Flight_Price_Dataset_of_Bangladesh.csv")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0

def test_clean_data():
    sample_data = {
        "Airline": ["A", "A", None],
        "Price": [100, 100, 200]
    }
    df = pd.DataFrame(sample_data)

    cleaned_df = clean_data(df)

    # Check duplicates removed and nulls handled
    assert cleaned_df.isnull().sum().sum() == 0
    assert len(cleaned_df) <= len(df)
