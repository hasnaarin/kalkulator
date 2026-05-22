import math

def calculate_add(a, b):
    result = a + b
    return {
        "result": result,
        "formula": f"{a} + {b} = {result}",
        "steps": [
            f"Identifikasi nilai input pertama a = {a} dan input kedua b = {b}.",
            f"Lakukan operasi penjumlahan antara {a} dan {b}.",
            f"Diperoleh hasil akhir penjumlahan sebesar {result}."
        ],
        "operation": "Penjumlahan"
    }

def calculate_subtract(a, b):
    result = a - b
    return {
        "result": result,
        "formula": f"{a} - {b} = {result}",
        "steps": [
            f"Identifikasi nilai input pertama a = {a} dan input kedua b = {b}.",
            f"Kurangkan nilai b ({b}) dari nilai a ({a}).",
            f"Diperoleh hasil akhir pengurangan sebesar {result}."
        ],
        "operation": "Pengurangan"
    }

def calculate_multiply(a, b):
    result = a * b
    return {
        "result": result,
        "formula": f"{a} × {b} = {result}",
        "steps": [
            f"Identifikasi nilai input pertama a = {a} dan input kedua b = {b}.",
            f"Lakukan operasi perkalian antara nilai {a} dengan {b}.",
            f"Diperoleh hasil akhir perkalian sebesar {result}."
        ],
        "operation": "Perkalian"
    }

def calculate_divide(a, b):
    if b == 0:
        raise ValueError("Pembagi tidak boleh bernilai nol.")
    result = a / b
    return {
        "result": result,
        "formula": f"{a} ÷ {b} = {result}",
        "steps": [
            f"Identifikasi nilai pembilang a = {a} dan penyebut b = {b}.",
            f"Pastikan bahwa penyebut b ({b}) tidak sama dengan nol untuk menghindari pembagian tidak terdefinisi.",
            f"Lakukan pembagian nilai {a} dengan {b} untuk mendapatkan hasil {result}."
        ],
        "operation": "Pembagian"
    }

def calculate_power(a, b):
    result = math.pow(a, b)
    if result.is_integer():
        result = int(result)
    return {
        "result": result,
        "formula": f"{a}^{b} = {result}",
        "steps": [
            f"Identifikasi nilai bilangan pokok a = {a} dan pangkat b = {b}.",
            f"Lakukan perpangkatan dengan mengalikan bilangan {a} sebanyak {b} kali.",
            f"Diperoleh hasil pangkat sebesar {result}."
        ],
        "operation": "Pangkat"
    }

def calculate_sqrt(a):
    if a < 0:
        raise ValueError("Nilai di dalam akar kuadrat tidak boleh bernilai negatif.")
    result = math.sqrt(a)
    if result.is_integer():
        result = int(result)
    return {
        "result": result,
        "formula": f"√{a} = {result}",
        "steps": [
            f"Identifikasi bilangan input a = {a}.",
            f"Pastikan bilangan {a} bernilai non-negatif agar dapat dihitung akar kuadratnya dalam bilangan riil.",
            f"Hitung nilai akar kuadrat dari {a} dan dapatkan hasil {result}."
        ],
        "operation": "Akar Kuadrat"
    }

def calculate_mod(a, b):
    if b == 0:
        raise ValueError("Pembagi modulus tidak boleh bernilai nol.")
    result = a % b
    return {
        "result": result,
        "formula": f"{a} % {b} = {result}",
        "steps": [
            f"Identifikasi nilai bilangan yang dibagi a = {a} dan pembagi b = {b}.",
            f"Lakukan pembagian bulat {a} oleh {b} untuk mengetahui sisa hasil baginya.",
            f"Diperoleh sisa hasil pembagian (modulus) sebesar {result}."
        ],
        "operation": "Modulus"
    }

def calculate_floor_divide(a, b):
    if b == 0:
        raise ValueError("Pembagi floor division tidak boleh bernilai nol.")
    result = a // b
    return {
        "result": result,
        "formula": f"{a} // {b} = {result}",
        "steps": [
            f"Identifikasi nilai bilangan yang dibagi a = {a} dan pembagi b = {b}.",
            f"Lakukan pembagian {a} dibagi {b} kemudian bulatkan hasilnya ke arah bawah (bilangan bulat terdekat).",
            f"Diperoleh hasil pembagian bulat (floor division) sebesar {result}."
        ],
        "operation": "Floor Division"
    }
