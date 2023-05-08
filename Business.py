from DatabasePy import Database
from GraphPy import Graph
import matplotlib.pyplot as plt;
plt.rcdefaults()


class Business:
    def __init__(self):
        self.G = Graph()
        self.D = Database('SQLite_Python.db', 'Database')

    def query_to_database(self, country):
        data = self.D.fetch(country)
        self.G.create_xy_plot(data)
        return data



#x = Business()
#print(x.query_to_database("Turkey"))
