import pandas as pd

from src.helper.paths import DATA_DIR

FILE_PATH = DATA_DIR + "/SeoulBikeData.csv"
def load_data():
    data = pd.read_csv(FILE_PATH)
    return data