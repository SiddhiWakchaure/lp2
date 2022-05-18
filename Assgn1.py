class Node:
    def __init__(self,value):
        self.value=value
        self.next=[]

    def __str__(self):
        return f"Node: {self.value}"

class Graph:
    def __init__(self,nodes):
        self.nodes=nodes
        self.visited=list(False for i in self.nodes)
        self.queue=[]
    def resetVisitedandQueue(self):
        self.visited = list(False for i in self.nodes)
        self.queue = []
    def dfs(self,index):
        self.visited[index] = True
        for i in self.nodes[index].next:
            if not self.visited[i]:
                self.dfs(i)
        print(self.nodes[index])
    def bfs(self,index):
        print(self.nodes[index])
        for i in self.nodes[index].next:
            if not self.visited[i]:
                self.visited[i] = True
                self.queue.append(i)
        if len(self.queue):
            self.bfs(self.queue.pop(0))

def menu():
    return int(input('''
What to perform?
1. DFS
2. BFS
0. Exit
'''))

def create_graph(n):
    nodes=list(Node(i) for i in range(n))
    return Graph(nodes)
def create_connections(graph):
    for i in range(int(input("Total edges: "))):
        u,v=map(int,input("Next connection: ").split())
        graph.nodes[u].next.append(v)
        graph.nodes[v].next.append(u)

graph=create_graph(int(input("Size of graph: ")))
create_connections(graph)

while True:
    choice=menu()
    if choice==0:
        print("Thank you")
        break
    if choice==1:
        graph.resetVisitedandQueue()
        graph.dfs(int(input("Start index: ")))
    elif choice==2:
        graph.resetVisitedandQueue()
        index=int(input("Start index: "))
        graph.visited[index] = True
        graph.bfs(index)

'''
OUTPUT:

Size of graph: 6
Total edges: 9
Next connection: 0 5
Next connection: 2 1
Next connection: 1 3
Next connection: 1 0
Next connection: 5 3
Next connection: 2 4
Next connection: 4 5
Next connection: 5 0
Next connection: 0 3

What to perform?
1. DFS
2. BFS
0. Exit
1
Start index: 5
Node: 4
Node: 2
Node: 3
Node: 1
Node: 0
Node: 5

What to perform?
1. DFS
2. BFS
0. Exit
2
Start index: 3
Node: 3
Node: 1
Node: 5
Node: 0
Node: 2
Node: 4

What to perform?
1. DFS
2. BFS
0. Exit
0
Thank you

Process finished with exit code 0

'''
