import plotly.graph_objects as go
import numpy as np


class Visualisation():

    @staticmethod
    def visualise_predicted_trace(prediction: np.ndarray, inputs:np.ndarray, targets:np.ndarray,plot_title=''):
        figure = go.Figure()

        targets_array = go.Scatter(
            x=inputs,
            y=targets,
            name="Target",
            mode='markers'
        )

        prediction_array = go.Scatter(
            x=inputs,
            y=prediction,
            name="Prediction",
            mode='lines'
        )
        figure.update_layout(
            title=plot_title,
            legend_title="Legend name"
        )
        figure.add_traces([targets_array, prediction_array])
        figure.show()

    @staticmethod
    def visualise_error():
        pass