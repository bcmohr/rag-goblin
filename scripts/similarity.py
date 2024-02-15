import numpy as np

# Similarity calculation function
def similar(vector1, vector2):
    # Calculating cosine similarity as an example
    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    return dot_product / (norm_vector1 * norm_vector2)

if __name__ == "__main__":
    print(similar(np.array([1, 2, 3]), np.array([4, 5, 6])))