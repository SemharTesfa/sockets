import xml.etree.cElementTree as ET


class ParseXML:
    def __init__(self, file_name):
        self.name = file_name

    def parseXML(self):
        my_tree = ET.parse(self.name)
        my_root = my_tree.getroot()

        for element in my_root:
            data = []
            for record in element.findall('record'):
                country = record.find('Country').text
                year = record.find('Year').text
                value = record.find('Value').text
                data.append([country, year, value])
        return data


if __name__ == "__main__":
    x = ParseXML("UNData.xml")
    #print(x.parseXML())
