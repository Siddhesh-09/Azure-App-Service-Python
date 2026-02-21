from flask import Flask, request, jsonify
import tomllib

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Python 3.14 demo helpers
# ---------------------------------------------------------------------------

def compute_operation(op: str, a: float, b: float) -> float | None:
    """Perform a simple math operation using `match` (Python 3.14 feature).

    The return type uses the new union operator (`|`) for types, which has
    been available since 3.10 but is normal in 3.14 code.  We also show a
    ``match``/``case`` block with fallthrough-like behaviour for unknown ops.
    """
    match op:
        case "add":
            return a + b
        case "sub":
            return a - b
        case "mul":
            return a * b
        case "div":
            return a / b if b != 0 else None
        case _:
            raise ValueError(f"Unknown operation: {op}")

# Load configuration from a TOML file using the built-in tomllib.
# ``tomllib`` arrived in Python 3.11, but Python 3.14 lets us rely on it
# without any backports.
try:
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)
except FileNotFoundError:
    config = {"app": {"name": "unknown", "version": "0.0.0"}}

@app.route("/")
def index():
    name = config.get("app", {}).get("name", "webapp")
    return f"Hello from {name} running on Python 3.14!"

@app.route("/calc")
def calc():
    op = request.args.get("op", "add")
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        result = compute_operation(op, a, b)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # debug=True for local development only; Azure App Service will set
    # ``FLASK_ENV`` or ``DEBUG`` as appropriate.
    app.run(host="0.0.0.0", port=8000, debug=True)
