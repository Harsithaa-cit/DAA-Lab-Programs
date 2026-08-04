import tkinter as tk
from tkinter import ttk, messagebox
import heapq


class SmartRouteFinder:

    def __init__(self, root):

        self.root = root
        self.root.title("Smart City Emergency Route Finder - Dijkstra")
        self.root.geometry("1000x650")


        # Locations (Vertices)

        self.locations = [
            "Hospital",
            "School",
            "Market",
            "Railway Station",
            "Airport",
            "Bus Stand"
        ]


        # Road network (Edges with distance)

        self.graph = {

            "Hospital": [
                ("School", 4),
                ("Market", 2)
            ],

            "School": [
                ("Hospital", 4),
                ("Railway Station", 5),
                ("Market", 1)
            ],

            "Market": [
                ("Hospital", 2),
                ("School", 1),
                ("Airport", 8)
            ],

            "Railway Station": [
                ("School", 5),
                ("Airport", 3),
                ("Bus Stand", 6)
            ],

            "Airport": [
                ("Market", 8),
                ("Railway Station", 3),
                ("Bus Stand", 2)
            ],

            "Bus Stand": [
                ("Railway Station", 6),
                ("Airport", 2)
            ]
        }


        # Positions for visualization

        self.position = {

            "Hospital": (120,120),
            "School": (350,80),
            "Market": (300,250),
            "Railway Station": (550,150),
            "Airport": (700,280),
            "Bus Stand": (450,420)

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
            text="Emergency Route Finder",
            font=("Arial",15,"bold")
        ).pack(pady=10)



        tk.Label(
            panel,
            text="Source Location"
        ).pack()


        self.source = ttk.Combobox(
            panel,
            values=self.locations
        )

        self.source.pack()



        tk.Label(
            panel,
            text="Destination"
        ).pack()


        self.destination = ttk.Combobox(
            panel,
            values=self.locations
        )

        self.destination.pack()



        tk.Button(
            panel,
            text="Find Shortest Route",
            command=self.find_route
        ).pack(pady=10)



        tk.Button(
            panel,
            text="Reset",
            command=self.reset
        ).pack()



        self.result = tk.Label(
            panel,
            text="Distance : -",
            wraplength=220,
            font=("Arial",12)
        )

        self.result.pack(pady=20)



        self.canvas = tk.Canvas(
            self.root,
            width=700,
            height=600,
            bg="white"
        )

        self.canvas.pack(
            side=tk.RIGHT
        )



    def draw_graph(self, path=[]):

        self.canvas.delete("all")


        # Draw roads

        for u in self.graph:

            for v,w in self.graph[u]:

                x1,y1=self.position[u]
                x2,y2=self.position[v]


                width=2


                # Highlight shortest path

                if len(path)>1:

                    for i in range(len(path)-1):

                        if (
                            (path[i]==u and path[i+1]==v)
                            or
                            (path[i]==v and path[i+1]==u)
                        ):
                            width=5



                self.canvas.create_line(
                    x1,y1,
                    x2,y2,
                    width=width
                )


                self.canvas.create_text(
                    (x1+x2)//2,
                    (y1+y2)//2,
                    text=str(w),
                    fill="blue"
                )



        # Draw locations

        for place,(x,y) in self.position.items():

            self.canvas.create_oval(
                x-35,y-35,
                x+35,y+35,
                fill="lightgreen"
            )


            self.canvas.create_text(
                x,
                y,
                text=place.replace(" ","\n")
            )



    # Dijkstra Algorithm

    def dijkstra(self, source):

        distance={}

        previous={}


        for node in self.locations:

            distance[node]=float("inf")
            previous[node]=None


        distance[source]=0


        queue=[
            (0,source)
        ]


        while queue:

            current_distance,current = heapq.heappop(queue)


            if current_distance > distance[current]:
                continue


            for neighbour,weight in self.graph[current]:

                new_distance=current_distance+weight


                if new_distance < distance[neighbour]:

                    distance[neighbour]=new_distance

                    previous[neighbour]=current


                    heapq.heappush(
                        queue,
                        (new_distance,neighbour)
                    )


        return distance,previous



    def reconstruct_path(self, previous, source, target):

        path=[]

        current=target


        while current is not None:

            path.append(current)

            current=previous[current]


        path.reverse()


        if path[0]==source:

            return path

        return []



    def find_route(self):

        source=self.source.get()

        destination=self.destination.get()


        if source=="" or destination=="":

            messagebox.showerror(
                "Error",
                "Select source and destination"
            )

            return



        distance,previous=self.dijkstra(source)


        path=self.reconstruct_path(
            previous,
            source,
            destination
        )


        if not path:

            self.result.config(
                text="No Route Available"
            )

            return



        self.result.config(

            text=
            f"Shortest Route:\n"
            f"{' → '.join(path)}\n\n"
            f"Distance = {distance[destination]} km"

        )


        self.draw_graph(path)



    def reset(self):

        self.result.config(
            text="Distance : -"
        )

        self.draw_graph([])



root=tk.Tk()

app=SmartRouteFinder(root)

root.mainloop()