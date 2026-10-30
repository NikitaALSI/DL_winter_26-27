from dl_lib.engine.value import Value


def main():
    a = Value(10.0)
    b = Value(-6.0)
    d = a + b
    print(d,
          f"d._op = '{d._op}'",
          f"d._prev = {[x.data for x in d._prev]}",
          sep="\n")
    
    a = Value(2.0)
    b = Value(-3.0)
    e = a * b
    print(e,
          f"e._op = '{e._op}'",
          f"e._prev = {[x.data for x in e._prev]}",
          sep="\n")

    return 0
