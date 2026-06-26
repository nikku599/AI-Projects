Certainly! To solve the N-Queens problem in Java, we'll:

1. Use backtracking recursion to place queens row by row.
2. Ensure that queens don't threaten each other by checking columns, and diagonals.
3. Store solutions as a list of solutions, where each solution is represented as a 2D array or list.
4. Print all solutions found.

Here's the plan:
- Create a main class called `NQueens`.
- Use a helper method `solveNQueens` that takes the size `n` and outputs solutions.
- Use a recursive backtracking method `solve` to place queens row by row.
- For checking conflicts, maintain boolean arrays for columns, diagonals, and anti-diagonals.

Now, I will present the complete code and then output the solutions for a manageable `n`, such as 4 or 8.

---

### Complete Java Code for N-Queens Problem

```java
import java.util.ArrayList;
import java.util.List;

public class NQueens {
    private int size;
    private List<List<String>> solutions;

    public NQueens(int n) {
        this.size = n;
        this.solutions = new ArrayList<>();
    }

    public List<List<String>> solveNQueens() {
        boolean[] columns = new boolean[size]; // Columns occupancy
        boolean[] diag1 = new boolean[2 * size - 1]; // Main diagonals
        boolean[] diag2 = new boolean[2 * size - 1]; // Anti-diagonals
        int[] queens = new int[size]; // queens[row] = col index

        solve(0, queens, columns, diag1, diag2);
        return solutions;
    }

    private void solve(int row, int[] queens, boolean[] columns, boolean[] diag1, boolean[] diag2) {
        if (row == size) {
            // All queens placed successfully
            solutions.add(buildBoard(queens));
            return;
        }

        for (int col = 0; col < size; col++) {
            int d1 = row - col + size - 1; // index for main diagonal
            int d2 = row + col; // index for anti-diagonal

            if (columns[col] || diag1[d1] || diag2[d2]) {
                continue; // Conflict, try next column
            }

            // Place queen
            queens[row] = col;
            columns[col] = true;
            diag1[d1] = true;
            diag2[d2] = true;

            solve(row + 1, queens, columns, diag1, diag2);

            // Backtrack
            columns[col] = false;
            diag1[d1] = false;
            diag2[d2] = false;
        }
    }

    private List<String> buildBoard(int[] queens) {
        List<String> board = new ArrayList<>();
        for (int row = 0; row < size; row++) {
            StringBuilder rowString = new StringBuilder();
            for (int col = 0; col < size; col++) {
                if (queens[row] == col) {
                    rowString.append('Q');
                } else {
                    rowString.append('.');
                }
            }
            board.add(rowString.toString());
        }
        return board;
    }

    public static void main(String[] args) {
        int n = 4; // You can change this to 8 for more complexity
        NQueens solution = new NQueens(n);
        List<List<String>> allSolutions = solution.solveNQueens();

        System.out.println("Total solutions for " + n + "-Queens: " + allSolutions.size());
        int count = 1;
        for (List<String> sol : allSolutions) {
            System.out.println("Solution " + count + ":");
            for (String row : sol) {
                System.out.println(row);
            }
            System.out.println();
            count++;
        }
    }
}
```

---

### Expected Output for `n = 4`

Running the above code will produce:

```
Total solutions for 4-Queens: 2
Solution 1:
.Q..
...Q
Q...
..Q.

Solution 2:
..Q.
Q...
...Q
.Q..
```

---

### Final notes:
- Change `int n = 4;` in the `main` method to other sizes like 8 for more complex solutions.
- The code is efficient and uses backtracking with pruning for speed.

---

**You asked for a text file with code and output.**

### Content of `NQueensSolution.java`

```plaintext
import java.util.ArrayList;
import java.util.List;

public class NQueens {
    private int size;
    private List<List<String>> solutions;

    public NQueens(int n) {
        this.size = n;
        this.solutions = new ArrayList<>();
    }

    public List<List<String>> solveNQueens() {
        boolean[] columns = new boolean[size]; // Columns occupancy
        boolean[] diag1 = new boolean[2 * size - 1]; // Main diagonals
        boolean[] diag2 = new boolean[2 * size - 1]; // Anti-diagonals
        int[] queens = new int[size]; // queens[row] = col index

        solve(0, queens, columns, diag1, diag2);
        return solutions;
    }

    private void solve(int row, int[] queens, boolean[] columns, boolean[] diag1, boolean[] diag2) {
        if (row == size) {
            // All queens placed successfully
            solutions.add(buildBoard(queens));
            return;
        }

        for (int col = 0; col < size; col++) {
            int d1 = row - col + size - 1; // index for main diagonal
            int d2 = row + col; // index for anti-diagonal

            if (columns[col] || diag1[d1] || diag2[d2]) {
                continue; // Conflict, try next column
            }

            // Place queen
            queens[row] = col;
            columns[col] = true;
            diag1[d1] = true;
            diag2[d2] = true;

            solve(row + 1, queens, columns, diag1, diag2);

            // Backtrack
            columns[col] = false;
            diag1[d1] = false;
            diag2[d2] = false;
        }
    }

    private List<String> buildBoard(int[] queens) {
        List<String> board = new ArrayList<>();
        for (int row = 0; row < size; row++) {
            StringBuilder rowString = new StringBuilder();
            for (int col = 0; col < size; col++) {
                if (queens[row] == col) {
                    rowString.append('Q');
                } else {
                    rowString.append('.');
                }
            }
            board.add(rowString.toString());
        }
        return board;
    }

    public static void main(String[] args) {
        int n = 4; // Set size of chessboard
        NQueens solution = new NQueens(n);
        List<List<String>> allSolutions = solution.solveNQueens();

        System.out.println("Total solutions for " + n + "-Queens: " + allSolutions.size());
        int count = 1;
        for (List<String> sol : allSolutions) {
            System.out.println("Solution " + count + ":");
            for (String row : sol) {
                System.out.println(row);
            }
            System.out.println();
            count++;
        }
    }
}
```

### Output for n=4

```plaintext
Total solutions for 4-Queens: 2
Solution 1:
.Q..
...Q
Q...
..Q.

Solution 2:
..Q.
Q...
...Q
.Q..
```

---

You can compile and run this Java code to verify the solutions.