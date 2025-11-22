
def parse_input(lines):
  """
  The input for this is a number of lines of the form: "[num_a][spaces][num_b]"
  This gets parsed into two lists, one for each column, all converted to ints.
  """
  
  list_a, list_b = [], []
  for i in range(len(lines)):
    num_strs = lines[i].split()

    a, b = num_strs
    list_a.append(int(a))
    list_b.append(int(b))
  
  return list_a, list_b

def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    lines = f.readlines()
  
  list_a, list_b = parse_input(lines)

  # sort both lists so that a pairwise iteration (or zip) matches the nth smallest of both lists together
  list_a.sort()
  list_b.sort()

  # zip the lists together, map each pair to its abolute difference, and sum for the final score
  combined = zip(list_a, list_b)
  diffs = map(lambda pair: abs(pair[0] - pair[1]), combined)
  score = sum(diffs)

  print(f"Score: {score}")

if __name__ == "__main__":
  main()