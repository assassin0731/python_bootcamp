import networkx as nx
import matplotlib.pyplot as plt
import json
import scipy

G = nx.Graph()


def main():
    try:
        a_file = open("result.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        G.add_nodes_from(json_object.keys())

        for node, neighbors in json_object.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        nx.draw(G, with_labels=True)
        plt.show()
    except FileNotFoundError:
        print('Database not found')


if __name__ == '__main__':
    main()
