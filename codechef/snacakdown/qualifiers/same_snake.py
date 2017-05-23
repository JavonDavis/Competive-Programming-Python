from collections import namedtuple, defaultdict
Snake = namedtuple('Snake', 'start end')
Point = namedtuple('Point', 'x y')
snake1_id = "snake1"
snake2_id = "snake2"



def in_row(snake):
    return snake.start.x == snake.end.x


def is_valid_same_column(snake1, snake2):
    snake1min = min(snake1.start.x, snake1.end.x)
    snake2min = min(snake2.start.x, snake2.end.x)
    if snake1min <= snake2min:
        start_snake = snake1
        end_snake = snake2
    else:
        start_snake = snake2
        end_snake = snake1

    start_snake_start = max(start_snake.start.x, start_snake.end.x)
    end_snake_start = min(end_snake.start.x, end_snake.end.x)
    return start_snake_start >= end_snake_start


def in_same_row(snake1, snake2):
    return snake1.start.x == snake2.start.x


def in_same_column(snake1, snake2):
    return snake1.start.y == snake2.start.y


def is_valid_same_row(snake1, snake2):
    snake1min = min(snake1.start.y, snake1.end.y)
    snake2min = min(snake2.start.y, snake2.end.y)
    if snake1min <= snake2min:
        start_snake = snake1
        end_snake = snake2
    else:
        start_snake = snake2
        end_snake = snake1
    start_snake_start = max(start_snake.start.y, start_snake.end.y)
    end_snake_start = min(end_snake.start.y, end_snake.end.y)
    return start_snake_start >= end_snake_start


def is_valid_diff_row_column(snake_in_row, snake_in_column):
    return snake_in_row.start == snake_in_column.start or snake_in_row.end == snake_in_column.start or \
           snake_in_row.start == snake_in_column.end or snake_in_row.end == snake_in_column.end


def same_snake(snake1, snake2):
    # Add snakes to the graph
    if in_row(snake1) and in_row(snake2):
        return in_same_row(snake1, snake2) and is_valid_same_row(snake1, snake2)
    elif not in_row(snake1) and not in_row(snake2):
        return in_same_column(snake1, snake2) and is_valid_same_column(snake1, snake2)
    else:
        if in_row(snake1):
            return is_valid_diff_row_column(snake1, snake2)
        else:
            return is_valid_diff_row_column(snake2, snake1)


T = int(raw_input())
for _ in xrange(T):
    graph = defaultdict(set)
    snake_vertices = {snake1_id: set(), snake2_id: set()}
    x1, y1, x2, y2 = map(int, raw_input().strip().split())
    snake1 = Snake(Point(x1, y1), Point(x2, y2))
    x1, y1, x2, y2 = map(int, raw_input().strip().split())
    snake2 = Snake(Point(x1, y1), Point(x2, y2))
    if same_snake(snake1, snake2):
        print "yes"
    else:
        print "no"

