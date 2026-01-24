import collections

in_fn = input
op_fn = print

stats = []
for _ in range(3):
    line = input()
    stats.append(line.strip())

great_map = collections.defaultdict(set)
alphas = set()
def process(s: str):
    if s[1] >= ">":
        great_map[s[2]].add(s[0])
    else:
        great_map[s[0]].add(s[2])
    alphas.add(s[0])
    alphas.add(s[2])

for s in stats:
    process(s)

rev_map = {len(v): k for k, v in great_map.items()}
if len(rev_map) != 2:
    op_fn("Impossible")
else:
    op_fn(rev_map[2] + rev_map[1] + list(alphas - {rev_map[2], rev_map[1]})[0])
