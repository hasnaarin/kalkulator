def to_bin_padded(val, bits):
    if val >= 0:
        return f"{val:0{bits}b}"
    return bin((1 << bits) + val)[2:]

def get_truth_table(op):
    if op == "AND":
        return [
            {"a": 0, "b": 0, "res": 0},
            {"a": 0, "b": 1, "res": 0},
            {"a": 1, "b": 0, "res": 0},
            {"a": 1, "b": 1, "res": 1}
        ]
    elif op == "OR":
        return [
            {"a": 0, "b": 0, "res": 0},
            {"a": 0, "b": 1, "res": 1},
            {"a": 1, "b": 0, "res": 1},
            {"a": 1, "b": 1, "res": 1}
        ]
    elif op == "XOR":
        return [
            {"a": 0, "b": 0, "res": 0},
            {"a": 0, "b": 1, "res": 1},
            {"a": 1, "b": 0, "res": 1},
            {"a": 1, "b": 1, "res": 0}
        ]
    elif op == "NAND":
        return [
            {"a": 0, "b": 0, "res": 1},
            {"a": 0, "b": 1, "res": 1},
            {"a": 1, "b": 0, "res": 1},
            {"a": 1, "b": 1, "res": 0}
        ]
    elif op == "NOR":
        return [
            {"a": 0, "b": 0, "res": 1},
            {"a": 0, "b": 1, "res": 0},
            {"a": 1, "b": 0, "res": 0},
            {"a": 1, "b": 1, "res": 0}
        ]
    elif op == "NOT":
        return [
            {"a": 0, "res": 1},
            {"a": 1, "res": 0}
        ]
    return []

def calculate_bitwise(a, b, op):
    if a < 0 or (b is not None and b < 0):
        raise ValueError("Operasi logika bitwise hanya mendukung bilangan integer non-negatif.")

    bits = max(8, a.bit_length(), b.bit_length() if b is not None else 0)

    a_bin = to_bin_padded(a, bits)
    b_bin = to_bin_padded(b, bits) if b is not None else ""

    if op == "AND":
        res_val = a & b
        symbol = "&"
    elif op == "OR":
        res_val = a | b
        symbol = "|"
    elif op == "XOR":
        res_val = a ^ b
        symbol = "^"
    elif op == "NOT":
        res_val = ~a & ((1 << bits) - 1)
        symbol = "~"
    elif op == "NAND":
        res_val = ~(a & b) & ((1 << bits) - 1)
        symbol = "NAND"
    elif op == "NOR":
        res_val = ~(a | b) & ((1 << bits) - 1)
        symbol = "NOR"
    else:
        raise ValueError("Operator logika tidak dikenal.")

    res_bin = to_bin_padded(res_val, bits)

    steps = []
    if op == "NOT":
        steps.append(f"Representasi biner A ({a}) = {a_bin}")
        steps.append(f"Lakukan operasi NOT (pembalikan bit) pada setiap posisi bit A.")
        bit_steps = []
        for i in range(bits):
            bit_a = a_bin[i]
            bit_res = "1" if bit_a == "0" else "0"
            bit_steps.append(f"Bit posisi {bits - 1 - i} (terkanan ke-{i}): NOT {bit_a} = {bit_res}")
        steps.extend(bit_steps)
    else:
        steps.append(f"Representasi biner A ({a}) = {a_bin}")
        steps.append(f"Representasi biner B ({b}) = {b_bin}")
        steps.append(f"Lakukan operasi bitwise {op} pada setiap kolom bit sejajar.")
        bit_steps = []
        for i in range(bits):
            bit_a = a_bin[i]
            bit_b = b_bin[i]
            if op == "AND":
                bit_res = "1" if bit_a == "1" and bit_b == "1" else "0"
            elif op == "OR":
                bit_res = "1" if bit_a == "1" or bit_b == "1" else "0"
            elif op == "XOR":
                bit_res = "1" if bit_a != bit_b else "0"
            elif op == "NAND":
                bit_res = "0" if bit_a == "1" and bit_b == "1" else "1"
            elif op == "NOR":
                bit_res = "0" if bit_a == "1" or bit_b == "1" else "1"
            bit_steps.append(f"Bit posisi {bits - 1 - i}: {bit_a} {symbol} {bit_b} = {bit_res}")
        steps.extend(bit_steps)

    return {
        "result": res_val,
        "result_bin": res_bin,
        "a_bin": a_bin,
        "b_bin": b_bin,
        "truth_table": get_truth_table(op),
        "steps": steps,
        "operation": f"Bitwise {op}",
        "expression": f"~{a}" if op == "NOT" else f"{a} {symbol} {b}"
    }
