import tkinter as tk
from tkinter import messagebox
import random


class SmartMinMax:

    def __init__(self, root):

        self.root = root
        self.root.title("📊 Smart Data Analyzer - Divide & Conquer")
        self.root.geometry("950x650")
        self.root.resizable(False, False)


        self.comparisons = 0


        # ---------- Header ----------

        header = tk.Frame(
            root,
            height=80
        )

        header.pack(
            fill="x"
        )


        tk.Label(
            header,
            text="📊 Smart Data Analyzer",
            font=("Arial", 22, "bold")
        ).pack(pady=5)


        tk.Label(
            header,
            text="Minimum & Maximum Finding using Divide and Conquer Algorithm",
            font=("Arial", 11)
        ).pack()



        # ---------- Input Section ----------

        input_frame = tk.Frame(root)

        input_frame.pack(
            pady=15
        )


        tk.Label(
            input_frame,
            text="Enter Dataset:",
            font=("Arial",12,"bold")
        ).grid(
            row=0,
            column=0,
            padx=10
        )


        self.entry = tk.Entry(
            input_frame,
            width=60,
            font=("Arial",12)
        )

        self.entry.grid(
            row=0,
            column=1
        )



        # ---------- Buttons ----------

        button_frame = tk.Frame(root)

        button_frame.pack(
            pady=10
        )


        tk.Button(
            button_frame,
            text="Analyze Data",
            width=15,
            command=self.analyze
        ).grid(
            row=0,
            column=0,
            padx=10
        )


        tk.Button(
            button_frame,
            text="Generate Random",
            width=15,
            command=self.random_data
        ).grid(
            row=0,
            column=1,
            padx=10
        )


        tk.Button(
            button_frame,
            text="Clear",
            width=15,
            command=self.clear
        ).grid(
            row=0,
            column=2,
            padx=10
        )



        # ---------- Result Card ----------

        self.result_frame = tk.Frame(
            root,
            height=120
        )

        self.result_frame.pack(
            pady=15
        )


        self.result = tk.Label(
            self.result_frame,
            text="Run analysis to view results",
            font=("Arial",14),
            justify="left"
        )

        self.result.pack()



        # ---------- Graph Area ----------

        tk.Label(
            root,
            text="Data Visualization",
            font=("Arial",14,"bold")
        ).pack()


        self.canvas = tk.Canvas(
            root,
            width=850,
            height=250,
        )

        self.canvas.pack(
            pady=10
        )



    # Divide and Conquer Algorithm

    def min_max_dc(self, arr, low, high):

        if low == high:

            return arr[low], arr[low]


        if high == low + 1:

            self.comparisons += 1

            if arr[low] < arr[high]:

                return arr[low], arr[high]

            return arr[high], arr[low]


        mid = (low + high)//2


        left_min, left_max = self.min_max_dc(
            arr,
            low,
            mid
        )


        right_min, right_max = self.min_max_dc(
            arr,
            mid+1,
            high
        )


        self.comparisons += 1

        minimum = min(
            left_min,
            right_min
        )


        self.comparisons += 1

        maximum = max(
            left_max,
            right_max
        )


        return minimum, maximum



    def analyze(self):

        try:

            values = self.entry.get()

            arr = list(
                map(
                    int,
                    values.split(",")
                )
            )


            self.comparisons = 0


            minimum, maximum = self.min_max_dc(
                arr,
                0,
                len(arr)-1
            )


            self.result.config(

                text=
                f"Minimum Value : {minimum}\n\n"
                f"Maximum Value : {maximum}\n\n"
                f"Comparisons Used : {self.comparisons}\n\n"
                f"Algorithm : Divide & Conquer"

            )


            self.draw_chart(
                arr,
                minimum,
                maximum
            )


        except:

            messagebox.showerror(
                "Invalid Input",
                "Enter numbers separated by commas"
            )



    def random_data(self):

        arr = [
            random.randint(1,100)
            for i in range(10)
        ]


        self.entry.delete(
            0,
            tk.END
        )


        self.entry.insert(
            0,
            ",".join(
                map(str,arr)
            )
        )



    def draw_chart(self, arr, minimum, maximum):

        self.canvas.delete(
            "all"
        )


        max_value=max(arr)


        for i,value in enumerate(arr):

            x1=50+i*75
            height=(value/max_value)*150


            self.canvas.create_rectangle(

                x1,
                220-height,
                x1+40,
                220

            )


            self.canvas.create_text(

                x1+20,
                235,
                text=str(value)

            )


            if value==minimum:

                self.canvas.create_text(
                    x1+20,
                    200-height,
                    text="MIN"
                )


            if value==maximum:

                self.canvas.create_text(
                    x1+20,
                    200-height,
                    text="MAX"
                )



    def clear(self):

        self.entry.delete(
            0,
            tk.END
        )

        self.result.config(
            text="Run analysis to view results"
        )

        self.canvas.delete(
            "all"
        )



root=tk.Tk()

app=SmartMinMax(root)

root.mainloop()