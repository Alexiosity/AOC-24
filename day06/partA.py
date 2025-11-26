from time import sleep # only needed to have some delay when showing the progress with pretty-printing

def parse_input(grid):
  """
  Only finding positions of guard and obstacles
  """
  guard = (-1, -1, -1)
  obstacles = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] in "^>v<":
        guard = (row, col, "^>v<".index(grid[row][col]))
      if grid[row][col] == '#':
        obstacles.append( (row, col) )
  return guard, obstacles

def next_pos(row, col, direction):
  if direction == 0: return row - 1, col
  if direction == 1: return row    , col + 1
  if direction == 2: return row + 1, col
  if direction == 3: return row    , col - 1

def print_curr_grid(grid, guard, places_walked):
  """
  Pretty print current state of the grid
  Calling this at each step of the main loop shows the progression
  """
  DELAY_S = 0.2

  r, c, d = guard

  sleep(DELAY_S)

  print('+' + '-' * len(grid) + '+')
  for row in range(len(grid)):
    print('|', end='')
    for col in range(len(grid[0])):
      if (row, col) == (r, c):
        print("^>v<"[d], end='')
      elif (row, col) in places_walked:
        print('X', end='')
      else:
        print(grid[row][col], end='')
    print('|')
  print('+' + '-' * len(grid) + '+')
      
def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    grid = [line.strip() for line in f.readlines()]
  guard, obstacles = parse_input(grid)
  r, c, d = guard

  # Is the guard still around
  in_grid = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])

  places_walked = set()
  while in_grid(r, c):
    if next_pos(r, c, d) in obstacles:
      d = (d + 1) % 4 # turn right
    else:
      places_walked.add( (r, c) )
      r, c = next_pos(r, c, d)
    # print_curr_grid(grid, (r, c, d), places_walked)

  score = len(places_walked)
  print(f"Score: {score}")


if __name__ == "__main__":
  main()