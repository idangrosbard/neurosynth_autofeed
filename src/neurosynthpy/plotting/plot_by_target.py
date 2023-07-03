from plot_coordinates import plot_anatomical_voi

def extract_coordinates(df, target, col_name):
    '''
    a function that recives a target association/paper  and returns the relevant VOIs 
    coordinates that are connected to this target.

    input:
        df - a dataframe that contains the coordinates of all the VOIs and the rest of the data from Neurosynth
        target - the target association/paper
        col_name - the name of the column that contains the possible targets
    output:
        voi_coords - a numpy array that contains the coordinates of the VOIs that are connected to the target
    '''

    # Filter the DF according to the target
    filtered = df[df[col_name] == target][['x', 'y', 'z']]
    
    # Convert the cooardinates to numpy
    voi_coords = filtered.to_numpy()

    return voi_coords


def plot_by_target(df, target, col_name):
    '''
    a function that recives VOIs of a target association/paper and plots the relevant VOIs
    input:
        df - a dataframe that contains the coordinates of all the VOIs and the rest of the data from Neurosynth
        target - the target association/paper
        col_name - the name of the column that contains the possible targets
    output:
        plot - a plot of the VOIs that are connected to the target
    '''

    # Extract the coordinates of the VOIs
    voi_coords = extract_coordinates(df, target, col_name)
    
    # Plot the VOIs
    return plot_anatomical_voi(voi_coords)