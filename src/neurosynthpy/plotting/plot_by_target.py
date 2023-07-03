from plot_coordinates import plot_anatomical_voi
import pandas as pd
import numpy as np


def extract_coordinates(df: pd.DataFrame, target: str, col_name: str) -> np.ndarray:
    '''
    A function that receives a target association/paper and returns the relevant VOIs 
    coordinates that are connected to this target.

    Args:
        df (pd.DataFrame): A dataframe that contains the coordinates of all the VOIs and the rest of the data from Neurosynth
        target (str): The target association/paper
        col_name (str): The name of the column that contains the possible targets

    Returns:
        np.ndarray: A numpy array that contains the coordinates of the VOIs that are connected to the target
    '''

    # Filter the DataFrame according to the target
    filtered = df[df[col_name] == target][['x', 'y', 'z']]
    
    # Convert the coordinates to numpy
    voi_coords = filtered.to_numpy()

    return voi_coords


def plot_by_target(df: pd.DataFrame, target: str, col_name: str):
    '''
    A function that receives VOIs of a target association/paper and plots the relevant VOIs.

    Args:
        df (pd.DataFrame): A dataframe that contains the coordinates of all the VOIs and the rest of the data from Neurosynth
        target (str): The target association/paper
        col_name (str): The name of the column that contains the possible targets

    Returns:
        plot: A plot of the VOIs that are connected to the target
    '''

    # Extract the coordinates of the VOIs
    voi_coords = extract_coordinates(df, target, col_name)
    
    # Plot the VOIs
    return plot_anatomical_voi(voi_coords)