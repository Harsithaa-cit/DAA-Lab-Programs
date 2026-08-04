import tkinter as tk
from tkinter import ttk, messagebox


class MatrixOptimizer:

    def __init__(self, root):

        self.root = root
        self.root.title("🧮 Matrix Optimization Assistant")
        self.root.geometry("1000x700")
        self.root.configure(bg="#eef2ff")


        # ---------- Header ----------

        header = tk.Frame(
            root,
            bg="#312e81",
            height=90
        )

        header.pack(
            fill="x"
        )


        tk.Label(
            header,
            text="🧮 Matrix Optimization Assistant",
            font=("Arial", 24, "bold"),
            bg="#312e81",
            fg="white"
        ).pack(pady=10)


        tk.Label(
            header,
            text="Optimal Matrix Chain Multiplication using Dynamic Programming",
            font=("Arial", 11),
            bg="#312e81",
            fg="white"
        ).pack()



        # ---------- Input Card ----------

        input_frame = tk.Frame(
            root,
            bg="#dbeafe",
            bd=2,
            relief="groove"
        )

        input_frame.pack(
            pady=20,
            padx=30,
            fill="x"
        )


        tk.Label(
            input_frame,
            text="Enter Matrix Dimensions",
            font=("Arial",14,"bold"),
            bg="#dbeafe"
        ).pack(pady=5)


        tk.Label(
            input_frame,
            text="Example: 10 30 5 60 10",
            bg="#dbeafe"
        ).pack()


        self.entry = tk.Entry(
            input_frame,
            width=50,
            font=("Arial",13)
        )

        self.entry.pack(
            pady=10
        )


        tk.Button(
            input_frame,
            text="Optimize Matrix Chain",
            font=("Arial",12,"bold"),
            command=self.optimize
        ).pack(
            pady=10
        )



        # ---------- Result Area ----------

        result_frame = tk.Frame(
            root,
            bg="#fef3c7",
            bd=2,
            relief="groove"
        )

        result_frame.pack(
            padx=30,
            pady=10,
            fill="x"
        )


        self.result = tk.Label(
            result_frame,
            text="Results will appear here",
            font=("Arial",13),
            bg="#fef3c7",
            justify="left"
        )

        self.result.pack(
            pady=15
        )



        # ---------- DP Table ----------

        table_frame = tk.Frame(
            root,
            bg="#ffffff",
            bd=2,
            relief="groove"
        )

        table_frame.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=True
        )


        tk.Label(
            table_frame,
            text="DP Cost Table",
            font=("Arial",14,"bold"),
            bg="white"
        ).pack()


        self.table = ttk.Treeview(
            table_frame
        )

        self.table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )



    # Matrix Chain Multiplication DP

    def matrix_chain_order(self, dims):

        n = len(dims)-1


        m = [
            [0]*(n+1)
            for _ in range(n+1)
        ]


        s = [
            [0]*(n+1)
            for _ in range(n+1)
        ]



        for length in range(2,n+1):

            for i in range(1,n-length+2):

                j = i+length-1

                m[i][j] = float("inf")


                for k in range(i,j):

                    cost = (
                        m[i][k]
                        +
                        m[k+1][j]
                        +
                        dims[i-1]
                        *
                        dims[k]
                        *
                        dims[j]
                    )


                    if cost < m[i][j]:

                        m[i][j]=cost
                        s[i][j]=k


        return m,s



    def parenthesis(self,s,i,j):

        if i==j:

            return f"A{i}"


        k=s[i][j]


        left=self.parenthesis(
            s,
            i,
            k
        )


        right=self.parenthesis(
            s,
            k+1,
            j
        )


        return f"({left} × {right})"



    def optimize(self):

        try:

            dims=list(
                map(
                    int,
                    self.entry.get().split()
                )
            )


            if len(dims)<3:

                messagebox.showerror(
                    "Error",
                    "Enter minimum 3 dimensions"
                )

                return



            m,s=self.matrix_chain_order(
                dims
            )


            n=len(dims)-1


            order=self.parenthesis(
                s,
                1,
                n
            )


            self.result.config(

                text=
                f"Minimum Multiplication Cost : {m[1][n]}\n\n"
                f"Optimal Parenthesization :\n{order}\n\n"
                f"Number of Matrices : {n}"

            )


            self.display_table(
                m,
                n
            )



        except:

            messagebox.showerror(
                "Invalid Input",
                "Enter dimensions correctly"
            )



    def display_table(self,m,n):

        self.table.delete(
            *self.table.get_children()
        )


        self.table["columns"]=[
            f"A{i}"
            for i in range(1,n+1)
        ]


        self.table["show"]="headings"


        for col in self.table["columns"]:

            self.table.heading(
                col,
                text=col
            )


        for i in range(1,n+1):

            row=[]


            for j in range(1,n+1):

                if j<i:

                    row.append("---")

                else:

                    row.append(str(m[i][j]))


            self.table.insert(
                "",
                "end",
                values=row
            )



root=tk.Tk()

app=MatrixOptimizer(root)

root.mainloop()