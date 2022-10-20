from types import NoneType
from get_order_magnitude import order_m


def intmap_r2l(num: int, f: function) -> NoneType:
  sign = -1 if num < 0 else 1
  num = abs(num)
  while num:
    num, remainder = divmod(num, 10)
    f(remainder * sign)

def intmap_l2r(num: int, f: function) -> NoneType:
  order = order_m(num) + 1
  sign = -1 if num < 0 else 1
  num = abs(num)
  while order:
    order -= 1
    f((num // (10**order) % 10) * sign)