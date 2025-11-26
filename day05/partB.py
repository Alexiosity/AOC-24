
from collections import defaultdict

def parse_input(lines):
  order_rules = defaultdict(set)
  sep_line_num = -1
  for i, line in enumerate(lines):
    if len(line) < 3:
      sep_line_num = i
      break
    else:
      pre, post = line.strip().split('|')
      pre = int(pre)
      post = int(post)
      order_rules[pre].add(post)
  
  if sep_line_num == -1: raise ValueError("I don't know where to start looking for page lists")
  
  manuals = []
  for i in range(sep_line_num+1, len(lines)):
    manuals.append(tuple(int(n) for n in lines[i].strip().split(',')))
  
  return order_rules, manuals

def is_valid_manual(rules, manual):
  """
  Return whether the given pages follow the rules about relative order
  """

  for i, page in enumerate(manual):
    if any(manual[j] in rules[page] for j in range(i)): return False
  return True

def fix_manual_rec(rules, manual):
  """
  Given an invalid manual, yield a sequence of manuals with pages swapped
  so that the rules are followed.
  Hopefully this is a singleton sequence, 
  """

  # helper to test whether a page can go before all others in its manual
  can_be_first = lambda page: all(page not in rules[pre] for pre in manual)
  
  heads = [page for page in manual if can_be_first(page)]
  if len(heads) != 1: raise(Exception(f"Wrong number of heads ({len(heads)}) in {manual}"))
  for head in heads:

    # clone manual and remove head, giving all values in corresponding tail
    tail_pages = [page for page in manual if page != head]

    if len(tail_pages) == 1: # Base case, trivially return the last element in a list
      yield tail_pages
    else:  
      # Recurse to find all possible tails
      tails = fix_manual_rec(rules, tail_pages)

      # Build back up feasible results
      for tail in tails:
        yield [head] + tail

def fix_manual(rules, manual):
  all_fixed = list(fix_manual_rec(rules, manual)) # Exhaust generator 
  if len(all_fixed) != 1: raise Exception(f"Fix of manual: {manual} not unique")
  return all_fixed[0]


def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    lines = f.readlines()
  order_rules, manuals = parse_input(lines)
  
  incorrect_manuals = [manual for manual in manuals if not is_valid_manual(order_rules, manual)]
  corrected_manuals = [fix_manual(order_rules, manual) for manual in incorrect_manuals]
  middle_pages = [manual[len(manual)//2] for manual in corrected_manuals]

  score = sum(middle_pages)
  print(f"Score: {score}")


if __name__ == "__main__":
  main()