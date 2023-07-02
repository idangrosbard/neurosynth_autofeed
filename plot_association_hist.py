import matplotlib.pyplot as plt

def plot_association_hist(associated_regions_list, z_scores_list):
    # Calculate the weights for each association based on the z-scores
    weights = [abs(z_score) for z_score in z_scores_list]

    # Create a histogram using the weights
    plt.figure(figsize=(10, 6))
    plt.hist(associated_regions_list, bins=len(associated_regions_list), weights=weights, color='blue', edgecolor='black')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Associated Regions/Functions')
    plt.ylabel('Weighted Z-Score')
    plt.title('Weighted Histogram of Associations')
    plt.tight_layout()
    plt.show()

    return plt.show()