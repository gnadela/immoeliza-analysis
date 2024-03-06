# immoeliza-analysis

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 🛠️ Updates
N/A

## 📒 Description

This repo is designed to load scraped data from an earlier project repo, organize, normalize, and clean the raw data for analysis. That analysis was conducted and catelogued in notebooks in the analysis folder and then used to further clean the data for future modeling efforts. The project is later presented to a client in a project update meeting which can be found in the reports folder. 

## 📦 Repo structure

```
.
├── analysis/
│ └── *Final_Notebook.ipynb
│ └── Bears_Notebook.ipynb
│ └── Caros_Notebook.ipynb
│ └── Geraldines_Notebook.ipynb
│ └── Viktors_Notebook.ipynb
├── reports/
│ └── presentation.pdf
|── src/
│ └── external_data/
│   └── PopulationDensity.csv
│   └── Postal_Refnis.csv
│   └── SectorData.csv
│   └── checkforlargeareaaggregations.csv
│ └── raw_data.csv
│ └── clean_data.csv
│ └── model_data.csv
|── src/
│ └── adding_data.py
│ └── clean.py
│ └── data_import.py
│ └── model_ready.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 🎮 Usage

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

3. Run the `main.py` file to execute the scraper:

    ```
    python main.py
    ```

4. The program will load and clean the data, add population density data, and create the three csv files in the src folder; raw_data, clean_data, and model_data

## ⏱️ Timeline

The development of this project took 5 days for completion.

## 📌 Personal Situation

This project was completed as part of the AI Boocamp at BeCode.org by team Python Pricers. 

Connect with the Python Pricers on LinkedIn:
1. [Bear Revels](https://www.linkedin.com/in/bear-revels/)
2. [Caroline Van Hoeke](https://www.linkedin.com/in/caroline-van-hoeke-8a3b87123/)
3. [Geraldine Nadela](https://www.linkedin.com/in/geraldine-nadela-60827a11)
4. [Viktor Cosaert](https://www.linkedin.com/in/viktor-cosaert/)
