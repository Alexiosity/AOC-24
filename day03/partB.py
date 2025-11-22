import re
import partA

def parse_input(raw_data):
  """
  This is broadly similar to part A, but there are also instructions of the form "do()" and "don't()"
  Any 'mul's after a 'don't' are ignored until another 'do' is encountered.
  So this parsing first splits the data on each 'do' and then 'don't' to find all sequences that still matter.
  """

  pure_do_blocks = []

  # Each block starts with a 'do' except the first, which is allowed by the spec
  split_by_do = re.split("do\(\)", raw_data)

  for block in split_by_do:
    # Only split once, as any more 'don't' blocks after the first don't change anything
    split_first_dont = re.split("don\'t\(\)", block, 1)
    pure_do_blocks.append(split_first_dont[0]) # only take the first block (after a 'do' and before any more 'don't's)
  
  int_pairs = []
  for do_str in pure_do_blocks:
    int_pairs += partA.parse_input(do_str) # Each string that still counts can be parsed individually just as in part A
  return int_pairs

def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    raw = f.read()
  
  int_pairs = parse_input(raw)
  
  # Score is (still) the sum of the product of each pair
  score = sum(a * b for a, b in int_pairs)
  print(f"Score: {score}")

if __name__ == "__main__":
  main()