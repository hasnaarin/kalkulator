CURRENCY_RATES = {
    "USD": 16000.0,
    "EUR": 17200.0,
    "SGD": 11800.0,
    "MYR": 3400.0,
    "JPY": 100.0
}

def convert_bases(val_str, from_base):
    val_str = val_str.strip().upper()
    try:
        if from_base == "DEC":
            dec_val = int(val_str, 10)
        elif from_base == "BIN":
            dec_val = int(val_str, 2)
        elif from_base == "OCT":
            dec_val = int(val_str, 8)
        elif from_base == "HEX":
            dec_val = int(val_str, 16)
        else:
            raise ValueError("Basis asal tidak didukung.")
    except ValueError:
        raise ValueError("Format input tidak sesuai dengan basis asal yang dipilih.")

    bin_res = bin(dec_val)[2:]
    oct_res = oct(dec_val)[2:]
    hex_res = hex(dec_val)[2:].upper()

    steps = []
    steps.append(f"1. Konversi input ke Desimal (DEC): {val_str} ({from_base}) = {dec_val} (DEC)")
    
    steps.append(f"2. Langkah konversi Desimal ({dec_val}) ke Biner (BIN) dengan pembagian berulang:")
    bin_steps = []
    temp = dec_val
    if temp == 0:
        bin_steps.append("0 / 2 = 0 sisa 0")
    else:
        while temp > 0:
            bin_steps.append(f"{temp} / 2 = {temp // 2} sisa {temp % 2}")
            temp = temp // 2
    steps.extend(bin_steps)
    steps.append(f"Hasil Biner (dari sisa bawah ke atas): {bin_res}")

    steps.append(f"3. Langkah konversi Desimal ({dec_val}) ke Oktal (OCT) dengan pembagian berulang:")
    oct_steps = []
    temp = dec_val
    if temp == 0:
        oct_steps.append("0 / 8 = 0 sisa 0")
    else:
        while temp > 0:
            oct_steps.append(f"{temp} / 8 = {temp // 8} sisa {temp % 8}")
            temp = temp // 8
    steps.extend(oct_steps)
    steps.append(f"Hasil Oktal (dari sisa bawah ke atas): {oct_res}")

    steps.append(f"4. Langkah konversi Desimal ({dec_val}) ke Heksadesimal (HEX) dengan pembagian berulang:")
    hex_steps = []
    temp = dec_val
    if temp == 0:
        hex_steps.append("0 / 16 = 0 sisa 0")
    else:
        while temp > 0:
            r = temp % 16
            r_str = str(r) if r < 10 else f"{r} ({chr(55 + r)})"
            hex_steps.append(f"{temp} / 16 = {temp // 16} sisa {r_str}")
            temp = temp // 16
    steps.extend(hex_steps)
    steps.append(f"Hasil Heksadesimal (dari sisa bawah ke atas): {hex_res}")

    return {
        "dec": str(dec_val),
        "bin": bin_res,
        "oct": oct_res,
        "hex": hex_res,
        "steps": steps
    }

def convert_temperature(val, from_unit):
    if from_unit == "C":
        c_val = val
    elif from_unit == "F":
        c_val = (val - 32) * 5/9
    elif from_unit == "K":
        c_val = val - 273.15
    elif from_unit == "R":
        c_val = val * 5/4
    else:
        raise ValueError("Satuan suhu asal tidak didukung.")

    res_c = c_val
    res_f = c_val * 9/5 + 32
    res_k = c_val + 273.15
    res_r = c_val * 4/5

    def clean_float(num):
        num = round(num, 4)
        if num.is_integer():
            return int(num)
        return num

    formulas = [
        f"Celsius (C) = {clean_float(res_c)} °C",
        f"Fahrenheit (F) = (Celsius × 9/5) + 32 = {clean_float(res_f)} °F",
        f"Kelvin (K) = Celsius + 273.15 = {clean_float(res_k)} K",
        f"Reamur (R) = Celsius × 4/5 = {clean_float(res_r)} °R"
    ]

    return {
        "c": clean_float(res_c),
        "f": clean_float(res_f),
        "k": clean_float(res_k),
        "r": clean_float(res_r),
        "formulas": formulas
    }

def convert_currency(idr_amount):
    if idr_amount < 0:
        raise ValueError("Nominal IDR tidak boleh negatif.")

    usd_val = idr_amount / CURRENCY_RATES["USD"]
    eur_val = idr_amount / CURRENCY_RATES["EUR"]
    sgd_val = idr_amount / CURRENCY_RATES["SGD"]
    myr_val = idr_amount / CURRENCY_RATES["MYR"]
    jpy_val = idr_amount / CURRENCY_RATES["JPY"]

    rates_info = [
        f"1 USD = Rp {int(CURRENCY_RATES['USD']):,}",
        f"1 EUR = Rp {int(CURRENCY_RATES['EUR']):,}",
        f"1 SGD = Rp {int(CURRENCY_RATES['SGD']):,}",
        f"1 MYR = Rp {int(CURRENCY_RATES['MYR']):,}",
        f"1 JPY = Rp {int(CURRENCY_RATES['JPY']):,}"
    ]

    return {
        "usd": round(usd_val, 4),
        "eur": round(eur_val, 4),
        "sgd": round(sgd_val, 4),
        "myr": round(myr_val, 4),
        "jpy": round(jpy_val, 4),
        "rates": rates_info
    }

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Nilai n faktorial tidak boleh negatif.")
    if n > 100:
        raise ValueError("Nilai n terlalu besar untuk dihitung (maksimal 100).")

    res = 1
    mult_str_list = []
    for i in range(n, 0, -1):
        res *= i
        mult_str_list.append(str(i))

    if n == 0:
        formula_str = "0! = 1"
    else:
        formula_str = f"{n}! = " + " × ".join(mult_str_list) + f" = {res:,}"

    return {
        "result": res,
        "formula": formula_str,
        "steps": [
            f"Faktorial dilambangkan dengan n! yang berarti mengalikan bilangan bulat n dengan bilangan di bawahnya hingga 1.",
            f"Perkalian berulang: " + " × ".join(mult_str_list) if n > 0 else "0! didefinisikan sebagai 1",
            f"Diperoleh hasil akhir sebesar {res}."
        ]
    }

def calculate_fibonacci(n):
    if n <= 0:
        raise ValueError("Jumlah deret Fibonacci harus lebih besar dari 0.")
    if n > 100:
        raise ValueError("Jumlah deret terlalu besar untuk dihitung (maksimal 100).")

    sequence = []
    steps = []
    
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        if i == 0:
            steps.append("Suku ke-1 (F0) = 0")
        elif i == 1:
            steps.append("Suku ke-2 (F1) = 1")
        else:
            steps.append(f"Suku ke-{i+1} (F{i}) = F{i-1} + F{i-2} = {sequence[-2]} + {sequence[-3]} = {a}")
        a, b = b, a + b

    seq_str = ", ".join(map(str, sequence))
    return {
        "sequence": sequence,
        "result_str": seq_str,
        "steps": steps
    }
