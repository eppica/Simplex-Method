base_variables = ['x1', 'x2', 'f1', 'f2', 'a1']
non_base_variables = ['f1', 'f2', 'a1']

M = 9999

matrix = [
    [1.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 2.0, 0.0, 1.0, 0.0],
    [3.0, 2.0, 0.0, 0.0, 1.0]
]

objective = [-3, -5, 0, 0, M]

total = 0

independent_terms = [4, 12, 18]

quotients = []
