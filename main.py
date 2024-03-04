from utils.data_import import import_data
from utils.clean import clean_data

def main():
    # Import raw data
    raw_data = import_data()

    # Clean the data
    clean_data(raw_data)

if __name__ == "__main__":
    main()