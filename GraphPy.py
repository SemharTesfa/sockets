import matplotlib.pyplot as plt;
import json
plt.rcdefaults()


class Graph:
    def __init__(self):
        pass

    def create_xy_plot(self, data):
        data_dict = json.loads(data)

        keys = data_dict.keys()
        values = [data_dict[key] for key in keys]
        plt.plot(keys, values)
        plt.xticks(rotation=90)
        plt.tight_layout()

        plt.show()
        return plt

#x = Graph()
#x.create_xy_plot("Turkey")


