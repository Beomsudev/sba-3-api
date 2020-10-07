from dataclasses import dataclass
import os
import pandas as pd

@dataclass
class FileReader:
    
    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''
