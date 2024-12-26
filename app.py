from flask import Flask, render_template, request
from sudoku import solve_puzzle
import sudoku

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sudoku_grid = ["."] * 81

        for row in range(9):
            for col in range(9):
                cell_name = f"cell-{row}-{col}"
                value = request.form.get(cell_name)

                if value and value.isdigit() and 1 <= int(value) <= 9:
                    sudoku_grid[row * 9 + col] = value
                else:
                    sudoku_grid[row * 9 + col] = (
                        "."  # Store blank cells as "."
                    )

        sudoku_grid = "".join(sudoku_grid)
        # For demonstration, we'll just print the grid to the console
        print("Sudoku Grid:")
        print(sudoku_grid)

        # Here you can add code to store the grid in a database or perform other actions

        # Solve the puzzle
        if sudoku_grid is not None:
            try:
                solved_grid = solve_puzzle(sudoku_grid)
            except:
                return render_template(
                    "index.html",
                    success=False,
                    error="Invalid Sudoku puzzle",
                )

        print("Solved Grid:")
        print(solved_grid)

        if sudoku_grid is None:
            return render_template(
                "index.html",
                success=100,
            )
        return render_template(
            "index.html",
            success=True,
            sudoku_board=solved_grid,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=4999)
