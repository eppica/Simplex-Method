import math
import os
from tabulate import tabulate
from problems.generic_problem import *
from resources.colors import *
import xlsxwriter

INITIAL_ROW = 0

try:
    os.mkdir('output')
except:
    pass

workbook = xlsxwriter.Workbook('output/simplex_solver.xlsx')
worksheet = workbook.add_worksheet('steps')


def big_m():
    global total
    div = -1 * M

    for i, base in enumerate(non_base_variables):
        if 'a' in base:

            for j in range(0, len(objective)):
                objective[j] = round(objective[j] + div * matrix[i][j], 5)

            total = round(total + div * independent_terms[i], 5)


def is_optimum_solution(function):
    for number in function:
        if number < 0:
            return False
    return True


def get_pivot_column_index(function):
    return function.index(min(function))


def get_pivot_line_index(j):
    for i, term in enumerate(independent_terms):
        coefficient = matrix[i][j]
        if coefficient <= 0:
            quotients.append(math.inf)
        else:
            quotients.append(term / coefficient)
    return quotients.index(min_positive(quotients))


def min_positive(iterable):
    for i, number in enumerate(iterable):
        if number < 0:
            iterable[i] = math.inf

    try:
        if min(iterable) != math.inf:
            print("Min Division", min(iterable))
            return min(iterable)
        else:
            raise Exception('There is no minimum positive')
    except:
        print('No optimal solution')
        exit(1)


def reset_pivot_line():
    for i, number in enumerate(matrix[pivot_line_index]):
        matrix[pivot_line_index][i] = number / pivot_number

    independent_terms[pivot_line_index] = independent_terms[pivot_line_index] / pivot_number


def scale_matrix():
    global total
    for i, line in enumerate(matrix):
        if i != pivot_line_index:
            div = -1 * line[pivot_column_index]
            for j, value in enumerate(line):
                matrix[i][j] = round(value + div * matrix[pivot_line_index][j],5)
            independent_terms[i] = round(independent_terms[i] + div * independent_terms[pivot_line_index], 5)

    div = -1 * objective[pivot_column_index]
    for j in range(0, len(objective)):
        objective[j] = round(objective[j] + div * matrix[pivot_line_index][j], 5)

    total = round(total + div * independent_terms[pivot_line_index], 5)


def print_matrix(column=None, line=None):
    printable_matrix = create_printable_matrix()

    output_excel(printable_matrix, column, line)

    if column or line:
        format_printable_matrix(printable_matrix, column, line)

    print(tabulate(printable_matrix, headers='firstrow', tablefmt='fancy_grid'))


def create_printable_matrix():
    lines = len(independent_terms) + 2
    columns = len(base_variables) + 2
    matrix_aux = lines * [columns * ['']]
    matrix_aux[0] = organize_line('\\', base_variables, 'b')
    for i in range(lines - 2):
        matrix_aux[i + 1] = organize_line(non_base_variables[i], matrix[i], independent_terms[i])
    matrix_aux[lines - 1] = organize_line('Z', objective, total)

    return matrix_aux


def format_printable_matrix(matrix_aux, column, line):
    line += 1
    column += 1
    for i in range(0, len(matrix_aux)):
        for j in range(0, len(matrix_aux[0])):
            if j == column and i == line:
                matrix_aux[i][j] = f'{COLOR["BLUE"]}{COLOR["BOLD"]}{matrix_aux[i][j]}{COLOR["END"]}'
            elif i == line:
                matrix_aux[i][j] = f'{COLOR["RED"]}{matrix_aux[i][j]}{COLOR["END"]}'
            elif j == column:
                matrix_aux[i][j] = f'{COLOR["RED"]}{matrix_aux[i][j]}{COLOR["END"]}'


def organize_line(non_base, values, independent):
    line = (len(base_variables) + 2) * ['']
    line[0] = str(non_base)
    for i, value in enumerate(values):
        line[i + 1] = str(values[i])
    line[len(values) + 1] = str(independent)
    return line


def output_excel(array, column, line):
    global INITIAL_ROW, worksheet

    cell_format = workbook.add_format()
    cell_format.set_bg_color('#FF6569')

    cell_format_pivot = workbook.add_format()
    cell_format_pivot.set_bg_color('#0ABCF4')

    for row_index, row in enumerate(array):
        for column_index, data in enumerate(row):
            if column is not None and line is not None:
                if row_index == line + 1 and column_index == column + 1:
                    worksheet.write(row_index + INITIAL_ROW, column_index, str(data), cell_format_pivot)
                elif row_index == line + 1 or column_index == column + 1:
                    worksheet.write(row_index + INITIAL_ROW, column_index, str(data), cell_format)
                else:
                    worksheet.write(row_index + INITIAL_ROW, column_index, str(data))
            else:
                worksheet.write(row_index + INITIAL_ROW, column_index, str(data))
    if column is not None and line is not None:
        for row_index, data in enumerate(quotients):
            if row_index == 0:
                worksheet.write(row_index + INITIAL_ROW, len(array[0]) + 1, 'divisions')
                pass
            worksheet.write(row_index + 1 + INITIAL_ROW, len(array[0]) + 1, str(data))

    INITIAL_ROW += len(array) + 1


def header():
    print(
        "   _____ _                 _            \n"
        "  / ____(_)               | |           \n"
        " | (___  _ _ __ ___  _ __ | | _____  __ \n"
        "  \\___ \\| | '_ ` _ \\| '_ \\| |/ _ \\ \\/ / \n"
        "  ____) | | | | | | | |_) | |  __/>  <  \n"
        " |_____/|_|_| |_| |_| .__/|_|\\___/_/\\_\\ \n"
        "                    | |                 \n"
        "                    |_|                 \n"
    )

    input(" PRESS ENTER TO START")
    os.system('cls')


def init():
    header()
    print(' Initial Table\n')
    print_matrix()
    print('\n=======================================================================================================\n')


init()

if M:
    big_m()


while True:

    if not is_optimum_solution(objective):
        pivot_column_index = get_pivot_column_index(objective)

        print("Pivot Column Index", pivot_column_index)

        pivot_line_index = get_pivot_line_index(pivot_column_index)
        print("Pivot Line Index", pivot_line_index)

        pivot_number = matrix[pivot_line_index][pivot_column_index]
        print("Pivot Number", pivot_number)

        print_matrix(pivot_column_index, pivot_line_index)

        non_base_variables[pivot_line_index] = base_variables[pivot_column_index]

        reset_pivot_line()

        scale_matrix()
    else:
        break

    quotients.clear()


print('\n\n\n=======================================================================================================\n')
print(' Final Table\n')
print_matrix()
workbook.close()

