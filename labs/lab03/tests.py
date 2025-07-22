#!/usr/bin/env python3
import subprocess, sys, re

TOL = 1e-6

def extract_numbers(text):
    # find ints, floats, scientific notation
    nums = re.findall(r"-?\d+\.?\d*(?:[eE][+-]?\d+)?", text)
    return [float(n) for n in nums]

def run_test(script, input_data, expected):
    proc = subprocess.run(
        [sys.executable, script],
        input=input_data,
        text=True,
        capture_output=True
    )
    actual = extract_numbers(proc.stdout)
    ok = (
        len(actual) == len(expected)
        and all(abs(a - e) < TOL for a, e in zip(actual, expected))
    )
    if ok:
        print(f"PASS {script} | in={input_data.strip()} → out={actual}")
    else:
        print(f"\nFAIL {script}")
        print(f"  Input:    {input_data.strip()}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")
    return ok

def main():
    tests = [
        # Scenario 1 – hotel reservation: TOTAL_PAYMENT = 287.5 * n
        ("lab_03_2.py", "0\n", [0.0]),
        ("lab_03_2.py", "1\n", [287.50]),
        ("lab_03_2.py", "5\n", [1437.50]),

        # Scenario 2 – storage conversion: KB → MB, GB, TB, PB
        ("lab_03_3.py", "0\n",    [0.0,                 0.0,                   0.0,                     0.0]),
        ("lab_03_3.py", "1024\n", [1.0, 0.0009765625, 9.5367431640625e-07, 9.313225746154785e-10]),
        ("lab_03_3.py", "1536\n", [1.5, 0.00146484375, 1.430511474609375e-06, 1.4015116691589355e-09]),

        # Scenario 3 – fax cost: TOTAL_COST = 3 + 0.2 * pages
        ("lab_03_4.py", "0\n",  [3.00]),
        ("lab_03_4.py", "5\n",  [4.00]),
        ("lab_03_4.py", "10\n", [5.00]),

        # Scenario 4 – cookies: TOTAL_CALORIES = packs_eaten * 10 * 300
        ("lab_03_5.py", "0\n", [0.0]),
        ("lab_03_5.py", "1\n", [3000.0]),
        ("lab_03_5.py", "4\n", [12000.0]),

        # Scenario 5 – mow wage: WAGE = ((yard_area – house_area) * 2)
        ("lab_03_6.py", "10 10 4 4\n",   [168.00]),  # (100–16)*2
        ("lab_03_6.py", "5 5 2 2\n",     [42.00]),   # (25–4)*2
        ("lab_03_6.py", "20 15 5 5\n",   [550.00]),  # (300–25)*2
    ]

    failures = False
    for script, inp, exp in tests:
        if not run_test(script, inp, exp):
            failures = True

    if failures:
        sys.exit(1)
    print("\n✅ All tests passed.")

if __name__ == "__main__":
    main()
