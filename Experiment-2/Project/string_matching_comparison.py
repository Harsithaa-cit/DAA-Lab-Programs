import tkinter as tk
from tkinter import scrolledtext
import time


# ---------------- Naive Algorithm ----------------

def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []

    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            matches.append(i)

    return matches


# ---------------- KMP Algorithm ----------------

def compute_lps(pattern):
    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length-1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):

    matches = []

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < len(text):

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i-j)
            j = lps[j-1]

        elif i < len(text) and text[i] != pattern[j]:

            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return matches



# ---------------- Rabin-Karp Algorithm ----------------

def rabin_karp(text, pattern):

    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    matches = []

    if m > n:
        return matches

    h = pow(d, m-1, q)

    p_hash = 0
    t_hash = 0


    for i in range(m):
        p_hash = (d*p_hash + ord(pattern[i])) % q
        t_hash = (d*t_hash + ord(text[i])) % q


    for i in range(n-m+1):

        if p_hash == t_hash:

            if text[i:i+m] == pattern:
                matches.append(i)


        if i < n-m:

            t_hash = (
                d*(t_hash - ord(text[i])*h)
                + ord(text[i+m])
            ) % q


    return matches



# ---------------- GUI Function ----------------

def analyze():

    text = text_box.get("1.0", tk.END).strip()
    pattern = pattern_box.get().strip()


    if not text or not pattern:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END,
                          "Please enter text and pattern")
        return


    algorithms = {
        "Naive": naive_search,
        "Rabin-Karp": rabin_karp,
        "KMP": kmp_search
    }


    result = ""
    times = {}


    for name, algorithm in algorithms.items():

        start = time.perf_counter()

        matches = algorithm(text, pattern)

        end = time.perf_counter()


        execution_time = end-start

        times[name] = execution_time


        result += (
            f"{name} Algorithm\n"
            f"Matches: {matches}\n"
            f"Execution Time: {execution_time:.8f} seconds\n\n"
        )


    fastest = min(times, key=times.get)


    result += (
        "--------------------------\n"
        f"Fastest Algorithm: {fastest}\n"
        f"Minimum Time: {times[fastest]:.8f} seconds"
    )


    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)



# ---------------- UI Design ----------------

window = tk.Tk()

window.title("String Matching Algorithm Analyzer")

window.geometry("700x600")


tk.Label(
    window,
    text="Enter Text",
    font=("Arial", 12)
).pack()


text_box = scrolledtext.ScrolledText(
    window,
    height=8,
    width=70
)

text_box.pack()



tk.Label(
    window,
    text="Enter Pattern",
    font=("Arial", 12)
).pack()


pattern_box = tk.Entry(
    window,
    width=50
)

pattern_box.pack()



tk.Button(
    window,
    text="Analyze Algorithms",
    command=analyze,
    font=("Arial", 12)
).pack(pady=10)



tk.Label(
    window,
    text="Result",
    font=("Arial", 12)
).pack()



result_box = scrolledtext.ScrolledText(
    window,
    height=15,
    width=70
)

result_box.pack()


window.mainloop()