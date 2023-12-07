def list_to_csv(data):
    return ','.join(map(str, data)) 

def csv_to_list(csv:str, casting=float):
    if csv == '':
        return  []
    splited = csv.split(',')
    res = []
    for x in splited:
        try:
            x  = casting(x)
            res.append(x)
        except:
            continue
    #res = list(map(casting, res))
    #res = list()
    return res