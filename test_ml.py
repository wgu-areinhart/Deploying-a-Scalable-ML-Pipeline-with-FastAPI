import pytest
# TODO: add necessary import
from ml.model import train_model, inference, compute_model_metrics
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_returns_correct_type():
    """
    Test that train_model returns a RandomForestClassifier

    """
    X = [[0, 1], [1, 0]]
    y = [0, 1]
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_inference_output_type():
    """
    Test that inference returns a NumPy array

    """
    X = [[0, 1], [1, 0]]
    y  = [0, 1]
    model = train_model(X, y)
    preds = inference(model, X)
    assert isinstance(preds, np.ndarray)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_outputs():
    """
    Test compute_model metrics outputs expected float values

    """
    y = np.array([1, 0, 1])
    preds = np.array([1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance( fbeta, float)
