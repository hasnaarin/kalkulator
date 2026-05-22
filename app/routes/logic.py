from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from datetime import datetime
from app.services.logic import calculate_bitwise

bp = Blueprint("logic", __name__, url_prefix="/logic")

def parse_int(val_str):
    try:
        return int(val_str)
    except (ValueError, TypeError):
        raise ValueError("Input harus berupa bilangan bulat (integer) yang valid.")

@bp.route("", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            operation = request.form.get("operation")
            a_str = request.form.get("a", "").strip()
            b_str = request.form.get("b", "").strip()

            if not operation:
                raise ValueError("Operator harus dipilih.")

            a = parse_int(a_str)
            b = None
            if operation != "NOT":
                b = parse_int(b_str)

            res_data = calculate_bitwise(a, b, operation)
            result = res_data

            if "history" not in session:
                session["history"] = []

            history_list = list(session["history"])
            history_list.append({
                "category": "Logika",
                "operation": res_data["operation"],
                "expression": res_data["expression"],
                "result": f"{res_data['result']} ({res_data['result_bin']})",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })

            if len(history_list) > 20:
                history_list.pop(0)

            session["history"] = history_list

        except Exception as e:
            flash(str(e), "error")

    return render_template("logic.html", result=result)

@bp.route("/clear-history", methods=["POST"])
def clear_history():
    session.pop("history", None)
    return redirect(url_for("logic.index"))
