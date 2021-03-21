base_variables = ['x1', 'x2', 'f1', 'f2', 'f3']
non_base_variables = ['f1', 'f2', 'f3']

matrix = [
    [1.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 2.0, 0.0, 1.0, 0.0],
    [2.0, 3.0, 0.0, 0.0, 1.0]
]

objective = [-3, -5, 0, 0, 0]

total = 0

independent_terms = [4, 12, 21]

M = None

quotients = []
