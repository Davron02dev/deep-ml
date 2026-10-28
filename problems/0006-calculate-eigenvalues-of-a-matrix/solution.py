import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix=np.array(matrix)
	eigenvalue=np.linalg.eigvals(matrix).real
	return eigenvalue