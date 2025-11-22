from partA import parse_input, is_safe

def is_safe_enough(report: list):
  """
  A report can be considered safe if it is safe, or if removing one value can produce a safe report
  """

  if is_safe(report): return True

  # Very bad and slow method but does work
  for i in range(len(report)):
    partial = report.copy() # shallow copy allowed because ints are primitives
    partial.pop(i)
    if is_safe(partial): return True
  return False

def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    lines = f.readlines()
  
  reports = parse_input(lines)

  safe_ish_reports = [r for r in reports if is_safe_enough(r)]
  score = len(safe_ish_reports)

  print(f"Score: {score}")

if __name__ == "__main__":
  main()