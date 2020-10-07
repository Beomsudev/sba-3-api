import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
from seoul_cctv_tea.police import Police
import folium

class CrimeMap:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()

    def hook_process(self):
        print('----------- CRIME MAP ----------')
        police = Police()
        police_norm = police.get_police_norm()



if __name__ == "__main__":
    crime = CrimeMap()
    crime.hook_process()