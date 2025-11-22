import re

def parse_input(raw_data):
  """
  The input is a single string containing a lot of bad data,
  Within the string, there are sequences of the form "mul([int],[int])" where each int is 1 to 3 chars long.
  These 'mul' sections are the only relevant data, and a list of the pairs of ints within is cast and returned.
  """
  
  # Extract the integer pairs from within valid 'mul' instances
  pairs_as_strs = re.findall("mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)", raw_data)

  # Cast to pairs of ints
  parsed = map(lambda p: (int(p[0]), int(p[1])), pairs_as_strs)

  return parsed


def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    raw = f.read()
  
  int_pairs = parse_input(raw)

  # Score is the sum of the product of each pair
  score = sum(a * b for a, b in int_pairs)

  print(f"Score: {score}")

if __name__ == "__main__":
  main()