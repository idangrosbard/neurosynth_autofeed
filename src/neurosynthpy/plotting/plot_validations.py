import pandas as pd

def validate_plot_input_assoc(df: pd.DataFrame) -> bool:
    '''
    Check if the input DataFrame contains necessary columns for association plotting.

    Args:
        df (pd.DataFrame): Input DataFrame to validate.

    Returns:
        bool: True if validation passes.
    
    Raises:
        ValueError: If the input is not a pandas DataFrame or does not contain a 'Name' column.
    '''
    # Check if the df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the 'Name' column exists in the DataFrame
    if 'Name' not in df.columns:
        raise ValueError("Input DataFrame 'df' must contain a 'Name' column.")
    
    return True


def validate_plot_input_study(df: pd.DataFrame) -> bool:
    '''
    Check if the input DataFrame contains necessary columns for study plotting.

    Args:
        df (pd.DataFrame): Input DataFrame to validate.

    Returns:
        bool: True if validation passes.
    
    Raises:
        ValueError: If the input is not a pandas DataFrame or does not contain a 'Study' column.
    '''
    # Check if the df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if the 'Study' column exists in the DataFrame
    if 'Study' not in df.columns:
        raise ValueError("Input DataFrame 'df' must contain a 'Study' column.")
    
    return True