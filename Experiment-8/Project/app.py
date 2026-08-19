from flask import Flask, render_template, request, jsonify
from itertools import permutations
import time

app = Flask(__name__)


def tsp_brute_force(cost):
    n = len(cost)
    cities = list(range(1, n))

    best_cost = float("inf")
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        current_cost = sum(
            cost[path[i]][path[i + 1]]
            for i in range(n)
        )

        if current_cost < best_cost:
            best_cost = current_cost
            best_path = path

    return best_path, best_cost


def validate_matrix(matrix):
    n = len(matrix)

    if n < 2 or n > 8:
        raise ValueError("Please provide between 2 and 8 cities.")

    if any(len(row) != n for row in matrix):
        raise ValueError("The cost matrix must be square.")

    for i in range(n):
        if matrix[i][i] != 0:
            raise ValueError("Diagonal values must be 0.")

        for j in range(n):
            if matrix[i][j] < 0:
                raise ValueError("Costs cannot be negative.")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():
    try:
        data = request.get_json()
        matrix = data.get("matrix", [])

        validate_matrix(matrix)

        start = time.perf_counter()

        path, minimum_cost = tsp_brute_force(matrix)

        elapsed_ms = (time.perf_counter() - start) * 1000

        cities = [chr(65 + i) for i in range(len(matrix))]

        route = [cities[i] for i in path]

        verification = []

        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]

            verification.append({
                "from": cities[u],
                "to": cities[v],
                "cost": matrix[u][v]
            })

        return jsonify({
            "success": True,
            "route": route,
            "cost": minimum_cost,
            "time_ms": round(elapsed_ms, 4),
            "verification": verification
        })

    except ValueError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

    except Exception:
        return jsonify({
            "success": False,
            "error": "Something went wrong while solving the problem."
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)