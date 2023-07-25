import numpy
cimport numpy
cimport cython
from libc.math cimport cos

cdef float pi = 3.14159




ctypedef numpy.int32_t DTYPE_int32
ctypedef numpy.uint8_t DTYPE_uint8
ctypedef numpy.float32_t DTYPE_float32
ctypedef numpy.float DTYPE_float64

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def histogram(numpy.ndarray[DTYPE_float64, ndim=1] xs,
        numpy.ndarray [DTYPE_float64, ndim=2]ranges,
        numpy.ndarray[DTYPE_float64, ndim=1] weights):

    cdef int i,j
    cdef int xs_count = xs.shape[0]
    cdef int ranges_count = ranges.shape[0]
    cdef numpy.ndarray[DTYPE_float64, ndim=1] res = numpy.zeros((ranges_count,), dtype = numpy.float64)
    
    #Only for performance search in half of range
    cdef int mid_range_idx = ranges_count//2
    cdef float mid_range_val = ranges[mid_range_idx,0]
    cdef int start_scan_index = 0
    #--------------------------------------------

    for i in range(xs_count):
        x = xs[i]
        #only for performance
        start_scan_index = 0
        if x >= mid_range_val:
            start_scan_index = mid_range_idx
        #-------------------
        for j in range(start_scan_index,ranges_count):
            
            if   ranges[j,0] <= x and  x < ranges[j, 1]:
                  res[j] += weights[i]
        #         break
        
    return res



