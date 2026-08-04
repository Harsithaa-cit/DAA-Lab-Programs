import tkinter as tk
from tkinter import ttk, messagebox


class SmartCityMST:

    def __init__(self, root):

        self.root = root
        self.root.title("Smart City Road Network Optimization")
        self.root.geometry("1000x650")


        # Cities
        self.cities = [
            "Chennai",
            "Guindy",
            "Adyar",
            "Velachery",
            "Tambaram",
            "OMR"
        ]


        # Roads (City1, City2, Cost)
        self.roads = [
            ("Chennai", "Guindy", 5),
            ("Chennai", "Tambaram", 10),
            ("Guindy", "Adyar", 7),
            ("Adyar", "Velachery", 3),
            ("Velachery", "OMR", 6),
            ("Tambaram", "Velachery", 8),
            ("Guindy", "OMR", 9)
        ]


        self.position = {

            "Chennai": (120,100),
            "Guindy": (320,80),
            "Adyar": (500,120),
            "Velachery": (420,280),
            "Tambaram": (150,350),
            "OMR": (650,300)

        }


        self.create_gui()
        self.draw_graph()



    def create_gui(self):

        panel = tk.Frame(
            self.root,
            width=250
        )

        panel.pack(
            side=tk.LEFT,
            fill=tk.Y
        )


        tk.Label(
            panel,
            text="Smart City MST",
            font=("Arial",16,"bold")
        ).pack(pady=10)



        tk.Label(
            panel,
            text="From City"
        ).pack()


        self.from_city = ttk.Combobox(
            panel,
            values=self.cities
        )

        self.from_city.pack()



        tk.Label(
            panel,
            text="To City"
        ).pack()


        self.to_city = ttk.Combobox(
            panel,
            values=self.cities
        )

        self.to_city.pack()



        tk.Label(
            panel,
            text="Road Cost"
        ).pack()


        self.cost = tk.Entry(panel)

        self.cost.pack()



        tk.Button(
            panel,
            text="Add Road",
            command=self.add_road
        ).pack(pady=5)



        tk.Button(
            panel,
            text="Run Kruskal",
            command=self.kruskal
        ).pack(pady=5)



        tk.Button(
            panel,
            text="Run Prim",
            command=self.prim
        ).pack(pady=5)



        tk.Button(
            panel,
            text="Reset",
            command=self.reset
        ).pack(pady=10)



        self.result = tk.Label(
            panel,
            text="Cost : -",
            font=("Arial",12)
        )

        self.result.pack()



        self.canvas = tk.Canvas(
            self.root,
            width=700,
            height=600,
            bg="white"
        )

        self.canvas.pack(
            side=tk.RIGHT
        )



    def draw_graph(self, mst=[]):

        self.canvas.delete("all")


        for a,b,cost in self.roads:

            x1,y1=self.position[a]
            x2,y2=self.position[b]


            width=2


            if (a,b,cost) in mst or (b,a,cost) in mst:
                width=5


            self.canvas.create_line(
                x1,y1,x2,y2,
                width=width
            )


            self.canvas.create_text(
                (x1+x2)//2,
                (y1+y2)//2,
                text=str(cost),
                fill="blue"
            )



        for city,(x,y) in self.position.items():

            self.canvas.create_oval(
                x-35,y-35,
                x+35,y+35,
                fill="lightgreen"
            )


            self.canvas.create_text(
                x,y,
                text=city
            )



    def add_road(self):

        a=self.from_city.get()
        b=self.to_city.get()


        try:
            c=int(self.cost.get())

        except:

            messagebox.showerror(
                "Error",
                "Enter valid cost"
            )
            return


        if a==b:

            messagebox.showerror(
                "Error",
                "Same city cannot connect"
            )
            return


        self.roads.append(
            (a,b,c)
        )

        self.draw_graph()



    # Union Find for Kruskal

    def find(self,parent,x):

        if parent[x]!=x:

            parent[x]=self.find(
                parent,
                parent[x]
            )

        return parent[x]



    def union(self,parent,rank,a,b):

        x=self.find(parent,a)
        y=self.find(parent,b)


        if x==y:
            return False


        if rank[x]<rank[y]:

            parent[x]=y

        elif rank[x]>rank[y]:

            parent[y]=x

        else:

            parent[y]=x
            rank[x]+=1


        return True



    # Kruskal Algorithm

    def kruskal(self):

        parent={}
        rank={}


        for city in self.cities:

            parent[city]=city
            rank[city]=0


        mst=[]
        total=0


        for a,b,c in sorted(
            self.roads,
            key=lambda x:x[2]
        ):


            if self.union(
                parent,
                rank,
                a,
                b
            ):

                mst.append(
                    (a,b,c)
                )

                total+=c



        self.result.config(
            text=f"Kruskal Cost = {total}"
        )

        self.draw_graph(mst)



    # Prim Algorithm

    def prim(self):

        visited=set()

        mst=[]

        total=0


        visited.add(
            self.cities[0]
        )


        while len(visited)<len(self.cities):

            possible=[]


            for a,b,c in self.roads:

                if a in visited and b not in visited:
                    possible.append((a,b,c))

                elif b in visited and a not in visited:
                    possible.append((a,b,c))


            if not possible:
                break


            edge=min(
                possible,
                key=lambda x:x[2]
            )


            mst.append(edge)

            total+=edge[2]


            visited.add(edge[0])
            visited.add(edge[1])


        self.result.config(
            text=f"Prim Cost = {total}"
        )

        self.draw_graph(mst)



    def reset(self):

        self.roads=[
            ("Chennai","Guindy",5),
            ("Chennai","Tambaram",10),
            ("Guindy","Adyar",7),
            ("Adyar","Velachery",3),
            ("Velachery","OMR",6),
            ("Tambaram","Velachery",8),
            ("Guindy","OMR",9)
        ]

        self.result.config(
            text="Cost : -"
        )

        self.draw_graph()



root=tk.Tk()

app=SmartCityMST(root)

root.mainloop()