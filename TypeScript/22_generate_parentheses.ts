// 22. Generate Parentheses

/**
 * This function generates all combinations of well-formed parentheses.
 *
 * @param n - The number of pairs of parentheses.
 * @returns An array of strings, each string representing a valid combination of parentheses.
 *
 * The function uses a depth-first search (DFS) approach to build the combinations.
 * It maintains a balance between the number of opening and closing parentheses.
 *
 * Time Complexity: O(4^n / sqrt(n))
 * Space Complexity: O(n)
 */
function generateParenthesis(n: number): string[] {
    let res: string[] = [];

    function dfs(left: number, right: number, s: string) {
        if (left + right === n * 2) {
            res.push(s);
        }

        if (left < n) {
            dfs(left + 1, right, s + '(');
        }

        if (right < left) {
            dfs(left, right + 1, s + ')');
        }
    }

    dfs(0, 0, '');
    return res;
}

// Test
let n = 3;
let result = generateParenthesis(n);
console.log(result); // Output: ["((()))","(()())","(())()","()(())","()()()"]