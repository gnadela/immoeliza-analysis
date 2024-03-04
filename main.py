from utils.data_import import import_data
from utils.clean import clean_data
from utils.model_ready import prepare_model_data  # Import the new module

def main():
    # Import raw data
    raw_data = import_data()

    # Clean the data
    clean_data(raw_data)

    # Prepare model data
    cleaned_data_file = './src/cleaned_data.csv'
    prepare_model_data(cleaned_data_file)  # Call the function from model_ready.py

if __name__ == "__main__":
    main()