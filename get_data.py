import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    k = json.loads(filename)

f = open('randomuser_data.json','r')
x= f.read()
print(get_data(x))