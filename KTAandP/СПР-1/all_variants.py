import math

print("=" * 60)
print("SIMPLIFIED TASK: Piecewise Function Calculator")
print("=" * 60)
# Input variant number
variant = int(input("Enter variant number (1-23): "))
if variant < 1 or variant > 23:
    print("Error: variant must be between 1 and 23")
else:
    # Input x value
    x = float(input("Enter x value: "))

    # Dictionary with interval boundaries for each variant
    # Each variant has 3 boundary points (b1, b2, b3)
    intervals = {
        1: (-2, 1, 3), 2: (0, 2, 5), 3: (-3, 0, 4),
        4: (-1, 1, 3), 5: (-1.5, 0.5, 2.5), 6: (-2.5, 0, 3.5),
        7: (-4, -1, 2), 8: (-0.5, 1.5, 4), 9: (-2.8, -0.5, 1.5),
        10: (-1.8, 0.8, 3.2), 11: (-0.8, 1.2, 3.5), 12: (-3.2, -0.5, 2.5),
        13: (-1.2, 0.6, 2.8), 14: (-2.2, 0.2, 2.6), 15: (-3.5, -1.2, 1.5),
        16: (-2.6, -0.3, 1.8), 17: (-2.4, 0.4, 3.2), 18: (-1.4, 0.9, 2.9),
        19: (-4.5, -2.2, 0), 20: (-0.7, 1.8, 4.5), 21: (-3.8, -1.5, 0.8),
        22: (-3.3, -0.8, 1.2), 23: (-1.6, 0.5, 2.4)
    }

    # Get boundaries for selected variant
    b1, b2, b3 = intervals[variant]

    print("\n" + "=" * 60)
    print(f"VARIANT {variant}")
    print("=" * 60)
    # Display interval definitions
    print(f"\nInterval definitions for variant {variant}:")
    print(f" I1: x < {b1}")
    print(f" I2: {b1} ≤ x < {b2}")
    print(f" I3: {b2} ≤ x < {b3}")
    print(f" I4: x ≥ {b3}")

    print(f"\n{'─' * 60}")
    print(f"INPUT: x = {x}")
    print(f"{'─' * 60}")

    # Determine which interval x belongs to and calculate y
    if x < b1:
        # Interval I1: y = x^2 + 1
        interval_name = f"I1 (x < {b1})"
        formula = "y = x² + 1"

        print(f"\nANALYSIS:")
        print(f" • Value x = {x} belongs to interval {interval_name}")
        print(f" • Formula to use: {formula}")

        print(f"\nCALCULATION:")
        print(f" y = x² + 1")
        print(f" y = ({x})² + 1")
        print(f" y = {x ** 2} + 1")

        y = x ** 2 + 1

        print(f"\n{'═' * 60}")
        print(f"RESULT: y = {y:.6f}")
        print(f"{'═' * 60}")

    elif x < b2:
        # Interval I2: y = sin(x)
        interval_name = f"I2 ({b1} ≤ x < {b2})"
        formula = "y = sin(x)"

        print(f"\nANALYSIS:")
        print(f" • Value x = {x} belongs to interval {interval_name}")
        print(f" • Formula to use: {formula}")

        print(f"\nCALCULATION:")
        print(f" y = sin(x)")
        print(f" y = sin({x})")

        y = math.sin(x)

        print(f"\n{'═' * 60}")
        print(f"RESULT: y = {y:.6f}")
        print(f"{'═' * 60}")

    elif x < b3:
        # Interval I3: y = e^x
        interval_name = f"I3 ({b2} ≤ x < {b3})"
        formula = "y = e^x"

        print(f"\nANALYSIS:")
        print(f" • Value x = {x} belongs to interval {interval_name}")
        print(f" • Formula to use: {formula}")

        print(f"\nCALCULATION:")
        print(f" y = e^x")
        print(f" y = e^({x})")

        y = math.exp(x)

        print(f"\n{'═' * 60}")
        print(f"RESULT: y = {y:.6f}")
        print(f"{'═' * 60}")

    else:
        # Interval I4: y = ln|x+1|
        interval_name = f"I4 (x ≥ {b3})"
        formula = "y = ln|x+1|"

        print(f"\nANALYSIS:")
        print(f" • Value x = {x} belongs to interval {interval_name}")
        print(f" • Formula to use: {formula}")

        # Check if x = -1 (undefined point)
        if x == -1:
            print(f"\n{'═' * 60}")
            print(f"ERROR: Function is undefined at x = {x}")
            print(f" (logarithm of zero)")
            print(f"{'═' * 60}")
        else:
            print(f"\nCALCULATION:")
            print(f" y = ln|x+1|")
            print(f" y = ln|{x}+1|")
            print(f" y = ln|{x + 1}|")

            y = math.log(abs(x + 1))

            print(f"\n{'═' * 60}")
            print(f"RESULT: y = {y:.6f}")
            print(f"{'═' * 60}")

