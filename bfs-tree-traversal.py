def node(value):
  return {
    "value": value,
    "children": [],
  }

a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')
g = node('g')
h = node('h')
i = node('i')
j = node('j')
k = node('k')
l = node('l')
m = node('m')

a["children"] += [b, c, d]
b["children"] += [e]
e["children"] += [k, l]
c["children"] += [f, g, h]
h["children"] += [m]
d["children"] += [i, j]

def breadth_first_print(root, fn):
  q = [root]

  while q:
    current_node = q.pop(0)
    fn(current_node["value"])
    q += current_node["children"]

breadth_first_print(a, print)
