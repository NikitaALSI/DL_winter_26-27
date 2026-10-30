from ...dl_lib.engine.value import Value


def main():
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    a_p_b = a + b
    a_m_b = a * b
    a_m_b_p_c = a * b + c

    print(a, b, c, 
          f"a + b  = {a_p_b}",
          f"a * b  = {a_m_b}",
          f"a * b + c = {a_m_b_p_c}",
          sep="\n")
    
    return 0