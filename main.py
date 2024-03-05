from utils.data_import import import_data
from utils.clean import clean_data
from utils.model_ready import prepare_model_data
from utils.adding_data import add_population_density

def main():
    # Import raw data
    raw_data = import_data()

    # Clean the data
    clean_data(raw_data)

    # Add population density
    cleaned_data_file = './src/cleaned_data.csv'
    add_population_density(cleaned_data_file)

    # Prepare model data
    prepare_model_data(cleaned_data_file)

if __name__ == "__main__":
    main()