from extract import extract_data
from transform import clean_data

def run_pipeline():
    file_path = "raw_bangladesh_data/Flight_Price_Dataset_of_Bangladesh.csv"

    # Extract
    raw_data = extract_data(file_path)
    print("Data extracted successfully.")

    # Transform
    clean_df = clean_data(raw_data)
    print("Data cleaned successfully.")

    # Save cleaned data (Sprint 1 increment)
    clean_df.to_csv("raw_bangladesh_data/cleaned_flight_data.csv", index=False)
    print("Cleaned data saved.")

if __name__ == "__main__":
    run_pipeline()
