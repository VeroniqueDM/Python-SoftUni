class InvalidColumnError(Exception):
    pass

class FullColumnError(Exception):
    pass

def print_matrix(matrix):
    for el in matrix:
        print(el)

def col_is_valid(col, max_col_index):
    if not (0<= col <= max_col_index):
        raise InvalidColumnError

def place_player_choice(ma, selected_col_ind, player_num):
    rows_count = len(ma)
    for row_ind in range(rows_count -1, -1, -1):
        if ma[row_ind][selected_col_ind] == 0:
            ma[row_ind][selected_col_ind] = player_num
            return row_ind,selected_col_ind
    raise FullColumnError


def is_player_num(ma, row, col, player_num):
    if col <0 or row<0:
        return False
    try:
        if ma[row][col]==player_num:
            return True
    except IndexError:
        return False
    return False

def is_horizontal(ma, row, col, player_num, slots_count = 4):
    right = []
    for index in range(slots_count):
        if is_player_num(ma, row, col + index, player_num):
            right.append(True)
        else:
            break
    left = []
    for index in range(slots_count):
        if is_player_num(ma, row, col - index, player_num):
            left.append(True)
        else:
            break
    # count_right = [ for index in range(slots_count) if ].count(True)
    # count_left = [is_player_num(ma, row, col-index, player_num) for index in range(slots_count)].count(True)
    # It should be strict '>' because we are counting the current element as well
    return len(left + right) > slots_count
# def is_vertical(ma, row, col, player_num, slots_count = 4):
#     count_up = [is_player_num(ma,row-index,col,player_num) for index in range(slots_count)].count(True)
#     count_down = [is_player_num(ma,row+index,col,player_num) for index in range(slots_count)].count(True)
#     return (count_down+count_up) > slots_count
def is_right_diagonal(ma, row, col, player_num, slots_count = 4):
    count_right_up = [is_player_num(ma, row-index, col + index, player_num) for index in range(slots_count)].count(True)
    count_left_down = [is_player_num(ma, row+index, col - index, player_num) for index in range(slots_count)].count(True)
    return (count_left_down + count_right_up) > 4

def is_left_diagonal(ma, row, col, player_num, slots_count = 4):
    count_left_up = [is_player_num(ma, row-index, col - index, player_num) for index in range(slots_count)].count(True)
    count_right_down = [is_player_num(ma, row+index, col + index, player_num) for index in range(slots_count)].count(True)
    return (count_left_up + count_right_down) > 4


def is_winner(ma, row, col, player_num, slots_count = 4):
    # is_horizontal(ma, row, col, player_num, slots_count=4)
    # is_right_diagonal(ma, row, col, player_num, slots_count=4)
    # is_left_diagonal(ma, row, col, player_num, slots_count=4)
    # is_vertical(ma, row, col, player_num, slots_count=4)
    # is_right = all( [is_player_num(ma,row,col+index,player_num)] for index in range(slots_count))
    # is_left =all([is_player_num(ma,row,col-index,player_num)] for index in range(slots_count))
    # is_up = all([is_player_num(ma,row-index,col,player_num)] for index in range(slots_count))
    is_down = all([is_player_num(ma,row+index,col,player_num) for index in range(slots_count)])
    # is_diag_upleft =all([is_player_num(ma,row-index,col-index,player_num)] for index in range(slots_count))
    # is_diag_upright =all([is_player_num(ma,row-index,col+index,player_num)] for index in range(slots_count))
    # is_diag_downleft =all([is_player_num(ma,row+index,col-index,player_num)] for index in range(slots_count))
    # is_diag_downright =all([is_player_num(ma,row+index,col+index,player_num)] for index in range(slots_count))
    if any([is_horizontal(ma, row, col, player_num, slots_count),
            is_right_diagonal(ma, row, col, player_num, slots_count),
            is_left_diagonal(ma, row, col, player_num, slots_count),
            is_down,
            ]):
        return True
    return False
rows_count = 6
cols_count = 7
matrix = [[0 for _ in range(cols_count)] for row_num in range(rows_count)]
player_num = 1

while True:
    player_num = 2 if player_num %2 == 0 else 1
    try:
        column_num = int(input(f'Player {player_num}, please choose a column: ')) -1

        col_is_valid(column_num, cols_count - 1)
        row, col = place_player_choice(matrix, column_num, player_num)
        if is_winner(matrix, row, col,player_num):
            print_matrix(matrix)
            print(f"The winner is player {player_num}")
            break
        print_matrix(matrix)
    except InvalidColumnError:
        print(f"This column is not valid. Please select a number between {1} and {cols_count}")
        continue
    except ValueError:
        print(f"Please select a valid digid.")
        continue
    except FullColumnError:
        print(f"This column is already full. Please select another column!")
        continue
    player_num +=1