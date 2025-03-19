function fibonacchi(n: number): number {
    if (n <= 1) return n;
    return n + fibonacchi(n - 1);
}

console.log(fibonacchi(1))
console.log(fibonacchi(5))