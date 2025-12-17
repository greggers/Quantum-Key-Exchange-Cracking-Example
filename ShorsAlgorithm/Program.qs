open Microsoft.Quantum.Intrinsic;
open Microsoft.Quantum.Canon;
open Microsoft.Quantum.Math;
open Microsoft.Quantum.Arithmetic;
open Microsoft.Quantum.Measurement;
open Microsoft.Quantum.Convert;

operation GreatestCommonDivisor(a : Int, b : Int) : Int {
    mutable x = a;
    mutable y = b;
    while (y != 0) {
        let temp = y;
        set y = x % y;
        set x = temp;
    }
    return x;
}

// Quantum order finding using QFT (simplified for small numbers)
operation QuantumOrderFinding(a : Int, N : Int) : Int {
    // Placeholder for real quantum order-finding logic
    return 4; // This would be found using QPE on a real quantum computer
}

operation ShorsAlgorithm(N : Int) : (Int, Int) {
    mutable a = 2; // Pick a small random number

    // Ensure a is coprime to N
    while (GreatestCommonDivisor(a, N) > 1) {
        set a = a + 1;
    }

    // Quantum step: Find the order r of a mod N
    let r = QuantumOrderFinding(a, N);

    // Compute potential factors using GCD
    let factor1 = GreatestCommonDivisor(PowerI(a, r / 2) - 1, N);
    let factor2 = N / factor1;

    return (factor1, factor2);
}

operation RunShorsExample() : Unit {
    let N = 15; // Example: Factoring 15 = 3 × 5
    let (p, q) = ShorsAlgorithm(N);
    Message($"Factors of {N} are {p} and {q}");
}
