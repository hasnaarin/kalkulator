from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from datetime import datetime
from app.services.arithmetic import (
    calculate_add, calculate_subtract, calculate_multiply,
    calculate_divide, calculate_power, calculate_sqrt,
    calculate_mod, calculate_floor_divide
)

bp = Blueprint("arithmetic", __name__, url_prefix="/arithmetic")

def parse_number(val_str):
    try:
        val = float(val_str)
        if val.is_integer():
            return int(val)
        return val
    except (ValueError, TypeError):
        raise ValueError("Input harus berupa angka valid.")

@bp.route("", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            operation = request.form.get("operation")
            a_str = request.form.get("a", "").strip()
            b_str = request.form.get("b", "").strip()

            if not operation:
                raise ValueError("Operasi harus dipilih.")

            a = parse_number(a_str)
            b = None
            if operation != "sqrt":
                b = parse_number(b_str)

            if operation == "add":
                res_data = calculate_add(a, b)
            elif operation == "subtract":
                res_data = calculate_subtract(a, b)
            elif operation == "multiply":
                res_data = calculate_multiply(a, b)
            elif operation == "divide":
                res_data = calculate_divide(a, b)
            elif operation == "power":
                res_data = calculate_power(a, b)
            elif operation == "sqrt":
                res_data = calculate_sqrt(a)
            elif operation == "mod":
                res_data = calculate_mod(a, b)
            elif operation == "floor_divide":
                res_data = calculate_floor_divide(a, b)
            else:
                raise ValueError("Operasi tidak dikenal.")

            result = res_data

            if "history" not in session:
                session["history"] = []

            history_list = list(session["history"])
            history_list.append({
                "category": "Aritmatika",
                "operation": res_data["operation"],
                "expression": res_data["formula"].split("=")[0].strip(),
                "result": str(res_data["result"]),
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })

            if len(history_list) > 20:
                history_list.pop(0)

            session["history"] = history_list

        except Exception as e:
            flash(str(e), "error")

    return render_template("arithmetic.html", result=result)

@bp.route("/clear-history", methods=["POST"])
def clear_history():
    session.pop("history", None)
    return redirect(url_for("arithmetic.index"))
