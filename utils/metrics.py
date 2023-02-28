import numpy as np


def MSE(predictions: np.ndarray, targets: np.ndarray) -> float:
    return float("{0:.2f}".format(((predictions - targets)**2).mean()))