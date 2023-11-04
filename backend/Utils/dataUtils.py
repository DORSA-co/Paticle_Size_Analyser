def list_to_csv(data):
    return ','.join(map(str, data)) 

def csv_to_list(csv:str, casting=float):
    if csv == '':
        return  []
    res = csv.split(',')
    return list(map(casting, res))