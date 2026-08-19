from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)


def first_fit(items, capacity):
    bins = []

    for item in items:
        placed = False

        for b in bins:
            if b["remaining"] + 1e-9 >= item:
                b["items"].append(item)
                b["remaining"] -= item
                placed = True
                break

        if not placed:
            bins.append({
                "items": [item],
                "remaining": capacity - item
            })

    return bins


def first_fit_decreasing(items, capacity):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity):
    bins = []

    for item in sorted(items, reverse=True):
        best = None
        best_remaining = float("inf")

        for b in bins:
            remaining = b["remaining"]

            if remaining + 1e-9 >= item:
                leftover = remaining - item

                if leftover < best_remaining:
                    best_remaining = leftover
                    best = b

        if best:
            best["items"].append(item)
            best["remaining"] -= item
        else:
            bins.append({
                "items": [item],
                "remaining": capacity - item
            })

    return bins


def format_bins(bins, capacity):
    result = []

    for index, b in enumerate(bins, 1):
        used = sum(b["items"])

        result.append({
            "number": index,
            "items": [round(x, 2) for x in b["items"]],
            "used": round(used, 2),
            "remaining": round(b["remaining"], 2),
            "utilization": round((used / capacity) * 100, 1)
        })

    return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.get_json()

    try:
        items = [float(x) for x in data["items"]]
        capacity = float(data["capacity"])

        if not items or capacity <= 0:
            raise ValueError

        if any(x <= 0 or x > capacity for x in items):
            raise ValueError

        lower_bound = math.ceil(sum(items) / capacity - 1e-9)

        ff = first_fit(items, capacity)
        ffd = first_fit_decreasing(items, capacity)
        bfd = best_fit_decreasing(items, capacity)

        return jsonify({
            "items": items,
            "capacity": capacity,
            "total": round(sum(items), 2),
            "lower_bound": lower_bound,
            "algorithms": {
                "FF": {
                    "name": "First Fit",
                    "bins_used": len(ff),
                    "bins": format_bins(ff, capacity)
                },
                "FFD": {
                    "name": "First Fit Decreasing",
                    "bins_used": len(ffd),
                    "bins": format_bins(ffd, capacity)
                },
                "BFD": {
                    "name": "Best Fit Decreasing",
                    "bins_used": len(bfd),
                    "bins": format_bins(bfd, capacity)
                }
            }
        })

    except (ValueError, TypeError, KeyError):
        return jsonify({
            "error": "Please enter valid item weights and bin capacity."
        }), 400


if __name__ == "__main__":
    app.run(debug=True, port=5002)