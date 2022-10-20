def order_m(num: int) -> int:
  num = abs(num)
  order = -1
  while num:
    order += 1
    num //= 10
  return order

## also for positive #s:
num = 1000
import math # or whatever
order = math.trunc(math.log10(num))