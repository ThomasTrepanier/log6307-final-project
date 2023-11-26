def flatten(d, t = ["image", "text"]):
   for a, b in d.items():
      if a in t:
         yield b
      elif isinstance(b, dict):
         yield from flatten(b)
      elif isinstance(b, list):
         for i in b:
            yield from flatten(i)


d = {'document': {'page': [{'@index': '0', 'image': {'@data': 'ABC', '@format': 'png', '@height': '620.00', '@type': 'base64encoded', '@width': '450.00', '@x': '85.00', '@y': '85.00'}}, {'@index': '1', 'row': [{'column': [{'text': ''}, {'text': {'#text': 'Text1', '@fontName': 'Arial', '@fontSize': '12.0', '@height': '12.00', '@width': '71.04', '@x': '121.10', '@y': '83.42'}}]}, {'column': [{'text': ''}, {'text': {'#text': 'Text2', '@fontName': 'Arial', '@fontSize': '12.0', '@height': '12.00', '@width': '101.07', '@x': '121.10', '@y': '124.82'}}]}]}, {'@index': '2', 'row': [{'column': {'text': {'#text': 'Text3', '@fontName': 'Arial', '@fontSize': '12.0', '@height': '12.00', '@width': '363.44', '@x': '85.10', '@y': '69.62'}}}, {'column': {'text': {'#text': 'Text4', '@fontName': 'Arial', '@fontSize': '12.0', '@height': '12.00', '@width': '382.36', '@x': '85.10', '@y': '83.42'}}}, {'column': {'text': {'#text': 'Text5', '@fontName': 'Arial', '@fontSize': '12.0', '@height': '12.00', '@width': '435.05', '@x': '85.10', '@y': '97.22'}}}]}, {'@index': '3'}]}}
print(json.dumps(list(filter(None, flatten(d))), indent=4))
