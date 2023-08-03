import numpy as np

def get_sift_idx(x , ranges):
    for i in range(len(ranges)):
        l, h = ranges[i]

        if l<= x < h:
            return i


def sift(xs, ranges: list[list]) -> list[np.ndarray]:
    sift_results = []
    for i in range(len(ranges)):
        sift_results.append([])
    for x in xs:
        idx = get_sift_idx(x, ranges)
        sift_results[idx].append(x)
    
    for i in range(len(sift_results)):
        sift_results[i] = np.array( sift_results[i] )
    return sift_results