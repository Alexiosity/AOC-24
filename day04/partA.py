"""
Strategy: Loop through grid, and at each 'X' check how many "XMAS"s can be found in the eight allowed directions,
incrementing score appropriately
"""


# No real parsing needed today

def check_xmases(grid, row, col):
  """
  Given the row and col coords of an 'X', return how many valid "XMAS"s exist starting there.
  """
  xmas_str = "XMAS"

  # Pretend enum for a list of is_valid flags using compass dirs
  N, NE, E, SE, S, SW, W, NW = range(8)
  is_valid = [True] * 8

  # Bound and char match tests
  in_bounds = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
  correct_char = lambda r, c, i: grid[r][c] == xmas_str[i]

  num_valid = 0

  # Count through the tail letters of XMAS, in each direction
  for i in range(1, len(xmas_str)):
    # N
    r = row - i
    c = col
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[N] = False
    # NE
    r = row - i
    c = col + i
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[NE] = False
    # E
    r = row
    c = col + i
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[E] = False
    # SE
    r = row + i
    c = col + i
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[SE] = False
    # S
    r = row + i
    c = col
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[S] = False
    # SW
    r = row + i
    c = col - i
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[SW] = False
    # W
    r = row
    c = col - i
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[W] = False
    # NW
    r = row - i
    c = col - i
    if not in_bounds(r, c) or not correct_char(r, c, i): is_valid[NW] = False
  
  for flag in is_valid:
    if flag: num_valid += 1
  
  return num_valid


def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    grid = f.readlines()

  score = 0
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == 'X':
        score += check_xmases(grid, row, col)

  print(f"Score: {score}")



if __name__ == "__main__":
  main()