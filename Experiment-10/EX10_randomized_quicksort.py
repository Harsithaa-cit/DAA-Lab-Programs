import random
import time
import sys

sys.setrecursionlimit(20000)

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

        # Select random pivot
        rand_idx = random.randint(low, high)

        # Move random pivot to last position
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        pi = partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# --------------------------------------------------
# Run Test
# --------------------------------------------------

def run_test(sort_fn, arr):

    global comparisons

    a = arr[:]

    comparisons = 0

    start = time.perf_counter()

    sort_fn(a, 0, len(a) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


# --------------------------------------------------
# Generate Test Cases
# --------------------------------------------------

N = 10000

test_cases = {

    "Random":
        [random.randint(1, 100000) for _ in range(N)],

    "Sorted":
        list(range(N)),

    "Reverse":
        list(range(N, 0, -1)),

    "Nearly Sorted":
        list(range(N))
}


# --------------------------------------------------
# Make Nearly Sorted Input
# --------------------------------------------------

ns = test_cases["Nearly Sorted"]

for _ in range(N // 20):

    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)

    ns[i], ns[j] = ns[j], ns[i]


# --------------------------------------------------
# Display Header
# --------------------------------------------------

print(
    f"{'Input Type':<18}"
    f"{'DQS Comps':>18}"
    f"{'DQS Time(ms)':>16}"
    f"{'RQS Comps':>18}"
    f"{'RQS Time(ms)':>16}"
)

print("-" * 86)


# --------------------------------------------------
# Run All Tests
# --------------------------------------------------

results = {}

for case, arr in test_cases.items():

    d_comps, d_time = run_test(
        deterministic_quicksort,
        arr
    )

    r_comps, r_time = run_test(
        randomized_quicksort,
        arr
    )

    results[case] = {
        "deterministic_comparisons": d_comps,
        "deterministic_time": d_time,
        "randomized_comparisons": r_comps,
        "randomized_time": r_time
    }

    print(
        f"{case:<18}"
        f"{d_comps:>18}"
        f"{d_time:>16.2f}"
        f"{r_comps:>18}"
        f"{r_time:>16.2f}"
    )


# --------------------------------------------------
# Summary
# --------------------------------------------------

print()
print("=" * 86)
print("SUMMARY")
print("=" * 86)

for case, result in results.items():

    d_comp = result["deterministic_comparisons"]
    r_comp = result["randomized_comparisons"]

    d_time = result["deterministic_time"]
    r_time = result["randomized_time"]

    print(f"\n{case}:")

    print(
        f"  Deterministic Quick Sort : "
        f"{d_comp} comparisons, {d_time:.2f} ms"
    )

    print(
        f"  Randomized Quick Sort    : "
        f"{r_comp} comparisons, {r_time:.2f} ms"
    )

    if d_time < r_time:
        print("  Faster Algorithm         : Deterministic Quick Sort")
    else:
        print("  Faster Algorithm         : Randomized Quick Sort")


# --------------------------------------------------
# Complexity
# --------------------------------------------------

print()
print("=" * 86)
print("COMPLEXITY")
print("=" * 86)

print("Deterministic Quick Sort:")
print("  Average Case : O(n log n)")
print("  Worst Case   : O(n^2)")

print()

print("Randomized Quick Sort:")
print("  Expected Case: O(n log n)")
print("  Worst Case   : O(n^2)")