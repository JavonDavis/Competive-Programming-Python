def lps(arr):
    n = len(arr)

    # Create a table to store results of subproblems
    dp_table = [[0 for _ in range(n)] for _ in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        dp_table[i][i] = 1

    # Build the table.
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if arr[i] == arr[j]:
                if cl == 2:
                    dp_table[i][j] = 2
                else:
                    dp_table[i][j] = dp_table[i + 1][j - 1] + 2
            else:
                dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i + 1][j])

    return dp_table[0][n - 1]