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

def breadth_first(root, fn):
  q = [root]

  while q:
    current_node = q.pop(0)
    fn(current_node["value"])
    q += current_node["children"]

def depth_first_preorder(root, fn):
  s = [root]

  while s:
    current_node = s.pop(0)
    fn(current_node["value"])
    s = current_node["children"] + s

def depth_first_preorder_r(node, fn):
  fn(node["value"])

  if len(node["children"]):
    for child in node["children"]:
      depth_first_preorder_r(child, fn)

def depth_first_postorder(root, fn):
  stack = [root]
  visited = []

  while stack:
    current_node = stack[-1]
    if len(current_node["children"]) and current_node not in visited:
      stack += list(reversed(current_node["children"]))
      visited.append(current_node)
    else:
      fn(stack.pop()["value"])

def depth_first_postorder_r(node, fn):
  if len(node["children"]):
    for child in node["children"]:
      depth_first_postorder_r(child, fn)

  fn(node["value"])

depth_first_preorder_r(a, print)
