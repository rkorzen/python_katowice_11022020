import sys
print(sys.path)
import a

print(dir(a))
a.hello()

from a import hello as helloa
from c import hello
helloa()
hello()
