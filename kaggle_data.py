import csv
import os
import kagglehub

class KaggleData:
    kaggle_path: str = ''
    data: str = ''
    def __init__(self, kaggle_path: str) -> None:
        self.kaggle_path = kaggle_path
        self.data = self.get_data()

    def get_data(self) -> str:
        data_path = kagglehub.dataset_download(self.kaggle_path)
        data_file: str = os.listdir(data_path)[0]
        return os.path.join(data_path, data_file)
    