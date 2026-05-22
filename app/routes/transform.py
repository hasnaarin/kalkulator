from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from datetime import datetime
from app.services.transform import (
    convert_bases, convert_temperature, convert_currency,
    calculate_factorial, calculate_fibonacci
)

bp = Blueprint("transform", __name__, url_prefix="/transform")

@bp.route("", methods=["GET", "POST"])
def index():
    result = None
    sub_feature = request.args.get("tab", "base")
    
    if request.method == "POST":
        sub_feature = request.form.get("sub_feature", "base")
        try:
            if sub_feature == "base":
                val = request.form.get("val", "").strip()
                from_base = request.form.get("from_base", "DEC").strip()
                if not val:
                    raise ValueError("Input angka basis tidak boleh kosong.")
                res_data = convert_bases(val, from_base)
                result = {"type": "base", "data": res_data}
                expr = f"{val} ({from_base})"
                res_str = f"DEC:{res_data['dec']} BIN:{res_data['bin']} OCT:{res_data['oct']} HEX:{res_data['hex']}"
                op_name = "Konversi Basis"

            elif sub_feature == "temp":
                val_str = request.form.get("val", "").strip()
                from_unit = request.form.get("from_unit", "C").strip()
                if not val_str:
                    raise ValueError("Nilai suhu tidak boleh kosong.")
                try:
                    val = float(val_str)
                except ValueError:
                    raise ValueError("Input suhu harus berupa angka.")
                res_data = convert_temperature(val, from_unit)
                result = {"type": "temp", "data": res_data}
                expr = f"{val_str} °{from_unit}"
                res_str = f"{res_data['c']}°C, {res_data['f']}°F, {res_data['k']}K, {res_data['r']}°R"
                op_name = "Konversi Suhu"

            elif sub_feature == "currency":
                val_str = request.form.get("val", "").strip()
                if not val_str:
                    raise ValueError("Nominal IDR tidak boleh kosong.")
                try:
                    val = float(val_str)
                except ValueError:
                    raise ValueError("Input IDR harus berupa angka.")
                res_data = convert_currency(val)
                result = {"type": "currency", "data": res_data}
                expr = f"Rp {val:,.2f}"
                res_str = f"USD:{res_data['usd']} EUR:{res_data['eur']} SGD:{res_data['sgd']}"
                op_name = "Konversi Mata Uang"

            elif sub_feature == "factorial":
                val_str = request.form.get("val", "").strip()
                if not val_str:
                    raise ValueError("Nilai n faktorial tidak boleh kosong.")
                try:
                    val = int(val_str)
                except ValueError:
                    raise ValueError("Input n faktorial harus berupa bilangan bulat.")
                res_data = calculate_factorial(val)
                result = {"type": "factorial", "data": res_data}
                expr = f"{val}!"
                res_str = f"{res_data['result']}"
                op_name = "Faktorial"

            elif sub_feature == "fibonacci":
                val_str = request.form.get("val", "").strip()
                if not val_str:
                    raise ValueError("Jumlah deret Fibonacci tidak boleh kosong.")
                try:
                    val = int(val_str)
                except ValueError:
                    raise ValueError("Input jumlah deret harus berupa bilangan bulat.")
                res_data = calculate_fibonacci(val)
                result = {"type": "fibonacci", "data": res_data}
                expr = f"Fibonacci ({val})"
                res_str = res_data["result_str"]
                if len(res_str) > 40:
                    res_str = res_str[:37] + "..."
                op_name = "Fibonacci"
            else:
                raise ValueError("Sub-fitur tidak dikenal.")

            if "history" not in session:
                session["history"] = []

            history_list = list(session["history"])
            history_list.append({
                "category": "Transformasi",
                "operation": op_name,
                "expression": expr,
                "result": res_str,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })

            if len(history_list) > 20:
                history_list.pop(0)

            session["history"] = history_list

        except Exception as e:
            flash(str(e), "error")

    return render_template("transform.html", result=result, active_tab=sub_feature)

@bp.route("/clear-history", methods=["POST"])
def clear_history():
    session.pop("history", None)
    return redirect(url_for("transform.index"))
