import os
import pandas as pd
from dataclasses import dataclass
from src.logger import lg
from src.exception import CustomException
from src.components import data_collection

class DataStoringConfig:
    