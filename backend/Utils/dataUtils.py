def list_to_csv(data):
    return ','.join(map(str, data)) 

def csv_to_list(csv:str, casting=float):
    res = csv.split(',')
    return map(casting, res)