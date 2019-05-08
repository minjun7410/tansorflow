import copy
import queue

def take_input():#입력받는 메서드
    """Accepts the size of the chess board"""

    while True:
        try:
            size = int(input('What is the size of the chessboard? n = \n'))
            if size == 1:
                print("Trivial solution, choose a board size of at least 4")
            if size <= 3:
                print("Enter a value such that size>=4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")


def get_board(size):#0으로 초기화된 체스판으로 만드는 메서드
    """Returns an n by n board"""
    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size#n by n 이 0으로 채워진 배열로 초기화시킨다.
    return board


def print_solutions(solutions, size):#모든 가능한 체스판을 출력하는 메서드
    """Prints all the solutions in user friendly way"""
    for sol in solutions:
        for row in sol:
            print(row)
        print()


def is_safe(board, row, col, size):#해당 위치가 1이 될 수 있는 위치인지 판별하는 메서드
    """Check if it's safe to place a queen at board[x][y]"""

    # check row on left side
    for iy in range(col):#주어진 위치에서 상단으로 가는 직선을 그릴때 1이 나오면 퀸이 죽으므로 false
        if board[row][iy] == 1:
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0:#주어진 위치에서 좌측 상단으로 가는 대각선을 그릴때 1이 나오면 false
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while jx < size and jy >= 0:#주어진 위치에서 우측 상단으로 가는 대각선을 그릴때 1이 나오면 false
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True #모든 직선에서 1이 나오지 않으면 퀸이 죽지 않는다는 뜻이므로 true 리턴


def solve(board, col, size):#재귀적으로 해당 위치의 모든 경우의 수를 따지는 메서드(깊이 우선 탐색 알고리즘)STACK
    """Use backtracking to find all solutions"""
    # base case
    if col >= size:#행의 최대 크기를 넘어서면 리턴
        return

    for i in range(size):#반복적으로 모든 열을 검사한다.
        if is_safe(board, i, col, size):#현재의 위치가 죽지 않는 위치라면
            board[i][col] = 1#1을 넣어준 다음
            if col == size - 1:#만약 그 위치의 행이 최대 사이즈라면
                add_solution(board)#solutions에 배열을 넣어 주고
                board[i][col] = 0#0을 넣어준다.
                return
            solve(board, col + 1, size)#(죽지 않는 위치라면)다음 행을 검사한다.
            # backtrack
            board[i][col] = 0#재귀적으로 모든 경우를 따진 후 이므로 0을 넣어 줌으로써 backtracking 한다.
def add_solution(board):#마지막 행까지 죽지 않는 배열을 완성했다면 호출하는 메서드
    """Saves the board state to the global variable 'solutions'"""
    global solutions#전역변수 solutions
    saved_board = copy.deepcopy(board)#deep copy를 이용해 안의 내용까지 복사
    solutions.append(saved_board)#solutions에 추가


def width_is_safe(array): #너비 우선 탐색에서 해당 케이스가 유망한지 확인하는 메서드
    for i in range(len(array)-1): #만약 3행이 마지막이라면 1행과 2행에 대해서 모두 죽지 않는 위치인지 확인하는 반복문
        diff = (len(array)-1) - i #3행과 1행이면 diff == 2
        if(array[-1] == array[i] - diff)or(array[-1] == array[i] + diff)or(array[-1] == array[i]):
            return False
    return True


def width_solve(size):#내가 만든 너비 우선 탐색 알고리즘 큐
    q_list = queue.Queue() #큐 배열 생성
    for i in range(size): #첫번째 큐 ([0],[1],[2],[3]) 생성하는 반복문
        q_list.put([i])
    while (q_list.empty() == False): #큐가 비어있을 때는 모든 경우를 조사했다는 뜻이므로 그 전은 루프
        got = q_list.get() #가장 먼저 들어온 아이템을 get 한다.
        for i in range(size): #그 아이템의 모든 자식을 따지는 반복문이다.
            array = got + [i] #[0] 이었다면 [0,0] , [0,1]... 이 생긴다.
            if (width_is_safe(array) == True): #따로 구현한 해당 노드가 안전한지 검사하는 메서드를 사용해 유망성을 조사한다.
                if (len(array) == size):#만약 마지막 행에 도달했을 때 유망하다면 완성했음을 뜻하므로
                    width_solution.append(array)#width_solution에 넣어준다.
                    continue
                q_list.put(array)

def width_print(width_solution , size): #모든 가능한 체스판을 출력하는 메서드
    for i in width_solution:
        for j in i:
            for k in range(size):
                if k == j:
                    print('1',' ',end='')
                    continue
                print('0',' ',end='')
            print()
        print()



size = take_input()

board = get_board(size)
solutions = []

solve(board, 0, size)

print_solutions(solutions, size)

print("Total solutions = {}".format(len(solutions)))
print()

width_solution = []

width_solve(size)

width_print(width_solution,size)