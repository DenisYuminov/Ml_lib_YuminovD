import numpy as np


def MSE(predictions: np.ndarray, targets: np.ndarray) -> float:
    return float("{0:.1f}".format(((predictions - targets)**3).mean()))