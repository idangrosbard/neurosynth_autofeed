import matplotlib.pyplot as plt

def plot_association_hist(associated_regions_list, z_scores_list, threshold=0.05):
    '''
    the function plots a histogram of the associated regions and functions based on the z-scores of the associations
    input:
        associated_regions_list: a list of associated regions and functions
        z_scores_list: a list of z-scores of the associations
        threshold: the threshold to filter out the associations that are not significant
    output:
        a histogram of the associated regions and functions based on the z-scores of the associations
    '''

    # Use the threshold to filter out the associations that are not significant
    significant_associations = [region for region, z_score in zip(associated_regions_list, z_scores_list) if z_score > threshold]

    # Calculate the weights for each association based on the z-scores of significant associations
    weights = [abs(z_score) for z_score in z_scores_list if z_score > threshold]

    # Sort the significant associations and weights based on weights (descending order)
    sorted_data = sorted(zip(significant_associations, weights), key=lambda x: x[1], reverse=True)
    sorted_associations, sorted_weights = zip(*sorted_data)

    # Create a histogram using the sorted weights and associations
    plt.figure(figsize=(10, 6))
    figure = plt.hist(sorted_associations, bins=len(sorted_associations), weights=sorted_weights, color='#68228B', edgecolor='white')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Associated Regions/Functions')
    plt.ylabel('Weighted Z-Score')
    plt.title('Weighted Histogram of Associations')
    plt.tight_layout()

    return figure