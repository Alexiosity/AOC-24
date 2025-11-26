"""
Need to find X-MASes, like:

M.S      M.M      S.M      S.S      
.A.  or  .A.  or  .A.  or  .A.
M.S      S.S      S.M      M.M

So, will find all A's with only Ms and Ss in the corners, and check which of those have valid placements
"""

def parse_input(lines):
  return [line.strip() for line in lines]

def check_for_cross_shape(grid, row, col):
  """
  Given a grid and position within it, return whether the corners around this centre is valid
  a valid cross shape must have two M corners and two S corners, and these must be consecutive (like m s m s would be invalid).
  """
  offsets = ((-1, -1,), (-1, 1), (1, 1), (1, -1))

  m_count = 0
  s_count = 0
  chars = []
  for roff, coff in offsets:
    targeted_char = grid[row + roff][col + coff]
    
    chars.append(targeted_char)
    if targeted_char == 'M':
      m_count += 1
    elif targeted_char == 'S':
      s_count += 1
    else:
      return False # All corners must be M and S, anything else fails early
    
  # A valid X-MAS must have 2 each of Ms and Ss, and must be next to each other
  return m_count == s_count == 2 and (chars[0] == chars[1] or chars[1] == chars[2])



def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    grid = f.readlines()
  grid = parse_input(grid)

  score = 0

  # Iterate through the possible "middles" which must be the char 'A'
  for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[row]) - 1):
      if grid[row][col] == 'A':
        # Only worth checking for the cross when an 'A' in the middle is found
        if check_for_cross_shape(grid, row, col): score += 1 
  
  print(f"Score: {score}")

if __name__ == "__main__":
  main()