# isort:skip
import os
import sys
from typing import List, Union

from preprocessor.models import Data

sys.path.append(os.getcwd())


def create_data_fixture(X: List[str], y: List[Union[str, int]]) -> Data:
    data = {'X': X, 'y': y}
    return Data(**data)
