import sys

PY3 = sys.version_info[0] == 3

def b(s):
  if PY3:
    if type(s) == bytes:
      return s
    else:
      return string.encode('latin-1')
  else:
    return string