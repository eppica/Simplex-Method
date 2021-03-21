import re

base_variables = []
non_base_variables = []
M = 9999
matrix = []
objective = []
independent_terms = []
coefitients = []


index_f = 0
index_a = 0


def split_multiplier_and_operands(equation):
    regex = r"((\+|-)?\d*)([a-zA-Z]*?\d)"
    matches = re.finditer(regex, equation, re.MULTILINE)
    operands = {}
    for match in matches:
        if (match.group(1) is None) or (match.group(1) == '+') or (match.group(1) == '-') or (match.group(1) == ''):
            operands.update({match.group(3): 1})
        else:
            operands.update({match.group(3): int(match.group(1))})

    return operands


def fill_matrix(equation):
    operands = split_multiplier_and_operands(equation)
    line = []
    for key, value in operands.items():
        for variable in coefitients:
            if variable not in operands.keys():
                line.append(0)
            elif variable == key:
                line.append(value)

    matrix.append(line)


def fill_objective(equation):
    operands = split_multiplier_and_operands(equation)
    for key, value in operands.items():
        objective.append(-1 * value)
        base_variables.append(key)
        coefitients.append(key)


def add_matrix_gap_and_artificial():
    for i in range(0, len(non_base_variables)):
        for j in range(0, len(non_base_variables)):
            if i == j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)


def output_file():
    file_output = open("problems/test.py", "w")
    file_output.write(f'base_variables = {base_variables}\n')
    file_output.write(f'non_base_variables = {non_base_variables}\n')
    file_output.write(f'M = {M}\n')
    file_output.write(f'matrix = {matrix}\n')
    file_output.write(f'objective = {objective}\n')
    file_output.write(f'total = 0\n')
    file_output.write(f'independent_terms = {independent_terms}\n')
    file_output.write(f'quotients = []\n')
    file_output.close()


def restrictions_to_default_pattern(f):
    global index_f, index_a

    regex = r"(=)|(<=)|(>=)"
    pattern = re.compile(regex)

    for i in range(1, len(f)):
        f[i] = f[i].replace(' ', '')
        match = pattern.search(f[i])
        if match:
            if match.group(1):
                equation, term = f[i].split(match.group(1))
                independent_terms.append(int(term))
                fill_matrix(equation)
                index_a += 1
                non_base_variables.append(f'a{index_a}')
                base_variables.append(f'a{index_a}')
                objective.append(M)

            if match.group(2):
                equation, term = f[i].split(match.group(2))
                independent_terms.append(int(term))
                fill_matrix(equation)
                index_f += 1
                non_base_variables.append(f'f{index_f}')
                base_variables.append(f'f{index_f}')
                objective.append(0)

            if match.group(3):
                equation, term = f[i].split(match.group(3))
                independent_terms.append(int(term))
                fill_matrix(equation)
                index_f += 1
                index_a += 1
                base_variables.append(f'f{index_f}')
                non_base_variables.append(f'f{index_f}')
                base_variables.append(f'a{index_a}')
                non_base_variables.append(f'a{index_a}')
                objective.append(0)


def print_all_variables():
    print(f'base_variables = {base_variables}\n')
    print(f'non_base_variables = {non_base_variables}\n')
    print(f'matrix = {matrix}\n')
    print(f'objective = {objective}\n')
    print(f'independent_terms = {independent_terms}\n')


def main():

    f = open('input.txt', 'r').read().split('\n')

    for i in range(0, len(f)):
        f[i] = f[i].replace(' ', '')

    objective_name = f[0].split('=')

    fill_objective(objective_name[1])

    restrictions_to_default_pattern(f)

    add_matrix_gap_and_artificial()

    print_all_variables()


main()
