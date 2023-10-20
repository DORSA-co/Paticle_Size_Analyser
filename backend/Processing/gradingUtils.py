import numpy as np

def get_sift_idx(x , ranges):
    for i in range(len(ranges)):
        l, h = ranges[i]

        if l<= x < h:
            return i
    return -1


def sift(xs:np.ndarray, ranges: list[list]) -> list[np.ndarray]:
    """sift xs radiuses base on ranges

    Args:
        xs (_type_): _description_
        ranges (list[list]): _description_

    Returns:
        list[np.ndarray]: _description_
    """
    sift_results = []
    for i in range(len(ranges)):
        sift_results.append([])
    for x in xs:
        idx = get_sift_idx(x, ranges)
        if idx != -1:
            sift_results[idx].append(x)
    
    for i in range(len(sift_results)):
        sift_results[i] = np.array( sift_results[i] )
    return sift_results