def create_binary(filename):
    n = []
    try:
      f =  open('a.py', 'rb')
      lines = b''.join(f.readlines())
      for i in range(0, len(lines), 16):
            n.append(lines[i:i+16])
    except FileNotFoundError:
         print(f"No such file: a.py")
    return n

def create_hex(lines: list):
    n = 0
    for line in lines:
          hex_ = line.hex(' ', 2)
          line = line.decode().replace("\n", ".")
          print(f"{n * 16:08x} : {hex_} : {line}")
          n = n+1
lines = create_binary('a.py')
create_hex(lines)
