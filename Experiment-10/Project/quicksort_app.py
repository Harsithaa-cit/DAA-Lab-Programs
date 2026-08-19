from flask import Flask, render_template, request, jsonify
import random
import time
import sys

app = Flask(__name__)

sys.setrecursionlimit(20000)


# --------------------------------------------------
# Global comparison counter
# --------------------------------------------------

comparisons = 0


# --------------------------------------------------
# Partition
# --------------------------------------------------

def partition(arr, low, high):
    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# --------------------------------------------------
# Deterministic Quick Sort
# Pivot = Last Element
# --------------------------------------------------

def deterministic_quicksort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


# --------------------------------------------------
# Randomized Quick Sort
# Pivot = Random Element
# --------------------------------------------------

def randomized_quicksort(arr, low, high):

    if low < high:

        random_index = random.randint(low, high)

        # Move random pivot to last position
        arr[random_index], arr[high] = (
            arr[high],
            arr[random_index]
        )

        pi = partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# --------------------------------------------------
# Run Sorting Algorithm
# --------------------------------------------------

def run_sort(arr, algorithm):

    global comparisons

    comparisons = 0

    start_time = time.perf_counter()

    if algorithm == "deterministic":

        deterministic_quicksort(
            arr,
            0,
            len(arr) - 1
        )

    else:

        randomized_quicksort(
            arr,
            0,
            len(arr) - 1
        )

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    return comparisons, execution_time


# --------------------------------------------------
# Generate Test Array
# --------------------------------------------------

def generate_array(size, input_type):

    if input_type == "random":

        return [
            random.randint(1, 100000)
            for _ in range(size)
        ]

    elif input_type == "sorted":

        return list(range(size))

    elif input_type == "reverse":

        return list(range(size, 0, -1))

    elif input_type == "nearly_sorted":

        arr = list(range(size))

        # Perform 5% random swaps
        for _ in range(size // 20):

            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)

            arr[i], arr[j] = arr[j], arr[i]

        return arr

    return []


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def index():

    return render_template("index.html")


# --------------------------------------------------
# Sort API
# --------------------------------------------------

@app.route("/sort", methods=["POST"])
def sort_array():

    try:

        data = request.get_json()

        input_type = data.get("input_type", "random")
        algorithm = data.get("algorithm", "randomized")
        size = int(data.get("size", 20))

        # Limit web demonstration size
        if size < 1:
            return jsonify({
                "error": "Array size must be at least 1."
            }), 400

        if size > 10000:
            return jsonify({
                "error": "Maximum array size is 10000."
            }), 400

        # Generate input
        original_array = generate_array(
            size,
            input_type
        )

        arr = original_array[:]

        # Run algorithm
        comparisons, execution_time = run_sort(
            arr,
            algorithm
        )

        return jsonify({

            "success": True,

            "algorithm": (
                "Deterministic Quick Sort"
                if algorithm == "deterministic"
                else "Randomized Quick Sort"
            ),

            "input_type": input_type,

            "size": size,

            "comparisons": comparisons,

            "time": round(execution_time, 4),

            "original": original_array[:100],

            "sorted": arr[:100]

        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# --------------------------------------------------
# Compare Both Algorithms
# --------------------------------------------------

@app.route("/compare", methods=["POST"])
def compare_algorithms():

    try:

        data = request.get_json()

        input_type = data.get(
            "input_type",
            "random"
        )

        size = int(
            data.get("size", 1000)
        )

        if size < 1:

            return jsonify({
                "error": "Array size must be at least 1."
            }), 400

        if size > 10000:

            return jsonify({
                "error": "Maximum array size is 10000."
            }), 400

        # Generate same input for fair comparison
        original_array = generate_array(
            size,
            input_type
        )

        deterministic_array = original_array[:]
        randomized_array = original_array[:]

        # Deterministic
        d_comparisons, d_time = run_sort(
            deterministic_array,
            "deterministic"
        )

        # Randomized
        r_comparisons, r_time = run_sort(
            randomized_array,
            "randomized"
        )

        return jsonify({

            "success": True,

            "input_type": input_type,

            "size": size,

            "deterministic": {

                "comparisons": d_comparisons,

                "time": round(
                    d_time,
                    4
                )

            },

            "randomized": {

                "comparisons": r_comparisons,

                "time": round(
                    r_time,
                    4
                )

            },

            "sorted": (
                deterministic_array
                == randomized_array
            )

        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# --------------------------------------------------
# Run Flask
# --------------------------------------------------

app.run(
    debug=True,
    port=5003
)