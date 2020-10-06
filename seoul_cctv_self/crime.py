import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.file_handler import FileReader
from config import basedir
import pandas as pd

class Service:
    def __init__(self):
        self.fileReader = FileReader() 
        self.seoul_cctv = os.path.join(basedir, 'seoul_cctv')
        self.data = os.path.join(self.seoul_cctv, 'data')

    def read_data(self, payload) -> object:
        this = self.fileReader
        this.context = self.data
        this.fname = payload
        print(pd.read_csv(os.path.join(self.data, this.fname)))
        print('*'*50)
        return pd.read_csv(os.path.join(self.data, this.fname), encoding='utf-8', thousands=',')




if __name__ == "__main__":
    t = Service()
    t.read_data('cctv_in_seoul.csv')