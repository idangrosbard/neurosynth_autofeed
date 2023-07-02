import plot_anatomical_voi
import plot_by_papers
import plot_assosiations
import plot_association_hist
import plot_by_assosiations

def plots(coord, papers_df, assosication_df): # the input should be the final class or something
    '''
    Main script of plotting functions
    '''

    # Plot the anatimical locations of the VOIs
    anatomical = plot_anatomical_voi(coord)

    # Plot the VOIs relavant for a specific paper
    by_paper = plot_by_papers(papers_df)

    # Plot the VOIs relavant for a specific assosiation/function
    by_assosiations = plot_by_assosiations(assosication_df)

    # Plot the assosiation map for a specific VOI
    assosiations_map = plot_assosiations(assosication_df)

    # Plot the histogram of the assosiations
    assosiations_hist = plot_association_hist(assosication_df)

    return anatomical, by_paper, by_assosiations, assosiations_map, assosiations_hist

