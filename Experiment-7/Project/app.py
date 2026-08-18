from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# ------------------------------------------
# Check whether placing a queen is safe
# ------------------------------------------

def is_safe(board, row, col):

    for prev_row in range(row):

        placed = board[prev_row]

        # Same column
        if placed == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


# ------------------------------------------
# N-Queens Backtracking Algorithm
# ------------------------------------------

def solve_n_queens(n):

    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                backtrack(row + 1)

                # Undo the placement
                board[row] = -1
                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


# ------------------------------------------
# Home Page
# ------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------------------
# Solve N-Queens
# ------------------------------------------

@app.route("/solve", methods=["POST"])
def solve():

    data = request.get_json()

    try:
        n = int(data["n"])
    except (ValueError, TypeError, KeyError):
        return jsonify({
            "success": False,
            "message": "Please enter a valid value of N."
        })

    # Allow reasonable board sizes
    if n < 1 or n > 10:
        return jsonify({
            "success": False,
            "message": "Please enter N between 1 and 10."
        })

    solutions, backtracks = solve_n_queens(n)

    # Convert solutions into JSON-friendly format
    formatted_solutions = []

    for solution in solutions:

        board = []

        for row in range(n):

            current_row = []

            for col in range(n):

                if solution[row] == col:
                    current_row.append("Q")
                else:
                    current_row.append(".")

            board.append(current_row)

        formatted_solutions.append({
            "positions": solution,
            "board": board
        })

    return jsonify({
        "success": True,
        "n": n,
        "solution_count": len(solutions),
        "backtracks": backtracks,
        "solutions": formatted_solutions
    })


# ------------------------------------------
# Run Flask
# ------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)