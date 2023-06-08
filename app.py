"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"



@hops.component(
    "/binmult",
    inputs=[
        hs.HopsNumber("A"), 
        hs.HopsNumber("B")
        ],
    outputs=[
        hs.HopsNumber("Multiply")
        ],
)
def BinaryMultiply(a: float, b: float):
    return a * b

@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b

#write a subtract component here in @hops format
@hops.component(
    "/subtract",
    name="Subtract",
    nickname="Sub",
    description="Subtract numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Difference", "D", "A - B")]
)
def subtract(a: float, b: float):
    return a - b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

#write a @hops.component function that creates complex numbers
#and returns them as a list of point

@hops.component(
    "/complex",
    name="Complex",
    nickname="Complex",
    description="Create complex numbers",
    inputs=[
        hs.HopsNumber("Real", "R", "Real part"),
        hs.HopsNumber("Imaginary", "I", "Imaginary part"),
        hs.HopsNumber("Z", "Z", "Z component of the complex number")
    ],
    outputs=[hs.HopsPoint("Complex", "C", "Complex number")]
)
def complex(r: float, i: float, z: float):
    import math
    import random
    return rhino3dm.Point3d(r, i, z + random.uniform(-3, 3))


"""
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗                                           
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║                                           
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║                                           
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║                                           
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║                                           
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                           
                                                                                                
███████╗ ██████╗ ██████╗                                                                        
██╔════╝██╔═══██╗██╔══██╗                                                                       
█████╗  ██║   ██║██████╔╝                                                                       
██╔══╝  ██║   ██║██╔══██╗                                                                       
██║     ╚██████╔╝██║  ██║                                                                       
╚═╝      ╚═════╝ ╚═╝  ╚═╝                                                                       
                                                                                                
██████╗  █████╗ ████████╗ █████╗      █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗██╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██║██╔════╝
██║  ██║███████║   ██║   ███████║    ███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗██║███████╗
██║  ██║██╔══██║   ██║   ██╔══██║    ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██║╚════██║
██████╔╝██║  ██║   ██║   ██║  ██║    ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║██║███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚══════╝
"""
#Python for Data Analysis
#Data Wrngling with Pandas, NumPy, and IPython
#By Wes McKinney
#https://www.oreilly.com/library/view/python-for-data/9781491957653/

import pandas as pd
import numpy as np
import rhino3dm
import random
pd.options.display.max_rows = 20
pd.options.display.max_columns = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)

"""

███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗
████╗  ██║██║   ██║████╗ ████║██╔══██╗╚██╗ ██╔╝
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝ ╚████╔╝ 
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔═══╝   ╚██╔╝  
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║        ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   
                                               
██████╗  █████╗ ███████╗██╗ ██████╗███████╗    
██╔══██╗██╔══██╗██╔════╝██║██╔════╝██╔════╝    
██████╔╝███████║███████╗██║██║     ███████╗    
██╔══██╗██╔══██║╚════██║██║██║     ╚════██║    
██████╔╝██║  ██║███████║██║╚██████╗███████║    
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚══════╝   
"""
#example of performance of numpy arrays vs python lists
my_arr = np.arange(1000000)
my_list = list(range(1000000))
#multiply each sequence by 2
'''
#in ipython %timeit is used to measure the execution time of small code snippets
%time for _ in range(10): my_arr2 = my_arr * 2
#CPU times: user 16.5 ms, sys: 12.1 ms, total: 28.6 ms
%time for _ in range(10): my_list2 = [x * 2 for x in my_list]
#CPU times: user 1.03 s, sys: 212 ms, total: 1.24 s
'''
#The Numpy Array: A Multidimensional Array Object

#create a 1D numpy array
#write this into a @hops component
@hops.component(
    "/numpy_1darray_02",
    name="1D Array",
    description="Create a 1D numpy array",
    inputs=[
        hs.HopsNumber("list", "list", "list of numbers", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("array", "array", "1D numpy array", hs.HopsParamAccess.LIST)
    ]
)
def create_1darray_02(list):   
    arr = np.array(list)
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    print (type(arr))
    return arr

#create a two-dimensional array from two lists
#write this into a @hops component
@hops.component(
    "/numpy_2darray",
    name="2D Array",
    description="Create a 2D numpy array",
    inputs=[
        hs.HopsNumber("list1", "list1", "list of numbers", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "list2", "list of numbers", hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST)
    ]
)
#print(arr.list_to_tree()) not working in grasshopper canvas
#use entwine in gh to convert list to tree
#return arr.tolist()[0] 
def create_2darray(list1, list2):
    arr = np.array([list1, list2])
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    print (type(arr))
    return arr[0], arr[1]
"""
#do not use this structure because it will destroy your datatree information
def array_2D(list1: list, list2: list):
    # Create a two-dimensional array
    listOut = []
    arr = np.array([list1, list2])
    # Print the array
    print(arr)
    arr = arr.tolist()
    print(arr)
    for i in arr:
        listOut.append(i)
    return listOut
"""

#create a three-dimensional array from three lists
#write this into a @hops component
@hops.component(
    "/numpy_3darray",
    name="3D Array",
    description="Create a 3D numpy array",
    inputs=[
        hs.HopsNumber("list1", "list1", "list of numbers", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "list2", "list of numbers", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "list3", "list of numbers", hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST)
    ]
)
def create_3darray(list1, list2, list3):
    arr = np.array([list1, list2, list3])
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    print (type(arr))
    return arr[0], arr[1], arr[2]

#data.shape returns a tuple of integers indicating the size of the array in each dimension
#data.dtype returns an object describing the data type of the array

#do not import with * from numpy import because it will overwrite python functions
#conflicts with things like data.shape and data.dtype, and data.ndim

#Scaling a N-dimensional array
#write this into a @hops component
@hops.component(
    "/numpy_scale",
    name="Scale",
    description="Scale a numpy array",
    inputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("scale", "scale", "scale factor", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST)
    ]
)
def scale(array1, array2, array3, scale):
    arr = np.array([array1, array2, array3])
    print (arr)
    print (type(arr))
    arr = arr * scale
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2]

#Add an array to itself
#write this into a @hops component
@hops.component(
    "/numpy_double",
    name="Double",
    description="Double a numpy array",
    inputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST)
    ]
)
def double(array1, array2, array3):
    arr = np.array([array1, array2, array3])
    print (arr)
    print (type(arr))
    arr = arr + arr
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2]

#add two different arrays together
#write this into a @hops component
@hops.component(
    "/numpy_add",
    name="Add",
    description="Add two numpy arrays",
    inputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array4", "array4", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array5", "array5", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array6", "array6", "1D numpy array", hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST)
    ]
)
def add(array1, array2, array3, array4, array5, array6):
    arr1 = np.array([array1, array2, array3])
    arr2 = np.array([array4, array5, array6])
    print (arr1)
    print (type(arr1))
    print (arr2)
    print (type(arr2))
    arr = arr1 + arr2
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2]

#find the shape of a numpy array from three lists
#write this into a @hops component
@hops.component(
    "/numpy_shape_02",
    name="Shape",
    description="Find the shape of a numpy array",
    inputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def shape_02(array1, array2, array3):
    arr = np.array([array1, array2, array3])
    print (arr)
    print (type(arr))
    shape_arr = arr.shape
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], shape_arr

#find the dtype of a numpy array from three lists
#write this into a @hops component
@hops.component(
    "/numpy_dtype_02",
    name="Dtype",
    description="Find the dtype of a numpy array",
    inputs=[
        hs.HopsNumber("array1", "array1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "1D numpy array", hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "1D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("dtype", "dtype", "dtype of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def dtype_02(array1, array2, array3):
    arr = np.array([array1, array2, array3])
    print (arr)
    print (type(arr))
    dtype_arr = str(arr.dtype)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], dtype_arr

"""
 ██████╗██████╗ ███████╗ █████╗ ████████╗██╗███╗   ██╗ ██████╗     
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝     
██║     ██████╔╝█████╗  ███████║   ██║   ██║██╔██╗ ██║██║  ███╗    
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║██║╚██╗██║██║   ██║    
╚██████╗██║  ██║███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝    
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     
                                                                   
███╗   ██╗██████╗  █████╗ ██████╗ ██████╗  █████╗ ██╗   ██╗███████╗
████╗  ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
██╔██╗ ██║██║  ██║███████║██████╔╝██████╔╝███████║ ╚████╔╝ ███████╗
██║╚██╗██║██║  ██║██╔══██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝  ╚════██║
██║ ╚████║██████╔╝██║  ██║██║  ██║██║  ██║██║  ██║   ██║   ███████║
╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ 
"""
#multi-dimensional numpy array with ndim and shape
#example 1 of a multi-dimensional numpy array
data2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (data2)
arr2 = np.array(data2)
print (arr2.ndim) 
print (arr2.shape)  #returns (3, 3)


#multi-dimensional numpy array with ndim and shape  
#write this into a @hops component
@hops.component(
    "/numpy_ndim_shape_02",
    name="Ndim Shape",
    description="Find the ndim and shape of a numpy array",
    inputs=[
        hs.HopsNumber("array1", "array1", "2D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array2", "array2", "2D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("array3", "array3", "2D numpy array", hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "2D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "2D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "2D numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def ndim_shape_02(array1, array2, array3):
    arr = np.array([array1, array2, array3])
    print (arr)
    print (type(arr))
    ndim_arr = str(arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], ndim_arr, shape_arr

#create a np.zeros and np.ones array
#example 1 of a np.zeros array
data3 = np.zeros(10)
print (data3)
arr3 = np.array(data3)
print (arr3.ndim)
print (arr3.shape)  #returns (10,)
print (arr3.dtype)  #returns float64
data4 = np.ones(10)
print (data4)
arr4 = np.array(data4)
print (arr4.ndim)
print (arr4.shape)  #returns (10,)
print (arr4.dtype)  #returns float64

#write this into a @hops component
@hops.component(
    "/numpy_zeros_02",   
    name="Zeros",
    description="Create a numpy array of zeros",
    inputs=[
        hs.HopsInteger("rows", "rows", "number of rows", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "number of columns", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of zeros", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of zeros", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of zeros", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array of zeros", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def zeros_02(rows: int, columns: int):
    arr = np.zeros((rows, columns))
    print (arr)
    print (type(arr))
    ndim_arr = (arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], arr[3], ndim_arr, shape_arr

#example 1 of a np.ones array
#write this into a @hops component
@hops.component(
    "/numpy_ones",
    name="Ones",
    description="Create a numpy array of ones",
    inputs=[
        hs.HopsInteger("rows", "rows", "number of rows", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "number of columns", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of ones", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of ones", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of ones", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array of ones", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def ones_02(rows: int, columns: int):
    arr = np.ones((rows, columns))
    print (arr)
    print (type(arr))
    ndim_arr = (arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], arr[3], ndim_arr, shape_arr

#avoid using numpy.empty to create an array because it will return an array with random values

#np.arange is similar to range() in python, but returns an array instead of a list
#write this into a @hops component
@hops.component(
    "/numpy_arange_02",
    name="Arange",
    description="Create a numpy array using arange",
    inputs=[
        hs.HopsInteger("count", "count", "number of elements", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("array", "array", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def arange(count: int):
    arr = np.arange(count)
    print (arr)
    print (type(arr))
    ndim_arr = (arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr, ndim_arr, shape_arr

#ones_like, zeros_like, empty_like
#write this into a @hops component
@hops.component(
    "/numpy_ones_like_02",
    name="Ones Like",
    description="Create a numpy array of ones with the same shape and type as a given array",
    inputs=[
        hs.HopsInteger("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of ones", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of ones", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of ones", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def ones_like_02(arr1: int, arr2: int, arr3: int):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    arr3 = np.array(arr3)
    arr = np.ones_like((arr1, arr2, arr3))
    print (arr)
    print (type(arr))
    ndim_arr = (arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], ndim_arr, shape_arr

#zeros_like, empty_like
#write this into a @hops component
@hops.component(
    "/numpy_zeros_like",
    name="Zeros Like",
    description="Create a numpy array of zeros with the same shape and type as a given array",
    inputs=[
        hs.HopsInteger("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM), 
        hs.HopsInteger("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of zeros", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of zeros", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of zeros", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def zeros_like_02(arr1: int, arr2: int, arr3: int):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    arr3 = np.array(arr3)
    arr = np.zeros_like((arr1, arr2, arr3))
    print (arr)
    print (type(arr))
    ndim_arr = (arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], ndim_arr, shape_arr

#empty_like
#write this into a @hops component
@hops.component(
    "/numpy_empty_like",
    name="Empty Like",
    description="Create a numpy array of empty values with the same shape and type as a given array",
    inputs=[
        hs.HopsInteger("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of empty values", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of empty values", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of empty values", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def empty_like_02(arr1: int, arr2: int, arr3: int):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    arr3 = np.array(arr3)
    arr = np.empty_like((arr1, arr2, arr3))
    print (arr)
    print (type(arr))
    ndim_arr = (arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], ndim_arr, shape_arr

#full_like
#write this into a @hops component
@hops.component(
    "/numpy_full_like",
    name="Full Like",
    description="Create a numpy array of a given value with the same shape and type as a given array",
    inputs=[
        hs.HopsInteger("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value", "value", "value to fill array with", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of given value", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of given value", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of given value", hs.HopsParamAccess.LIST),
        hs.HopsString("ndim", "ndim", "ndim of numpy array", hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape of numpy array", hs.HopsParamAccess.LIST)
    ]
)
def full_like_02(arr1: int, arr2: int, arr3: int, value: int):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    arr3 = np.array(arr3)
    arr = np.full_like((arr1, arr2, arr3), value)
    print (arr)
    print (type(arr))
    ndim_arr = (arr.ndim)
    shape_arr = (arr.shape)
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], ndim_arr, shape_arr

#eye, identity array
#write this into a @hops component
@hops.component(
    "/numpy_eye",
    name="Identity Array",
    description="Create a numpy array of ones on the diagonal and zeros elsewhere",
    inputs=[
        hs.HopsInteger("rows", "rows", "number of rows", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "number of columns", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("k", "k", "index of diagonal", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST)
    ]
)
def eye_02(rows: int, columns: int, k: int):
    arr = np.eye(rows, columns, k)
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], arr[3]

#identity array
#write this into a @hops component
@hops.component(
    "/numpy_identity",
    name="Identity Array",
    description="Create a numpy array of ones on the diagonal and zeros elsewhere",
    inputs=[
        hs.HopsInteger("n", "n", "number of rows and columns", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array of ones on the diagonal and zeros elsewhere", hs.HopsParamAccess.LIST)
    ]
)
def identity_02(n: int):
    arr = np.identity(n)
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2], arr[3]

#Data Types for ndarrays
#metadata for the array, such as shape, data type, etc.
#low-level metadata for the data in the array, 
# such as the byte-order, the number of bytes per element, etc.
#C and Fortran order
#type name followed by number of bits per element represents the data-type
#i - integer
#u - unsigned integer
#f - floating-point
#c - complex floating-point
#b - boolean
#object - Python object
#s - string
#U - Unicode string
#V - fixed chunk of memory for other type ( void )
#the number represents the number of bytes in the data-type
#the number can be replaced with the string "int" or "float" 
# to select the smallest data-type needed to represent the integers or floating-point numbers
#the number can also be a number of bits,
# as in the case of complex numbers where the number 
# represents the number of bits in each of the real and imaginary parts

#signed intger types means that the number can be positive or negative
#unsigned integer types means that the number can only be positive

#converting or casting an array from one dtype to another
#write into a @hops component
@hops.component(
    "/numpy_casting",
    name="Casting",
    description="Casting an array from one dtype to another",
    inputs=[
        hs.HopsInteger("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def casting_02(arr1: int, arr2: int, arr3: int):
    arr = np.array([arr1, arr2, arr3])
    print (arr)
    print (type(arr))
    #cast the array into an int type
    arr = arr.astype('i')
    print (arr)
    print (type(arr))
    arr = arr.tolist()
    print (arr)
    return arr[0], arr[1], arr[2]

"""
██╗   ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗ ██╗███████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║╚══███╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║   ██║█████╗  ██║        ██║   ██║   ██║██████╔╝██║  ███╔╝ ███████║   ██║   ██║██║   ██║██╔██╗ ██║
╚██╗ ██╔╝██╔══╝  ██║        ██║   ██║   ██║██╔══██╗██║ ███╔╝  ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
 ╚████╔╝ ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║██║███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
  ╚═══╝  ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

#arithmatic operations on arrays
#express batch operations on data without writing any for loops
#this is called vectorization
#any arithmetic operations between equal-size arrays applies the operation element-wise
#arithmetic operations with scalars propagate the scalar argument to each element in the array
#addtion, subtraction, multiplication, division, exponentiation
#write into a @hops component
@hops.component(
    "/numpy_adding",
    name="Arithmatic",
    description="Arithmatic operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_adding(arr1: int, arr2: int, arr3: int, arr4: int):
    arr1 = np.array([arr1, arr2])
    arr2 = np.array([arr3, arr4])
    print (arr1)
    print (arr2)
    print (arr1 + arr2)
    arr3 = arr1 + arr2
    print (arr3)
    return arr3[0], arr3[1]

#multiplication
#multiplication between arrays is element-wise
#matrix multiplication can be performed using the dot function or method
#write into a @hops component
@hops.component(
    "/numpy_multiplication",
    name="Multiplication",
    description="Multiplication operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_multiplication(arr1: int, arr2: int, arr3: int, arr4: int):
    arr1 = np.array([arr1, arr2])
    arr2 = np.array([arr3, arr4])
    print (arr1)
    print (arr2)
    print (arr1 * arr2)
    arr3 = arr1 * arr2
    print (arr3)
    return arr3[0], arr3[1]

#subtracting
#subtraction between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_subtracting",
    name="Subtracting",
    description="Subtracting operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_subtracting(arr1: int, arr2: int, arr3: int, arr4: int):
    arr1 = np.array([arr1, arr2])
    arr2 = np.array([arr3, arr4])
    print (arr1)
    print (arr2)
    print (arr1 - arr2)
    arr3 = arr1 - arr2
    print (arr3)
    return arr3[0], arr3[1]

#dividing
#division between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_dividing",
    name="Dividing",
    description="Dividing operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_dividing(arr1: int, arr2: int, arr3: int, arr4: int):
    arr1 = np.array([arr1, arr2])
    arr2 = np.array([arr3, arr4])
    print (arr1)
    print (arr2)
    print (arr1 / arr2)
    arr3 = arr1 / arr2
    print (arr3)
    return arr3[0], arr3[1]

#exponentiation and square root and log and trigonometric functions
#and comparison operators and logical operators and bitwise operators and 
#aggregation functions and linear algebra functions and random number generation
#and statistics functions and sorting and searching and reading and writing files
#and working with dates and times and working with strings and working with structured data
#and working with missing data and working with categorical data and working with time series data
#and working with images and working with text data and working with audio data
#and working with video data and working with databases and working with web APIs
#and working with geospatial data and working with big data and working with distributed data
#and working with parallel data and working with GPU data and working with sparse data
#and working with large data and working with streaming data and working with real-time data
#and working with data in the cloud and working with data in the browser and working with data in the terminal
#and working with data in the command line and working with data in the shell and working with data in the console
#and working with data in the editor and working with data in the IDE and working with data in the notebook
#and working with data in the debugger and working with data in the profiler and working with data in the debugger
#and working with data in the profiler and working with data in the debugger and working with data in the profiler
#and working with data in the debugger and working with data in the profiler and working with data in the debugger
#and the list goes on and on...

#exponentiation
#exponentiation between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_exponentiation",
    name="Exponentiation",
    description="Exponentiation operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("expontent", "expontent", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_exponentiation(arr1: int, arr2: int, arr3: int, arr4: int, expontent: int):
    arr = np.array([arr1, arr2, arr3, arr4])
    print (arr)
    arr2 = np.power(arr, expontent)
    print (arr2)
    return arr2[0], arr2[1], arr2[2], arr2[3]

#square root
#square root between arrays is element-wise
#write into a @hops component   
@hops.component(
    "/numpy_square_root",
    name="Square Root",
    description="Square Root operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("sqrt", "sqrt", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_square_root(arr1: int, arr2: int, arr3: int, arr4: int, sqrt: int):
    arr = np.array([arr1, arr2, arr3, arr4])
    print (arr)
    arr2 = np.sqrt(arr)
    print (arr2)
    return arr2[0], arr2[1], arr2[2], arr2[3]

#log
#log between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_log_01",
    name="Log",
    description="Log operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_log_01(arr1: int, arr2: int, arr3: int, arr4: int):
    arr = np.array([arr1, arr2, arr3, arr4])
    print (arr)
    arr2 = np.log(arr)
    print (arr2)
    return arr2[0], arr2[1], arr2[2], arr2[3]

#log base x
#log base x between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_log_base_x",
    name="Log Base X",
    description="Log Base X operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("log_base_x", "log_base_x", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_log_base_x(arr1: int, arr2: int, arr3: int, arr4: int, log_base_x: int):
    arr = np.array([arr1, arr2, arr3, arr4])
    print (arr)
    arr2 = np.log(arr)/np.log(log_base_x)
    print (arr2)
    return arr2[0], arr2[1], arr2[2], arr2[3]

#trigonometric functions
#trigonometric functions between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_sin",
    name="Trigonometric Functions",
    description="Trigonometric Functions operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_trigonometric_functions(arr1: int, arr2: int, arr3: int, arr4: int):
    arr = np.array([arr1, arr2, arr3, arr4])
    print (arr)
    arr2 = np.sin(arr)
    return arr2[0], arr2[1], arr2[2], arr2[3]

#cosine function
#cosine function between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_cos",
    name="Cosine Function",
    description="Cosine Function operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_cosine_function(arr1: int, arr2: int, arr3: int, arr4: int):
    arr = np.array([arr1, arr2, arr3, arr4])
    print (arr)
    arr2 = np.cos(arr)
    return arr2[0], arr2[1], arr2[2], arr2[3]

#tangent function
#secant function
#cosecant function
#cotangent function
#inverse trigonometric functions
#hyperbolic functions
#inverse hyperbolic functions


#rounding
#rounding between arrays is element-wise
#write into a @hops component
@hops.component(
    "/numpy_round",
    name="Rounding",
    description="Rounding operations on arrays",
    inputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("decimals", "decimals", "numpy array", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsNumber("arr1", "arr1", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "numpy array", hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "numpy array", hs.HopsParamAccess.LIST)
    ]
)
def numpy_round(arr1: int, arr2: int, arr3: int, arr4: int, decimals: int):
    arr = np.array([arr1, arr2, arr3, arr4])
    print (arr)
    arr2 = np.round(arr, decimals)
    return arr2[0], arr2[1], arr2[2], arr2[3]

#comparison operators
#comparison operators between arrays is element-wise
#write into a @hops component
#comparison operators
@hops.component(
    "/ndarray_comparison",
    name="ndarray_comparison_operators",
    nickname="ndarray_comparison_operators",
    description="ndarray_comparison_operators",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1"),
        hs.HopsNumber("list2", "l2", "list2"),
        hs.HopsNumber("list3", "l3", "list3"),
        hs.HopsNumber("list4", "l4", "list4")
        ],
    outputs=[
        hs.HopsBoolean("Array1", "A1", "Array of values"),
        hs.HopsBoolean("Array2", "A2", "Array of values")
        ]
)
def ndarray_comparison(list1: list, list2: list, list3: list, list4: list):
        #listOut1 = []
        arr1 = np.array([list1, list2])
        arr2 = np.array([list3, list4])
        # Print the array
        print(arr1)
        print(arr2)
        # Comparison operators the array
        arr3 = np.greater(arr1, arr2)
        # Print the result
        print(arr3)
        arr3 = arr3.tolist()
        return arr3[0], arr3[1]

#less than
#write into a @hops component
@hops.component(
    "/ndarray_less_than",
    name="ndarray_less_than",
    nickname="ndarray_less_than",
    description="ndarray_less_than",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1"),
        hs.HopsNumber("list2", "l2", "list2"),
        hs.HopsNumber("list3", "l3", "list3"),
        hs.HopsNumber("list4", "l4", "list4")
        ],
    outputs=[
        hs.HopsBoolean("Array1", "A1", "Array of values"),
        hs.HopsBoolean("Array2", "A2", "Array of values")
        ]
)
def ndarray_less_than(list1: list, list2: list, list3: list, list4: list):
        #listOut1 = []
        arr1 = np.array([list1, list2])
        arr2 = np.array([list3, list4])
        # Print the array
        print(arr1)
        print(arr2)
        # Comparison operators the array
        arr3 = np.less(arr1, arr2)
        # Print the result
        print(arr3)
        arr3 = arr3.tolist()
        return arr3[0], arr3[1]
    
#less than or equal to
#greate than or equal to
#equal to
#not equal to

#logical operators

#logical_and
#write into a @hops component
@hops.component(
    "/ndarray_logical_and_02",
    name="ndarray_logical_and",
    nickname="ndarray_logical_and",
    description="ndarray_logical_and",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1"),
        hs.HopsNumber("list2", "l2", "list2"),
        hs.HopsNumber("list3", "l3", "list3"),
        hs.HopsNumber("list4", "l4", "list4")
        ],
    outputs=[
        hs.HopsBoolean("Array1", "A1", "Array of values"),
        hs.HopsBoolean("Array2", "A2", "Array of values")
        ]
)
def ndarray_logical_and_02(list1: list, list2: list, list3: list, list4: list):
            arr1 = np.array([list1, list2])
            arr2 = np.array([list3, list4])
            # Print the array
            print(arr1)
            print(arr2)
            # Logical operators the array
            arr3 = np.logical_and(arr1, arr2)
            # Print the result
            print(arr3)
            arr3 = arr3.tolist()
            return arr3[0], arr3[1]

#logical_or
#write into a @hops component
@hops.component(
    "/ndarray_logical_or",
    name="ndarray_logical_or",
    nickname="ndarray_logical_or",
    description="ndarray_logical_or",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1"),
        hs.HopsNumber("list2", "l2", "list2"),
        hs.HopsNumber("list3", "l3", "list3"),
        hs.HopsNumber("list4", "l4", "list4")
        ],
    outputs=[
        hs.HopsBoolean("Array1", "A1", "Array of values"),
        hs.HopsBoolean("Array2", "A2", "Array of values")
        ]
)
def ndarray_logical_or(list1: list, list2: list, list3: list, list4: list):
            arr1 = np.array([list1, list2])
            arr2 = np.array([list3, list4])
            # Print the array
            print(arr1)
            print(arr2)
            # Logical operators the array
            arr3 = np.logical_or(arr1, arr2)
            # Print the result
            print(arr3)
            arr3 = arr3.tolist()
            return arr3[0], arr3[1]

#logical_not
#logical_xor

#aggregation functions and linear algebra functions and random number generation
#and statistics functions and sorting and searching and reading and writing files
#and working with dates and times and working with strings and working with structured data
#and working with missing data and working with categorical data and working with time series data
#and working with images and working with text data and working with audio data
#and working with video data and working with databases and working with web APIs
#and working with geospatial data and working with big data and working with distributed data
#and working with parallel data and working with GPU data and working with sparse data
#and working with large data and working with streaming data and working with real-time data
#and working with data in the cloud and working with data in the browser and working with data in the terminal
#and working with data in the command line and working with data in the shell and working with data in the console
#and working with data in the editor and working with data in the IDE and working with data in the notebook
#and working with data in the debugger and working with data in the profiler and working with data in the debugger
#and working with data in the profiler and working with data in the debugger and working with data in the profiler
#and working with data in the debugger and working with data in the profiler and working with data in the debugger
#and the list goes on and on...

"""
██╗███╗   ██╗██████╗ ███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝██║████╗  ██║██╔════╝ 
██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝ ██║██╔██╗ ██║██║  ███╗
██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗ ██║██║╚██╗██║██║   ██║
██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗██║██║ ╚████║╚██████╔╝
╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""
#Indexing and Slicing
#selecting a subset of any data structure in Python is called slicing
#slicing is a very powerful tool that allows you to select a subset 
# of data from a data structure

#one-dimensional arrays work the same way as lists
#two-dimensional arrays work the same way as lists of lists
#three-dimensional arrays work the same way as lists of lists of lists
#and so on and so forth
#N-dimensional arrays work the same way

#Indexing one-dimensional arrays
#write into a @hops component
@hops.component(
    "/ndarray_indexing_01",
    name="ndarray_indexing",
    nickname="ndarray_indexing",
    description="ndarray_indexing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_indexing_01(list1: list):
    arr = np.array(list1)
    return arr[0:5:2].tolist()

@hops.component(
    "/ndarray_indexing_04",
    name="ndarray_indexing",
    nickname="ndarray_indexing",
    description="ndarray_indexing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start", "s", "start", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("stop", "s", "stop", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("step", "s", "step", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_indexing_04(list1: list, start: int, stop: int, step: int):
    arr = np.array(list1)
    return arr[start:stop:step].tolist()

#slicing
#write into a @hops component
@hops.component(
    "/ndarray_slicing_01",
    name="ndarray_slicing",
    nickname="ndarray_slicing",
    description="ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_slicing_01(list1: list):
    arr = np.array(list1)
    arr_slice = arr[2:6]
    arr_slice[1] = 12345
    return arr_slice.tolist()

@hops.component(
    "/ndarray_slicing_02",
    name="ndarray_slicing",
    nickname="ndarray_slicing",
    description="ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start", "s", "start", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("stop", "s", "stop", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index", "i", "index", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("value", "v", "value", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_slicing_02(list1: list, start: int, stop: int, index: int, value: float):
    arr = np.array(list1)
    arr_slice = arr[start:stop]
    arr_slice[index] = value
    return arr_slice.tolist()

#bare slice [:] will assign to all values in the original array
#write into a @hops component
@hops.component(
    "/ndarray_slicing_03",
    name="ndarray_slicing",
    nickname="ndarray_slicing",
    description="ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_slicing_03(list1: list):
    arr = np.array(list1)
    arr_slice = arr[2:6]
    arr_slice[:] = 64
    return arr_slice.tolist()

@hops.component(
    "/ndarray_slicing_04",
    name="ndarray_slicing",
    nickname="ndarray_slicing",
    description="ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start", "s", "start", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("stop", "s", "stop", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("value", "v", "value", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_slicing_04(list1: list, start: int, stop: int, value: float):
    arr = np.array(list1)
    arr_slice = arr[start:stop]
    arr_slice[:] = value
    return arr_slice.tolist()

#must explicitly copy the array or slice to avoid modifying the original array
#write into a @hops component
@hops.component(
    "/ndarray_slicing_05",
    name="ndarray_slicing",
    nickname="ndarray_slicing",
    description="ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_slicing_05(list1: list):
    arr = np.array(list1)
    arr_slice = arr[2:6].copy()
    arr_slice[:] = 64
    return arr_slice.tolist()

@hops.component(
    "/ndarray_slicing_06",
    name="ndarray_slicing",
    nickname="ndarray_slicing",
    description="ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start", "s", "start", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("stop", "s", "stop", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("value", "v", "value", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_slicing_06(list1: list, start: int, stop: int, value: float):
    arr = np.array(list1)
    arr_slice = arr[start:stop].copy()
    arr_slice[:] = value
    return arr_slice.tolist()

#Higher dimensional arrays
#two-dimensional arrays work the same way as lists of lists
#the elements at each index are no longer scalars but rather one-dimensional arrays
#think of the axis 0 as the rows of the array and axis 1 as the columns of the array
#write into a @hops component
@hops.component(
    "/2d_ndarray_indexing_03",
    name="2d_ndarray_indexing",
    nickname="2d_ndarray_indexing",
    description="2d_ndarray_indexing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsInteger("index", "i", "index", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.LIST),
        hs.HopsNumber("Array2", "A2", "Array of values", hs.HopsParamAccess.LIST),
        hs.HopsNumber("Array3", "A3", "Array of values", hs.HopsParamAccess.LIST)
        ]
)
def ndarray_indexing_03(list1: list, list2: list, list3: list, index: int):
    arr2d = np.array([list1, list2, list3])
    arr2d_slice = arr2d[index]
    return arr2d_slice[0], arr2d_slice[1], arr2d_slice[2]



@hops.component(
    "/2d_ndarray_indexing_05",
    name="2d_ndarray_indexing",
    nickname="2d_ndarray_indexing",
    description="2d_ndarray_indexing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsInteger("index", "i", "index", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("element", "e", "element", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_indexing_05(list1: list, list2: list, list3: list, index: int, element: int):
    arr2d = np.array([list1, list2, list3])
    arrOut = arr2d[index][element]
    return arrOut

#in multidimensional arrays, if you omit later indices, 
# the returned object will be a lower dimensional ndarray 
# consisting of all the data along the higher dimensions

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print (arr3d)
print (arr3d[0])

#both scalar values and arrays can be assigned to arr3d[0]
old_values = arr3d[0].copy()
arr3d[0] = 42
print (arr3d)
arr3d[0] = old_values
print (arr3d)

#similarly, arr3d[1, 0] gives you all of the values whose indices
# start with (1, 0), forming a 1-dimensional array
print (arr3d[1, 0])

#write into a @hops component
@hops.component(
    "/3d_ndarray_indexing_02c",
    name="3d_ndarray_indexing",
    nickname="3d_ndarray_indexing",
    description="3d_ndarray_indexing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "i1", "index1", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "i2", "index2", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_indexing_02c(list1: list, list2: list, list3: list, list4: list, index1: int, index2: int):
    arr3d = np.array([[list1, list2], [list3, list4]])
    arrOut = arr3d[index1, index2]
    arrOut = arrOut.tolist()
    return arrOut

#this expression is the same as above
x = arr3d[1]
print (x[0])

#write into a @hops component
@hops.component(
    "/3d_ndarray_indexing_02d",
    name="3d_ndarray_indexing",
    nickname="3d_ndarray_indexing",
    description="3d_ndarray_indexing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "i1", "index1", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "i2", "index2", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("element", "e", "element", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_indexing_02d(list1: list, list2: list, list3: list, list4: list, index1: int, index2: int, element: int):
    arr3d = np.array([[list1, list2], [list3, list4]])
    arrOut = arr3d[index1, index2][element]
    return arrOut


#note that where subsections of the array have been selected,
# the returned arrays are views

#note the multidimensional slicing syntax for NumPy arrays
#will not work on Python lists

#Multidimensional arrays
#slicing multidimensional arrays is a bit of a pain
#the colon means take the entire axis
#the comma separates slices along each axis 
#so you can select a lower dimensional slice by doing
#arr2d[:2, 1:]  
#which is the first two rows and columns from index 1 onwards

#create a 2x2x3 array of random integers between 0 and 10 with a @hops component
#example
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print (arr3d)
#slice out the first 2x2x2 chunk
arr3d[:2, :2, :2]
print (arr3d[:2, :2, :2])
#write into a @hops component
@hops.component(
    "/3d_ndarray_slicing_01c",
    name="3d_ndarray_slicing",
    nickname="3d_ndarray_slicing",
    description="3d_ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "i1", "index1", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "i2", "index2", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_slicing_01c(list1: list, list2: list, list3: list, list4: list, index1: int, index2: int):
    arr3d = np.array([[list1, list2], [list3, list4]])
    arrOut = arr3d[:2, :2, :2]
    arrOut = arrOut[index1, index2]
    arrOut = arrOut.tolist()
    return arrOut
    
@hops.component(
    "/3d_ndarray_slicing_01e",
    name="3d_ndarray_slicing",
    nickname="3d_ndarray_slicing",
    description="3d_ndarray_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "i1", "index1", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "i2", "index2", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "i3", "index3", hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values", hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_slicing_01e(list1: list, list2: list, list3: list, list4: list, index1: int, index2: int, index3: int):
    arr3d = np.array([[list1, list2], [list3, list4]])
    arrOut = arr3d[:index3, :index3, :index3]
    arrOut = arrOut[index1, index2]
    arrOut = arrOut.tolist()
    return arrOut

#indexing with slices
# like one-dimensional objects such as Python lists, ndarrays can be sliced 
# with the familiar syntax,
# though now you can slice one or more axes

arr = np.arange(10)
print (arr)
print (arr[5:8])

#slicing a two-dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (arr2d)
print (arr2d[:2])
# this means "select the first two rows of arr2d and all of the columns from each"
print (arr2d[:2, 1:])
# this means "select the first two rows of arr2d and all of the columns from each"
# and then select columns 1 and 2
print (arr2d[1, :2])
# this means "select the second row of arr2d and all of the columns from each"
# and then select columns 0 and 1
print (arr2d[:2, 2])
# means "select the first two rows of arr2d and all of the columns from each"
# and then select column 2

#lower dimensional slices are views of the higher dimensional array
lower_dim_slice = arr2d[1, :2]
print (lower_dim_slice)
#means "select the second row of arr2d and all of the columns from each"
# and then select columns 0 and 1

#arr[:2, 2]
#means "select the first two rows of arr2d and all of the columns from each"
# and then select column 2

#apply this to a @hops.component
@hops.component(
    "/ndarray_indexSlice_2b",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start", "s", "start"),
        hs.HopsInteger("end", "e", "end")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_2b(list1: list, start: int, end: int):
        arr = np.array(list1)
        print (arr)
        print (arr[start:end])
        #return arr[start:end] as a list
        arrOut = arr[start:end].tolist()
        return arrOut
        '''
        listOut = []
        for i in arr[start:end]:
            listOut.append(i)
        return listOut
        '''

#accessed recursively
@hops.component(
    "/ndarray_indexSlice_4",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start0", "s0", "start0"),
        hs.HopsInteger("end0", "e0", "end0")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_4(list1: list, list2: list, list3: list, start0: int, end0: int):
        arr2d = np.array([list1, list2, list3])
        print (arr2d)
        print (arr2d[start0:end0])
        #return arr2d[start0:end0] as a list
        listOut = []
        listOut.append(arr2d[start0][end0])
        return listOut

@hops.component(
    "/ndarray_indexSlice_6",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start0", "s0", "start0"),
        hs.HopsInteger("end0", "e0", "end0"),
        hs.HopsInteger("start1", "s1", "start1"),
        hs.HopsInteger("end1", "e1", "end1")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_6(list1: list, list2: list, list3: list, start0: int, end0: int, start1: int, end1: int):
        arr2d = np.array([list1, list2, list3])
        print (arr2d)
        print (arr2d[start0:end0, start1:end1])
        #return arr2d[start0:end0, start1:end1] as a list
        listOut = []
        for i in arr2d[start0:end0, start1:end1]:
            for j in i:
                listOut.append(j)
        return listOut

@hops.component(
    "/ndarray_indexSlice_6b",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start1", "s1", "start1"),
        hs.HopsInteger("end1", "e1", "end1")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values")
        ]
)
def ndarray_indexSlice_6b(list1: list, list2: list, list3: list, start1: int, end1: int): 
        arr2d = np.array([list1, list2, list3])
        print (arr2d)
        print (arr2d[0:3, start1:end1])
        #return arr2d[start0:end0, start1:end1] as a list
        arrOut1 = arr2d[0:3, start1:end1][0]
        arrOut2 = arr2d[0:3, start1:end1][1]
        arrOut3 = arr2d[0:3, start1:end1][2]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist()

        '''
        listOut = []
        for i in arr2d[start0:end0, start1:end1]:
            for j in i:
                listOut.append(j)
        return listOut'''

#use a step size
@hops.component(
    "/ndarray_indexSlice_8",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start", "s", "start"),
        hs.HopsInteger("end", "e", "end"),
        hs.HopsInteger("step", "st", "step")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_8(list1: list, start: int, end: int, step: int):
        arr = np.array(list1)
        print (arr)
        print (arr[start:end:step])
        #return arr[start:end:step] as a list
        listOut = []
        for i in arr[start:end:step]:
            listOut.append(i)
        return listOut

#use a step size
@hops.component(
    "/ndarray_indexSlice_8c",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start", "s", "start"),
        hs.HopsInteger("end", "e", "end"),
        hs.HopsInteger("step", "st", "step")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_8c(list1: list, start: int, end: int, step: int):
        arr = np.array(list1)
        print (arr)
        print (arr[start:end:step])
        #return arr[start:end:step] as a list
        arrOut = arr[start:end:step].tolist()
        return arrOut

#use a step size on a 2d array
@hops.component(
    "/ndarray_indexSlice_10",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start0", "s0", "start0"),
        hs.HopsInteger("end0", "e0", "end0"),
        hs.HopsInteger("step0", "st0", "step0"),
        hs.HopsInteger("start1", "s1", "start1"),
        hs.HopsInteger("end1", "e1", "end1"),
        hs.HopsInteger("step1", "st1", "step1")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_10(list1: list, list2: list, list3: list, start0: int, end0: int, step0: int, start1: int, end1: int, step1: int):
        arr2d = np.array([list1, list2, list3])
        print (arr2d)
        print (arr2d[start0:end0:step0, start1:end1:step1])
        #return arr2d[start0:end0:step0, start1:end1:step1] as a list
        listOut = []
        for i in arr2d[start0:end0:step0, start1:end1:step1]:
            for j in i:
                listOut.append(j)
        return listOut

#use a step size on a 2d array
@hops.component(
    "/ndarray_indexSlice_10d",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start1", "s1", "start1"),
        hs.HopsInteger("end1", "e1", "end1"),
        hs.HopsInteger("step1", "st1", "step1")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values")
        ]
)
def ndarray_indexSlice_10d(list1: list, list2: list, list3: list, start1: int, end1: int, step1: int):
        arr2d = np.array([list1, list2, list3])
        print (arr2d)
        #return arr2d[start0:end0:step0, start1:end1:step1] as a list
        arrOut1 = arr2d[0:3:1, start1:end1:step1][0]
        arrOut2 = arr2d[0:3:1,  start1:end1:step1][1]
        arrOut3 = arr2d[0:3:1,  start1:end1:step1][2]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist()     

#3d array with 4 lists of 3 elements each
@hops.component(
    "/ndarray_indexSlice_19",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_19(list1: list, list2: list, list3: list, list4: list):
        arr3d = np.array([[list1, list2], [list3, list4]])
        print (arr3d)
        listOut = []
        for i in arr3d:
            for j in i:
                for k in j:
                    listOut.append(k)
        return listOut

#3d array with 4 lists of 3 elements each
@hops.component(
    "/ndarray_indexSlice_19d",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values"),
        hs.HopsNumber("Array4", "A4", "Array of values")
        ]
)
def ndarray_indexSlice_19d(list1: list, list2: list, list3: list, list4: list):
        arr3d = np.array([[list1, list2], [list3, list4]])
        print (arr3d)
        arrOut1 = arr3d[0][0]
        arrOut2 = arr3d[0][1]
        arrOut3 = arr3d[1][0]
        arrOut4 = arr3d[1][1]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist(), arrOut4.tolist()
'''
#use a step size on a 3d array
@hops.component(
    "/ndarray_indexSlice_20b",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("start1", "s1", "start1"),
        hs.HopsInteger("end1", "e1", "end1"),
        hs.HopsInteger("step1", "st1", "step1")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values"),
        hs.HopsNumber("Array4", "A4", "Array of values")
        ]
)
def ndarray_indexSlice_20b(list1: list, list2: list, list3: list, list4: list, start1: int, end1: int, step1: int):
        arr3d = np.array([[list1, list2], [list3, list4]])
        print (arr3d)
        #return arr3d[start0:end0:step0, start1:end1:step1] as a list
        arrOut1 = arr3d[0:2:1, start1:end1:step1][0][0]
        arrOut2 = arr3d[0:2:1, start1:end1:step1][0][1]
        arrOut3 = arr3d[0:2:1, start1:end1:step1][1][0]
        arrOut4 = arr3d[0:2:1, start1:end1:step1][1][1]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist(), arrOut4.tolist()
'''
#use a step size on a 3d array
@hops.component(
    "/ndarray_indexSlice_20f",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("element", "e", "element")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values"),
        hs.HopsNumber("Array4", "A4", "Array of values")
        ]
)
def ndarray_indexSlice_20f(list1: list, list2: list, list3: list, list4: list, element: int):
        arr3d = np.array([[list1, list2], [list3, list4]])
        print (arr3d)
        #return arr3d[start0:end0:step0, start1:end1:step1] as a list
        arrOut1 = arr3d[0:2:1, 0:3:1][0][0][element]
        arrOut2 = arr3d[0:2:1, 0:3:1][0][1][element]
        arrOut3 = arr3d[0:2:1, 0:3:1][1][0][element]
        arrOut4 = arr3d[0:2:1, 0:3:1][1][1][element]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist(), arrOut4.tolist()

#use a step size on a 3d array
@hops.component(
    "/ndarray_indexSlice_20g",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("eS", "eS", "eS"),
        hs.HopsInteger("eE", "eE", "eE")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values"),
        hs.HopsNumber("Array4", "A4", "Array of values")
        ]
)
def ndarray_indexSlice_20g(list1: list, list2: list, list3: list, list4: list, eS: int, eE: int):
        arr3d = np.array([[list1, list2], [list3, list4]])
        print (arr3d)
        #return arr3d[start0:end0:step0, start1:end1:step1] as a list
        arrOut1 = arr3d[0:2:1, 0:3:1][0][0][eS:eE]
        arrOut2 = arr3d[0:2:1, 0:3:1][0][1][eS:eE]
        arrOut3 = arr3d[0:2:1, 0:3:1][1][0][eS:eE]
        arrOut4 = arr3d[0:2:1, 0:3:1][1][1][eS:eE]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist(), arrOut4.tolist()

#use a step size on a 3d array
@hops.component(
    "/ndarray_indexSlice_20h",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("eS", "eS", "eS"),
        hs.HopsInteger("eE", "eE", "eE")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values"),
        hs.HopsNumber("Array4", "A4", "Array of values")
        ]
)
def ndarray_indexSlice_20h(list1: list, list2: list, list3: list, list4: list, eS: int, eE: int):
        arr3d = np.array([[list1, list2], [list3, list4]])
        print (arr3d)
        #return arr3d[start0:end0:step0, start1:end1:step1] as a list
        arrOut1 = arr3d[0][0][eS:eE]
        arrOut2 = arr3d[0][1][eS:eE]
        arrOut3 = arr3d[1][0][eS:eE]
        arrOut4 = arr3d[1][1][eS:eE]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist(), arrOut4.tolist()

#use a step size on a 3d array
@hops.component(
    "/ndarray_indexSlice_20m",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST),
        hs.HopsInteger("eS", "eS", "eS"),
        hs.HopsInteger("eE", "eE", "eE"),
        hs.HopsInteger("step", "st", "step")
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values"),
        hs.HopsNumber("Array3", "A3", "Array of values"),
        hs.HopsNumber("Array4", "A4", "Array of values")
        ]
)
def ndarray_indexSlice_20m(list1: list, list2: list, list3: list, list4: list, eS: int, eE: int, step: int):
        arr3d = np.array([[list1, list2], [list3, list4]])
        print (arr3d)
        #return arr3d[start0:end0:step0, start1:end1:step1] as a list
        arrOut1 = arr3d[0][0][eS:eE:step]
        arrOut2 = arr3d[0][1][eS:eE:step]
        arrOut3 = arr3d[1][0][eS:eE:step]
        arrOut4 = arr3d[1][1][eS:eE:step]
        return arrOut1.tolist(), arrOut2.tolist(), arrOut3.tolist(), arrOut4.tolist()

'''
██████╗  ██████╗  ██████╗ ██╗     ███████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔═══██╗██║     ██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██║   ██║██║     █████╗  ███████║██╔██╗ ██║
██╔══██╗██║   ██║██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║
██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║██║ ╚████║
╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                            
██╗███╗   ██╗██████╗ ███████╗██╗  ██╗██╗███╗   ██╗ ██████╗  
██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝██║████╗  ██║██╔════╝  
██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝ ██║██╔██╗ ██║██║  ███╗ 
██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗ ██║██║╚██╗██║██║   ██║ 
██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗██║██║ ╚████║╚██████╔╝ 
╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝  
'''

#Boolean Indexing
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.array([[7,4], [0, 2], [-5, 6], [3, -4], [0, -1], [-2, 3], [2, 3]])
print (names)
print (data)
print (names == 'Bob')
print (data[names == 'Bob'])
print (data[names == 'Bob', 1:])
print (data[names == 'Bob', 1])
print (~ (names == 'Bob'))
print (data[~ (names == 'Bob')])

#the ~ operator can be used to invert the condition

cond = names == 'Bob'
print (data[~cond])

#& and | can be used to combine multiple boolean arrays
mask = (names == 'Bob') | (names == 'Will')
print (mask)
print (data[mask])
#always creates a copy of the data and does not modify the original array
#python keywords and and or do not work with boolean arrays

#to set all of the negative values in data to 0, we 
#can combine boolean indexing with standard indexing
data[data < 0] = 0
print (data)

#set a whole row or column using a 1d boolean array
data[names != 'Joe'] = 7
print (data)
#convenient to do with pandas

#Boolean indexing with @hops.component
@hops.component(
    "/ndarray_indexSlice_22",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsString("name", "n", "name", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values")
        ]
)
def ndarray_indexSlice_22(name: str, list1: list, list2: list, list3: list, list4: list):
        names = np.array(name)
        data = np.array([list1, list2, list3, list4])
        print (names)
        print (data)
        print (names == 'Bob')
        listOut = []
        for i in data[names == 'Bob']:
            for j in i:
                listOut.append(j)
        return listOut

#Boolean indexing with @hops.component
@hops.component(
    "/ndarray_indexSlice_22b",
    name="ndarray_indexing_and_slicing",
    nickname="ndarray_indexing_and_slicing",
    description="ndarray_indexing_and_slicing",
    inputs=[
        hs.HopsString("name", "n", "name", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list1", "l1", "list1", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "l2", "list2", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list3", "l3", "list3", hs.HopsParamAccess.LIST),
        hs.HopsNumber("list4", "l4", "list4", hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("Array1", "A1", "Array of values"),
        hs.HopsNumber("Array2", "A2", "Array of values")
        ]
)
def ndarray_indexSlice_22b(name: str, list1: list, list2: list, list3: list, list4: list):
        names = np.array(name)
        data = np.array([list1, list2, list3, list4])
        print (names)
        print (data)
        print (names == 'Bob')
        arrOut = data[names == 'Bob'].tolist()
        return arrOut[0], arrOut[1]


        #the ~ operator can be used to invert the condition

        cond = names == 'Bob'
        print (data[~cond])

        #& and | can be used to combine multiple boolean arrays
        mask = (names == 'Bob') | (names == 'Will')
        print (mask)
        print (data[mask])
        #always creates a copy of the data and does not modify the original array
        #python keywords and and or do not work with boolean arrays

        #to set all of the negative values in data to 0, we 
        #can combine boolean indexing with standard indexing
        data[data < 0] = 0
        print (data)

        #set a whole row or column using a 1d boolean array
        data[names != 'Joe'] = 7
        print (data)
        #convenient to do with pandas

        listOut = []
        for i in data:
            for j in i:
                listOut.append(j)
        return listOut

#~ operator
# mask = (names == 'Bob') | (names == 'Will')
# & and | can be used to combine multiple boolean arrays

#set negative values to 0
data = np.array([[-7,4], [0, -2], [-5, 6], [3, -4], [0, -1], [-2, 3], [-2, 3]])
data[data < 0] = 0  
print (data)


#Fancy Indexing
#is a term adopted by NumPy to describe indexing using integer arrays
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print (arr) #returns an 8x4 array of integers from 0 to 7
#pass a list or ndarray of integers specifying the desired order
print (arr[[4, 3, 0, 6]])
#pass negative indices
print (arr[[-3, -5, -7]])
#using fancy indexing, the shape of the result reflects the shape of 
# the index arrays rather than the shape of the array being indexed
arr = np.arange(32).reshape((8, 4))
print (arr)
print (arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print (arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
#fancy indexing, unlike slicing, always copies the data into a new array
#example of fancy indexing
print("")
arr[[1, 5, 7, 2],[0, 3, 1, 2]] = 0
print (arr)

#Transposing Arrays and Swapping Axes
#special attribute, T, to transpose a matrix
arr = np.arange(15).reshape((3, 5))
print (arr)
print (arr.T)
#computing the inner matrix product using np.dot
arr = np.random.randn(6, 3)
print (arr)
print (np.dot(arr.T, arr))
#@ operator for matrix multiplication
print (arr.T @ arr)


@hops.component(
    "/ndarray_fancyIndexing_3",
    name="ndarray_fancyIndexing",
    nickname="ndarray_fancyIndexing",
    description="ndarray_fancyIndexing",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST)
        ]
)   
def ndarray_fancyIndexing_3(rows: int, columns: int):
    arr = np.zeros((rows, columns))
    for i in range(rows):
        arr[i] = i
    print(arr)
    print(arr.tolist())
    print(arr.tolist()[0])
    print(arr.tolist()[1])
    print(arr.tolist()[2])
    #print(arr.list_to_tree()) not working in grasshopper canvas
    # use entwine node in gh to convert lists to tree
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2]
  
#transpsing and swapping axes
@hops.component(
    "/ndarray_transpose",
    name="ndarray_transpose",
    nickname="ndarray_transpose",
    description="ndarray_transpose",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L4", "L4", "L4", access = hs.HopsParamAccess.LIST)
        ]
)   
def ndarray_transpose(rows: int, columns: int):
    arr = np.arange(15).reshape((rows, columns))
    print(arr)
    arrTranspose = arr.T
    print(arrTranspose)
    print(arrTranspose.tolist())
    print(arrTranspose.tolist()[0])
    print(arrTranspose.tolist()[1])
    print(arrTranspose.tolist()[2])
    print(arrTranspose.tolist()[3])
    print(arrTranspose.tolist()[4])
    #print(arr.list_to_tree()) not working in grasshopper canvas
    # use entwine node in gh to convert lists to tree
    return arrTranspose.tolist()[0], arrTranspose.tolist()[1], arrTranspose.tolist()[2], arrTranspose.tolist()[3], arrTranspose.tolist()[4]

#@ operator for matrix multiplication
@hops.component(
    "/ndarray_matrixMultiplication_3",
    name="ndarray_matrixMultiplication",
    nickname="ndarray_matrixMultiplication",
    description="ndarray_matrixMultiplication",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L4", "L4", "L4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_matrixMultiplication_3(rows: int, columns: int):
    arr = np.arange(15).reshape((rows, columns))
    print(arr)
    print(arr.T)
    arrMult = arr.T @ arr
    print(arrMult)
    return arrMult.tolist()[0], arrMult.tolist()[1], arrMult.tolist()[2], arrMult.tolist()[3], arrMult.tolist()[4]

#swapaxes method takes a pair of axis numbers and switches the 
#indicated axes to rearrange the data
arr = np.arange(16).reshape((2, 2, 4))
print (arr)
print (arr.swapaxes(1, 2))
#swapaxes similarly returns a view on the data without making a copy

#swapaxes method takes a pair of axis numbers and switches the
#indicated axes to rearrange the data
@hops.component(
    "/ndarray_swapaxes2",
    name="ndarray_swapaxes",
    nickname="ndarray_swapaxes",
    description="ndarray_swapaxes",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsInteger("axis1", "a1", "axis1"),
        hs.HopsInteger("axis2", "a2", "axis2")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_swapaxes2(rows: int, columns: int, axis1: int, axis2: int):
    arr = np.arange(15).reshape((rows, columns))
    print(arr)
    print(arr.swapaxes(axis1, axis2))
    return arr.swapaxes(axis1, axis2).tolist()[0], arr.swapaxes(axis1, axis2).tolist()[1], arr.swapaxes(axis1, axis2).tolist()[2]

"""
██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ███╗                            
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗ ████║                            
██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔████╔██║                            
██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╔╝██║                            
██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚═╝ ██║                            
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝                            
                                                                                  
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗                             
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗                            
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝                            
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗                            
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║                            
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                            
                                                                                  
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""
#pseudo-random number generation
#example of generating a 4x4 array of samples from the standard normal distribution
#write into a @hops component
@hops.component(
    "/ndarray_random_1",
    name="ndarray_random",
    nickname="ndarray_random",
    description="ndarray_random",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_1(rows: int, columns: int):
    samples = np.random.standard_normal((rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#use an explicit seed to make the output deterministic
@hops.component(
    "/ndarray_random_seed",
    name="ndarray_random_seed",
    nickname="ndarray_random_seed",
    description="ndarray_random_seed",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsInteger("seed", "s", "seed")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_seed(rows: int, columns: int, seed: int):    
    np.random.seed(seed)
    samples = np.random.standard_normal((rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#numpy random number generation functions
#permutations
@hops.component(
    "/ndarray_random_permutations",
    name="ndarray_random_permutations",
    nickname="ndarray_random_permutations",
    description="ndarray_random_permutations",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_permutations(rows: int, columns: int):
    arr = np.arange(16).reshape((rows, columns))
    print (arr)
    print (np.random.permutation(arr))
    return np.random.permutation(arr).tolist()[0], np.random.permutation(arr).tolist()[1], np.random.permutation(arr).tolist()[2], np.random.permutation(arr).tolist()[3]

#shuffle
@hops.component(
    "/ndarray_random_shuffle",
    name="ndarray_random_shuffle",
    nickname="ndarray_random_shuffle",
    description="ndarray_random_shuffle",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsInteger("seed", "s", "seed")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_shuffle(rows: int, columns: int, seed: int):
    arr = np.arange(16).reshape((rows, columns))
    print (arr)
    np.random.seed(seed)
    np.random.shuffle(arr)
    print (arr)
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2], arr.tolist()[3]

#uniform
@hops.component(
    "/ndarray_random_uniform",
    name="ndarray_random_uniform",
    nickname="ndarray_random_uniform",
    description="ndarray_random_uniform",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsInteger("low", "l", "low"),
        hs.HopsInteger("high", "h", "high")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_uniform(rows: int, columns: int, low: int, high: int):
    samples = np.random.uniform(low, high, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#ingeters
@hops.component(
    "/ndarray_random_integers",
    name="ndarray_random_integers",
    nickname="ndarray_random_integers",
    description="ndarray_random_integers",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsInteger("low", "l", "low"),
        hs.HopsInteger("high", "h", "high")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_integers(rows: int, columns: int, low: int, high: int):  
    samples = np.random.randint(low, high, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#binomial
@hops.component(
    "/ndarray_random_binomial",
    name="ndarray_random_binomial",
    nickname="ndarray_random_binomial",
    description="ndarray_random_binomial",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),    
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsInteger("n", "n", "n"),
        hs.HopsNumber("p", "p", "p")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_binomial(rows: int, columns: int, n: int, p: float):
    samples = np.random.binomial(n, p, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#beta
@hops.component(
    "/ndarray_random_beta",
    name="ndarray_random_beta",
    nickname="ndarray_random_beta",
    description="ndarray_random_beta",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsNumber("a", "a", "a"),
        hs.HopsNumber("b", "b", "b")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_beta(rows: int, columns: int, a: float, b: float):
    samples = np.random.beta(a, b, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#chisquare
@hops.component(
    "/ndarray_random_chisquare",
    name="ndarray_random_chisquare",
    nickname="ndarray_random_chisquare",
    description="ndarray_random_chisquare",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsInteger("df", "df", "df")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_chisquare(rows: int, columns: int, df: int):
    samples = np.random.chisquare(df, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#gamma
@hops.component(
    "/ndarray_random_gamma",
    name="ndarray_random_gamma",
    nickname="ndarray_random_gamma",
    description="ndarray_random_gamma",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsNumber("shape", "s", "shape"),
        hs.HopsNumber("scale", "s", "scale")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_gamma(rows: int, columns: int, shape: float, scale: float):
    samples = np.random.gamma(shape, scale, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#laplace
@hops.component(
    "/ndarray_random_laplace",
    name="ndarray_random_laplace",
    nickname="ndarray_random_laplace",
    description="ndarray_random_laplace",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsNumber("loc", "l", "loc"),
        hs.HopsNumber("scale", "s", "scale")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_laplace(rows: int, columns: int, loc: float, scale: float):
    samples = np.random.laplace(loc, scale, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#logistic
@hops.component(
    "/ndarray_random_logistic", 
    name="ndarray_random_logistic",
    nickname="ndarray_random_logistic",
    description="ndarray_random_logistic",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsNumber("loc", "l", "loc"),
        hs.HopsNumber("scale", "s", "scale")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_logistic(rows: int, columns: int, loc: float, scale: float):
    samples = np.random.logistic(loc, scale, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]

#lognormal
@hops.component(
    "/ndarray_random_lognormal",
    name="ndarray_random_lognormal",
    nickname="ndarray_random_lognormal",
    description="ndarray_random_lognormal",
    inputs=[
        hs.HopsInteger("rows", "r", "rows"),
        hs.HopsInteger("columns", "c", "columns"),
        hs.HopsNumber("mean", "m", "mean"),
        hs.HopsNumber("sigma", "s", "sigma")
        ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST)        
            ]
)
def ndarray_random_lognormal(rows: int, columns: int, mean: float, sigma: float):
    samples = np.random.lognormal(mean, sigma, size=(rows, columns))
    print(samples)
    return samples.tolist()[0], samples.tolist()[1], samples.tolist()[2], samples.tolist()[3]


"""
██╗   ██╗███╗   ██╗██╗██╗   ██╗███████╗██████╗ ███████╗ █████╗ ██╗         
██║   ██║████╗  ██║██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║         
██║   ██║██╔██╗ ██║██║██║   ██║█████╗  ██████╔╝███████╗███████║██║         
██║   ██║██║╚██╗██║██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══██║██║         
╚██████╔╝██║ ╚████║██║ ╚████╔╝ ███████╗██║  ██║███████║██║  ██║███████╗    
 ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝    
                                                                           
███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗ 
██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝ 
█████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗ 
██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║ 
██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║ 
╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ 
"""
#Univeral Functions : Fast Element-Wise Array Functions
#a universal function (or ufunc for short) is a function 
# that operates on ndarrays in an element-by-element fashion, 
# supporting array broadcasting, type casting, 
# and several othe"r standard features.
#Many ufuncs are simple element-wise transformations,
# like sqrt or exp

arr = np.arange(10)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))
#these are referred to as unary ufuncs

#write these into a @hops component
@hops.component(
    "/ndarray_unary_ufuncs",
    name="ndarray_unary_ufuncs",
    nickname="ndarray_unary_ufuncs",
    description="ndarray_unary_ufuncs",
    inputs=[
        hs.HopsNumber("arr", "arr", "arr", access = hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("sqrt", "sqrt", "sqrt", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("exp", "exp", "exp", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_unary_ufuncs(arr: float):
    sqrt = np.sqrt(arr)
    exp = np.exp(arr)
    print(sqrt)
    print(exp)
    return sqrt.tolist(), exp.tolist()

#numpy.add or numpy.maximum, take two arrays and return a single array as the result
#these are referred to as binary ufuncs
rng = np.random.default_rng(seed=12345)
print (rng)
x = rng.standard_normal(8)
y = rng.standard_normal(8)
print(x)
print(y)
print(np.maximum(x, y))

#write these into a @hops component
@hops.component(
    "/ndarray_binary_ufuncs",
    name="ndarray_binary_ufuncs",
    nickname="ndarray_binary_ufuncs",
    description="ndarray_binary_ufuncs",
    inputs=[
        hs.HopsNumber("x", "x", "x", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("y", "y", "y", access = hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("maximum", "maximum", "maximum", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_binary_ufuncs(x: float, y: float):
    maximum = np.maximum(x, y)
    print(maximum)
    return maximum.tolist()

arr = rng.standard_normal(7) * 5
print(arr)
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)

#write these into a @hops component
@hops.component(
    "/ndarray_modf",
    name="ndarray_modf",
    nickname="ndarray_modf",
    description="ndarray_modf",
    inputs=[
        hs.HopsNumber("arr", "arr", "arr", access = hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsNumber("remainder", "remainder", "remainder", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("whole_part", "whole_part", "whole_part", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_modf(arr: float):
    remainder, whole_part = np.modf(arr)
    print(remainder)
    print(whole_part)
    return remainder.tolist(), whole_part.tolist()

#optional out argument that allows you to write the results of a 
# computation to that array
arr = rng.standard_normal(7) * 5
print(arr)
out = np.zeros_like(arr)
print(out)
np.add(arr, 1)
print(arr)
np.add(arr, 1, out=out)
print(out)

#some unary ufuncs
#abs, fabs, sqrt, square, exp, log, log10, log2, log1p, 
# sign, ceil, floor, rint, modf, isnan, isfinite, isinf, 
# cos, cosh, sin, sinh, tan, tanh, arccos, arccosh, 
# arcsin, arcsinh, arctan, arctanh, logical_not

#abs


#some binary ufuncs
#add, subtract, multiply, divide, floor_divide, power,
# maximum, minimum, mod, copysign, greater, greater_equal,
# less, less_equal, equal, not_equal, logical_and,
# logical_or, logical_xor

"""
 █████╗ ██████╗ ██████╗  █████╗ ██╗   ██╗                                                     
██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝                                                     
███████║██████╔╝██████╔╝███████║ ╚████╔╝                                                      
██╔══██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝                                                       
██║  ██║██║  ██║██║  ██║██║  ██║   ██║                                                        
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                                                        
                                                                                              
 ██████╗ ██████╗ ██╗███████╗███╗   ██╗████████╗███████╗██████╗                                
██╔═══██╗██╔══██╗██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗                               
██║   ██║██████╔╝██║█████╗  ██╔██╗ ██║   ██║   █████╗  ██║  ██║                               
██║   ██║██╔══██╗██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██║  ██║                               
╚██████╔╝██║  ██║██║███████╗██║ ╚████║   ██║   ███████╗██████╔╝                               
 ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝                                
                                                                                              
██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗███╗   ███╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║████╗ ████║██║████╗  ██║██╔════╝ 
██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║██╔████╔██║██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""

#Array-Oriented Programming with Arrays
#express many data processing tasks as concise array expressions
#without the need for loops
#vectorization
#check out broadcasting later

#example for evaluating the function sqrt(x^2 + y^2) across a regular grid of values
#using the np.meshgrid function
# takes two 1D arrays and produces two 2D matrices corresponding 
# to all pairs of (x, y) in the two arrays
points = np.arange(-5, 5, 1) #10 equally spaced points #1000 points
xs, ys = np.meshgrid(points, points)
print(xs)
print(" ")
print(ys)
#print first row of ys
print(ys[0])
print(ys[0][0])
#print first first row of ys and convert to list
print(ys[0].tolist())



#write this into a @hops component
@hops.component(
    "/ndarray_meshgrid_02",
    name="ndarray_meshgrid",
    nickname="ndarray_meshgrid",
    description="ndarray_meshgrid",
    inputs=[
        hs.HopsString("points", "points", "points", access = hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsString("xs", "xs", "xs", access = hs.HopsParamAccess.LIST),
        hs.HopsString("ys", "ys", "ys", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_meshgrid_02(points: float):
    xs, ys = np.meshgrid(points, points)
    #print(xs)
    print(ys)
    return xs.tolist(), ys.tolist()

#write this again
@hops.component(
    "/ndarray_meshgrid_05",
    name="ndarray_meshgrid",
    nickname="ndarray_meshgrid",
    description="ndarray_meshgrid",
    inputs=[
        hs.HopsNumber("start", "start", "start", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("stop", "stop", "stop", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("step", "step", "step", access = hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("ysRow1", "ysRow1", "ysRow1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow2", "ysRow2", "ysRow2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow3", "ysRow3", "ysRow3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow4", "ysRow4", "ysRow4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow5", "ysRow5", "ysRow5", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow6", "ysRow6", "ysRow6", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow7", "ysRow7", "ysRow7", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow8", "ysRow8", "ysRow8", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow9", "ysRow9", "ysRow9", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("ysRow10", "ysRow10", "ysRow10", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_meshgrid_05(start: float, stop: float, step: float):
    points = np.arange(start, stop, step)
    xs, ys = np.meshgrid(points, points)
    print(ys)
    return ys[0].tolist(), ys[1].tolist(), ys[2].tolist(), ys[3].tolist(), ys[4].tolist(), ys[5].tolist(), ys[6].tolist(), ys[7].tolist(), ys[8].tolist(), ys[9].tolist()

#evaluate the function sqrt(x^2 + y^2) across a regular grid of values
#using the np.meshgrid function
# takes two 1D arrays and produces two 2D matrices corresponding
# to all pairs of (x, y) in the two arrays
points = np.arange(-5, 5, 1) #10 equally spaced points #1000 points
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)



#write this again
@hops.component(
    "/ndarray_meshgrid_06",
    name="ndarray_meshgrid",
    nickname="ndarray_meshgrid",
    description="ndarray_meshgrid",
    inputs=[
        hs.HopsNumber("start", "start", "start", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("stop", "stop", "stop", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("step", "step", "step", access = hs.HopsParamAccess.ITEM)
        ],
    outputs=[
        hs.HopsNumber("yzRow1", "yzRow1", "yzRow1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow2", "yzRow2", "yzRow2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow3", "yzRow3", "yzRow3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow4", "yzRow4", "yzRow4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow5", "yzRow5", "yzRow5", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow6", "yzRow6", "yzRow6", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow7", "yzRow7", "yzRow7", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow8", "yzRow8", "yzRow8", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow9", "yzRow9", "yzRow9", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yzRow10", "yzRow10", "yzRow10", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_meshgrid_06(start: float, stop: float, step: float):
    points = np.arange(start, stop, step)
    xs, ys = np.meshgrid(points, points)
    z = np.sqrt(xs ** 2 + ys ** 2)
    print(z)
    return z[0].tolist(), z[1].tolist(), z[2].tolist(), z[3].tolist(), z[4].tolist(), z[5].tolist(), z[6].tolist(), z[7].tolist(), z[8].tolist(), z[9].tolist()

#the term vectorization refers to the practice of replacing explicit loops
#with array expressions
#vectorized array operations are often one or two (or more) orders of magnitude
#faster than their pure python equivalents, with the biggest impact in any kind
#of numerical computations
#any time you see such a loop in a python script, you should consider whether
#it can be replaced with a vectorized expression
#the vectorized approach is more concise and often more than 100 times faster
#than the loop based approach

#Expressing Conditional Logic as Array Operations
#The numpy.where function is a vectorized version of the ternary expression
#x if condition else y

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
#suppose we wanted to take a value from xarr whenever the corresponding
#value in cond is True, and otherwise take the value from yarr
#list comprehension
result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
print(result)
#this has multiple problems
#1. it will not be very fast for large arrays
#2. it will not work with multidimensional arrays
#with np.where we can write this very concisely
result = np.where(cond, xarr, yarr)
print(result)

#write this into a @hops component
@hops.component(
    "/ndarray_where_01",
    nickname="ndarray_where",
    description="ndarray_where",
    inputs = [
        hs.HopsNumber("xarr", "xarr", "xarr", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yarr", "yarr", "yarr", access = hs.HopsParamAccess.LIST),
        hs.HopsBoolean("cond", "cond", "cond", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("result", "result", "result", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_where_01(xarr: float, yarr: float, cond: bool):
    result = np.where(cond, xarr, yarr)
    return result.tolist()

#the second and third arguments to np.where don't need to be arrays
#they can be scalars
#A typical use of where in data analysis is to produce a new array of values
#based on another array
#suppose you had a matrix of randomly generated data and you wanted to replace
#all positive values with 2 and all negative values with -2
arr = np.random.randn(4, 4)
print(arr)
print(arr > 0)
print(np.where(arr > 0, 2, -2))

#you can combine scalars and arrays when using np.where
print(np.where(arr > 0, 2, arr)) #set only positive values to 2

#write this into a @hops component
@hops.component(
    "/ndarray_where_03",
    name="ndarray_where",
    nickname="ndarray_where",
    description="ndarray_where",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_where_03(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arr > 0
    arr = np.where(arr > 0, 2, -2)
    return arr[0].tolist(), arr[1].tolist(), arr[2].tolist(), arr[3].tolist()

#Mathematical and Statistical Methods
#mathematical functions that compute statistics about an entire array or
#about the data along an axis are accessible as methods of the array class
#you can use aggregations (often called reductions) like sum, mean, and std
#either by calling the array instance method or using the top level numpy
#function
arr = np.random.randn(5, 4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())

#write this into a @hops component
@hops.component(
    "/ndarray_mean_02",
    name="ndarray_mean",
    nickname="ndarray_mean",
    description="ndarray_mean",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("mean", "mean", "mean", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_mean_02(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    mean = arr.mean()
    return arr[0].tolist(), arr[1].tolist(), arr[2].tolist(), arr[3].tolist(), mean


#functions like mean and sum take an optional axis argument that computes the
#statistic over the given axis, resulting in an array with one fewer dimension
#than the original array
print(arr.mean(axis=1))
print(arr.sum(axis=0))

#write this into a @hops component
@hops.component(
    "/ndarray_mean_03",
    name="ndarray_mean",
    nickname="ndarray_mean",
    description="ndarray_mean",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("mean", "mean", "mean", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_mean_03(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    mean = arr.mean(axis=axis)
    return arr[0].tolist(), arr[1].tolist(), arr[2].tolist(), arr[3].tolist(), mean.tolist()

#cumsum and cumprod do not aggregate, instead producing an array of the
#intermediate results
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())

#write this into a @hops component
@hops.component(
    "/ndarray_cumsum_06",
    name="ndarray_cumsum",
    nickname="ndarray_cumsum",
    description="ndarray_cumsum",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ],
    )
def ndarray_cumsum_06(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    cumarr = arr.cumsum(axis=axis)
    print(cumarr)
    return cumarr[0].tolist(), cumarr[1].tolist(), cumarr[2].tolist(), cumarr[3].tolist()

#write a @hops component that computes the cumulative product of the elements
#along the given axis of the array
@hops.component(
    "/ndarray_cumprod_07",
    name="ndarray_cumprod",
    nickname="ndarray_cumprod",
    description="ndarray_cumprod",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ],
    )
def ndarray_cumprod_07(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    cumarr = arr.cumprod(axis=axis)
    print(cumarr)
    return cumarr[0].tolist(), cumarr[1].tolist(), cumarr[2].tolist(), cumarr[3].tolist()


#Basic array statistical methods
#min, max, argmin, argmax, sum, mean, std, var, cumsum, cumprod
#min and max return the minimum and maximum values in an array
#argmin and argmax return the index of the minimum and maximum elements
#std and var compute the standard deviation and variance
#cumsum and cumprod compute the cumulative sums and products
#write this into a @hops component
@hops.component(
    "/ndarray_min",
    name="ndarray_min",
    nickname="ndarray_min",
    description="ndarray_min",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_min(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    min = arr.min(axis=axis)
    return min[0].tolist(), min[1].tolist(), min[2].tolist(), min[3].tolist(), min.tolist()

#write this into a @hops component
@hops.component(
    "/ndarray_max",
    name="ndarray_max",
    nickname="ndarray_max",
    description="ndarray_max",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_max(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    max = arr.max(axis=axis)
    return max[0].tolist(), max[1].tolist(), max[2].tolist(), max[3].tolist(), max.tolist()

#write this into a @hops component
@hops.component(
    "/ndarray_argmin_05",
    name="ndarray_argmin",
    nickname="ndarray_argmin",
    description="ndarray_argmin",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsInteger("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_argmin_05(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    argmin = arr.argmin(axis=axis)
    return argmin[0].tolist(), argmin[1].tolist(), argmin[2].tolist(), argmin[3].tolist()

#write a @hops component for argmax
@hops.component(
    "/ndarray_argmax_05",
    name="ndarray_argmax",
    nickname="ndarray_argmax",
    description="ndarray_argmax",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsInteger("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_argmax_05(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    argmax = arr.argmax(axis=axis)
    return argmax[0].tolist(), argmax[1].tolist(), argmax[2].tolist(), argmax[3].tolist()

#std and var compute the standard deviation and variance
#write a @hops component for std
@hops.component(
    "/ndarray_std_05",
    name="ndarray_std",
    nickname="ndarray_std",
    description="ndarray_std",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_std_05(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    std = arr.std(axis=axis)
    return std[0].tolist(), std[1].tolist(), std[2].tolist(), std[3].tolist(), std.tolist()

#write a @hops component for var
@hops.component(
    "/ndarray_var_05",
    name="ndarray_var",
    nickname="ndarray_var",
    description="ndarray_var",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_var_05(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    var = arr.var(axis=axis)
    return var[0].tolist(), var[1].tolist(), var[2].tolist(), var[3].tolist(), var.tolist()

#Methods for Boolean Arrays
#boolean arrays are coerced to 0 and 1 in the methods below
#therefore sum is often used as a means of counting True values in a boolean array
arr = rng.standard_normal(100)
(arr > 0).sum() #number of positive values
(arr <= 0).sum() #number of negative values

#write a @hops component for sum
@hops.component(
    "/ndarray_sum_3",
    name="ndarray_sum",
    nickname="ndarray_sum",
    description="ndarray_sum",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsInteger("nPos", "nPos", "nPos", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("nNeg", "nNeg", "nNeg", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_sum_03(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    nPos = (arr > 0).sum()
    nNeg = (arr <= 0).sum()
    return nPos.tolist(), nNeg.tolist()

#the parantheses are required in the above example to be able to 
# call the sum method on the temporary result of arr > 0 and arr <= 0

#additional methods any and all, are used to quickly test whether 
# any or all the values in an array are True
bools = np.array([False, False, True, False])
bools.any() #True
bools.all() #False

#write a @hops component for any
@hops.component(
    "/ndarray_any",
    name="ndarray_any",
    nickname="ndarray_any",
    description="ndarray_any",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsBoolean("any", "any", "any", access = hs.HopsParamAccess.ITEM),
        hs.HopsBoolean("all", "all", "all", access = hs.HopsParamAccess.ITEM)
        ]   
)
def ndarray_any(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    #change array to zeros 
    arr = np.zeros((rows, columns))
    print(arr)
    any = arr.any()
    all = arr.all()
    return any.tolist(), all.tolist()

#Methods for Sorting
#sort in place using the sort method
arr = rng.standard_normal(6)
arr.sort()
print(arr)

#sort each one dimensional section of values in a multidimensional array
#by passing an axis argument to sort
arr = rng.standard_normal((3, 5))
print(arr)
arr.sort(axis=0)
print(arr)
arr.sort(axis=1)
print(arr)

#the top level method np.sort returns a sorted copy of an array
#like the Python built-in function sorted
#instead of sorting in place
arr2 = np.array([3, 5, 2, 1])
print(arr)
sorted_arr2 = np.sort(arr2)
print(sorted_arr2)

#write a @hops component for sort
@hops.component(
    "/ndarray_sort",
    name="ndarray_sort",
    nickname="ndarray_sort",
    description="ndarray_sort",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_sort(rows: int, columns: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arr.sort(axis=axis)
    return arr[0].tolist(), arr[1].tolist(), arr[2].tolist(), arr[3].tolist()

#write a @hops component for top level sort
@hops.component(
    "/ndarray_top_level_sort",
    name="ndarray_top_level_sort",
    nickname="ndarray_top_level_sort",
    description="ndarray_top_level_sort",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3", "arr3", "arr3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4", "arr4", "arr4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_top_level_sort(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arr = np.sort(arr)
    return arr[0].tolist(), arr[1].tolist(), arr[2].tolist(), arr[3].tolist()

#unique and other set logic
#numpy has some basic set operations for one dimensional ndarrays
#np.unique returns the sorted unique values in an array
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))

#contrast with the pure Python alternative
print(sorted(set(names)))
print(sorted(set(ints)))

#writing this into a @hops component
@hops.component(
    "/ndarray_unique_02",
    name="ndarray_unique",
    nickname="ndarray_unique",
    description="ndarray_unique",
    inputs = [
        hs.HopsInteger("list", "list", "list", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsInteger("unique", "unique", "unique", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_unique_02(list: int):
    unique = np.unique(list)
    return unique.tolist()

#another function, np.in1d, tests membership of the values in one array in another
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))

#write this into a @hops component
@hops.component(
    "/ndarray_in1d",
    name="ndarray_in1d",
    nickname="ndarray_in1d",
    description="ndarray_in1d",
    inputs = [
        hs.HopsInteger("list", "list", "list", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("values", "values", "values", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsBoolean("in1d", "in1d", "in1d", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_in1d(list: int, values: int):
    in1d = np.in1d(list, values)
    return in1d.tolist()

#Array set operations
#unique(x) #compute the sorted, unique elements in x

#intersect1d(x, y) #compute the sorted, common elements in x and y
#write this into a @hops component
@hops.component(
    "/ndarray_intersect1d",
    name="ndarray_intersect1d",
    nickname="ndarray_intersect1d",
    description="ndarray_intersect1d",
    inputs = [
        hs.HopsInteger("x", "x", "x", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("y", "y", "y", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsInteger("intersect1d", "intersect1d", "intersect1d", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_intersect1d(x: int, y: int):
    intersect1d = np.intersect1d(x, y)
    return intersect1d.tolist()
    
#union1d(x, y) #compute the sorted union of elements
#write this into a @hops component
@hops.component(
    "/ndarray_union1d",
    name="ndarray_union1d",
    nickname="ndarray_union1d",
    description="ndarray_union1d",
    inputs = [
        hs.HopsInteger("x", "x", "x", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("y", "y", "y", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsInteger("union1d", "union1d", "union1d", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_union1d(x: int, y: int):
    union1d = np.union1d(x, y)
    return union1d.tolist()

#in1d(x, y) #compute a boolean array indicating whether each element of x is contained in y

#setdiff1d(x, y) #set difference, elements in x that are not in y
#write this into a @hops component
@hops.component(
    "/ndarray_setdiff1d",
    name="ndarray_setdiff1d",
    nickname="ndarray_setdiff1d",
    description="ndarray_setdiff1d",
    inputs = [
        hs.HopsInteger("x", "x", "x", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("y", "y", "y", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsInteger("setdiff1d", "setdiff1d", "setdiff1d", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_setdiff1d(x: int, y: int):
    setdiff1d = np.setdiff1d(x, y)
    return setdiff1d.tolist()
    
#setxor1d(x, y) #set symmetric differences, 
# elements that are in either of the arrays, but not both
#write this into a @hops component
@hops.component(
    "/ndarray_setxor1d",
    name="ndarray_setxor1d",
    nickname="ndarray_setxor1d",
    description="ndarray_setxor1d",
    inputs = [
        hs.HopsInteger("x", "x", "x", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("y", "y", "y", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsInteger("setxor1d", "setxor1d", "setxor1d", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_setxor1d(x: int, y: int):
    setxor1d = np.setxor1d(x, y)
    return setxor1d.tolist()

"""
███████╗██╗██╗     ███████╗    ██╗███╗   ██╗██████╗ ██╗   ██╗████████╗     █████╗ ███╗   ██╗██████╗     
██╔════╝██║██║     ██╔════╝    ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝    ██╔══██╗████╗  ██║██╔══██╗    
█████╗  ██║██║     █████╗      ██║██╔██╗ ██║██████╔╝██║   ██║   ██║       ███████║██╔██╗ ██║██║  ██║    
██╔══╝  ██║██║     ██╔══╝      ██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║       ██╔══██║██║╚██╗██║██║  ██║    
██║     ██║███████╗███████╗    ██║██║ ╚████║██║     ╚██████╔╝   ██║       ██║  ██║██║ ╚████║██████╔╝    
╚═╝     ╚═╝╚══════╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     
                                                                                                        
 ██████╗ ██╗   ██╗████████╗██████╗ ██╗   ██╗████████╗    ██╗    ██╗██╗████████╗██╗  ██╗                 
██╔═══██╗██║   ██║╚══██╔══╝██╔══██╗██║   ██║╚══██╔══╝    ██║    ██║██║╚══██╔══╝██║  ██║                 
██║   ██║██║   ██║   ██║   ██████╔╝██║   ██║   ██║       ██║ █╗ ██║██║   ██║   ███████║                 
██║   ██║██║   ██║   ██║   ██╔═══╝ ██║   ██║   ██║       ██║███╗██║██║   ██║   ██╔══██║                 
╚██████╔╝╚██████╔╝   ██║   ██║     ╚██████╔╝   ██║       ╚███╔███╔╝██║   ██║   ██║  ██║                 
 ╚═════╝  ╚═════╝    ╚═╝   ╚═╝      ╚═════╝    ╚═╝        ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝                 
                                                                                                        
 █████╗ ██████╗ ██████╗  █████╗ ██╗   ██╗███████╗                                                       
██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝                                                       
███████║██████╔╝██████╔╝███████║ ╚████╔╝ ███████╗                                                       
██╔══██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝  ╚════██║                                                       
██║  ██║██║  ██║██║  ██║██║  ██║   ██║   ███████║                                                       
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                                       
"""

#File I/O with numpy arrays
#np.save and np.load are the two workhorse functions for 
# efficiently saving and loading array data on disk
#focus on binary data and leave the load and save of text data to pandas
#arrays are saved by default in an uncompressed raw binary format with file extension .npy
# and passing the arrays as keyword arguments

arr = np.arange(10)
np.save('some_array', arr)
#if the file path does not already end in .npy, the extension is appended
#load the array back into memory with np.load
print(np.load('some_array.npy'))
#you save multiple arrays in an uncompressed archive using np.savez 
np.savez('array_archive.npz', a=arr, b=arr)
#when loading an .npz file, you get back a dict-like object 
# that loads the individual arrays lazily
arch = np.load('array_archive.npz')
print(arch['a'])
print(arch['b'])
#if your data compresses well, you may wish to use numpy.savez_compressed instead
np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)

#write this into a @hops component
@hops.component(
    "/ndarray_save_01",
    name="ndarray_save",
    nickname="ndarray_save",
    description="ndarray_save",
    inputs = [
        hs.HopsInteger("arr", "arr", "arr", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsInteger("arr_saved", "arr_saved", "arr_saved", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_save_01(arr: int):
    np.save('some_array', arr)
    arr_saved = np.load('some_array.npy')
    return arr_saved.tolist()

@hops.component(
    "/ndarray_savez_03b",
    name="ndarray_savez",
    nickname="ndarray_savez",
    description="ndarray_savez",    
    inputs = [
        hs.HopsInteger("arr1", "arr1", "arr1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arr2", "arr2", "arr2", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsInteger("arrZa_saved", "arrZa_saved", "arrZa_saved", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("arrZb_saved", "arrZb_saved", "arrZb_saved", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_savez_03b(arr1: int, arr2: int):
    np.savez('array_archive.npz', a=arr1, b=arr2)
    arrZ_saved = np.load('array_archive.npz')
    [print(arrZ_saved['a']), print(arrZ_saved['b'])]
    print(type(arrZ_saved['a']))
    return arrZ_saved['a'].tolist(), arrZ_saved['b'].tolist()


"""
██╗     ██╗███╗   ██╗███████╗ █████╗ ██████╗             
██║     ██║████╗  ██║██╔════╝██╔══██╗██╔══██╗            
██║     ██║██╔██╗ ██║█████╗  ███████║██████╔╝            
██║     ██║██║╚██╗██║██╔══╝  ██╔══██║██╔══██╗            
███████╗██║██║ ╚████║███████╗██║  ██║██║  ██║            
╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝            
                                                         
 █████╗ ██╗      ██████╗ ███████╗██████╗ ██████╗  █████╗ 
██╔══██╗██║     ██╔════╝ ██╔════╝██╔══██╗██╔══██╗██╔══██╗
███████║██║     ██║  ███╗█████╗  ██████╔╝██████╔╝███████║
██╔══██║██║     ██║   ██║██╔══╝  ██╔══██╗██╔══██╗██╔══██║
██║  ██║███████╗╚██████╔╝███████╗██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                                                    
"""
#Linear Algebra
#numpy.linalg has a standard set of matrix decompositions and things like inverse and determinant
#linear algebra, like matrix multiplication, decompositions, determinants, 
# and other square matrix math
# * is an element wise product
# @ is a matrix product
# dot is also a matrix product
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
print(y)
print(x @ y)
print(x.dot(y))
print(np.dot(x, y))

#write this into a @hops component
@hops.component(
    "/ndarray_matrix_multiplication",
    name="ndarray_dot",
    nickname="ndarray_dot",
    description="ndarray_dot",
    inputs = [
        hs.HopsInteger("rowsX", "rowsX", "rowsX", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columnsX", "columnsX", "columnsX", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("rowsY", "rowsY", "rowsY", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columnsY", "columnsY", "columnsY", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("list2", "list2", "list2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_matrix_multiplication(rowsX: int, columnsX: int, rowsY: int, columnsY: int):
    x = rng.standard_normal((rowsX, columnsX))
    y = rng.standard_normal((rowsY, columnsY))
    print(x)
    print(y)
    arr1 = x @ y
    #arr2 = x.dot(y)
    return arr1.tolist()[0], arr1.tolist()[1]

# x.dot(x) is equivalent to np.dot(x, y)

#A matrix product between a two dimensional array and a suitably sized one dimensional 
# array results in a one dimensional array
print(x @ np.ones(3))
print(np.dot(x, np.ones(3)))

#numpy.linalg has a standard set of matrix decompositions and things like inverse and determinant
#inverse of a square matrix
from numpy.linalg import inv, qr
X = rng.standard_normal((5, 5))
mat = X.T @ X
print(inv(mat))
print(mat @ inv(mat))

#The expression X.T @ X computes the dot product of X with its transpose X
#the inverse of a matrix is typically not the most efficient way to solve a linear system

#write this into a @hops component
@hops.component(
    "/ndarray_inverse_03",
    name="ndarray_inverse",
    nickname="ndarray_inverse",
    description="ndarray_inverse",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1list1", "arr1list1", "arr1list1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr1list2", "arr1list2", "arr1list2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr1list3", "arr1list3", "arr1list3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr1list4", "arr1list4", "arr1list4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2list1", "arr2list1", "arr2list1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2list2", "arr2list2", "arr2list2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2list3", "arr2list3", "arr2list3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2list4", "arr2list4", "arr2list4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_inverse_03(rows: int, columns: int):
    X = rng.standard_normal((rows, columns))
    mat = X.T @ X
    print(mat)
    arr1 = inv(mat)
    arr2 = mat @ inv(mat)
    return arr1[0].tolist(), arr1[1].tolist(), arr1[2].tolist(), arr1[3].tolist(), arr2[0].tolist(), arr2[1].tolist(), arr2[2].tolist(), arr2[3].tolist()

#the expression X.T.dot(X) computes the dot product of X with its transpose X

#Commonly used numpy.linalg functions
#diag #return the diagonal (or off-diagonal) elements of a square matrix as a 1D array
#dot #matrix multiplication
#trace #compute the sum of the diagonal elements
#det #compute the matrix determinant
#eig #compute the eigenvalues and eigenvectors of a square matrix
#inv #compute the inverse of a square matrix
#pinv #compute the Moore-Penrose pseudo-inverse of a matrix
#qr #compute the QR decomposition
#svd #compute the singular value decomposition (SVD)
#solve #solve the linear system Ax = b for x, where A is a square matrix
#lstsq #compute the least-squares solution to Ax = b

#write a @hops component for diag
@hops.component(
    "/ndarray_diag_01",
    name="ndarray_diag",
    nickname="ndarray_diag",
    description="ndarray_diag",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("diag", "diag", "diag", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_diag_01(rows: int, columns: int):
    X = rng.standard_normal((rows, columns))
    print(X)
    diag = np.diag(X)
    return diag.tolist()

#write a @hops component for trace
@hops.component(
    "/ndarray_trace_03",
    name="ndarray_trace",
    nickname="ndarray_trace",
    description="ndarray_trace",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("trace", "trace", "trace", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_trace_03(rows: int, columns: int):
    X = rng.standard_normal((rows, columns))
    print(X)
    trace = np.trace(X)
    return trace

#write a @hops component for det
@hops.component(
    "/ndarray_det_01",
    name="ndarray_det",
    nickname="ndarray_det",
    description="ndarray_det",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("det", "det", "det", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_det_01(rows: int, columns: int):
    X = rng.standard_normal((rows, columns))
    print(X)
    det = np.linalg.det(X)
    return det

#write a @hops component for eig
@hops.component(
    "/ndarray_eig_04",
    name="ndarray_eig",
    nickname="ndarray_eig",
    description="ndarray_eig",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("eig", "eig", "eig", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_eig_04(rows: int, columns: int):
    X = rng.standard_normal((rows, columns))
    print(X)
    eig = np.linalg.eig(X)
    print (eig)
    print(type(eig))
    convert = str(eig)
    return convert

#pinv #compute the Moore-Penrose pseudo-inverse of a matrix
#qr #compute the QR decomposition
#svd #compute the singular value decomposition (SVD)
#solve #solve the linear system Ax = b for x, where A is a square matrix
#lstsq #compute the least-squares solution to Ax = b

"""
██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ███╗    
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗ ████║    
██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔████╔██║    
██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╔╝██║    
██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚═╝ ██║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝    
                                                          
██╗    ██╗ █████╗ ██╗     ██╗  ██╗███████╗                
██║    ██║██╔══██╗██║     ██║ ██╔╝██╔════╝                
██║ █╗ ██║███████║██║     █████╔╝ ███████╗                
██║███╗██║██╔══██║██║     ██╔═██╗ ╚════██║                
╚███╔███╔╝██║  ██║███████╗██║  ██╗███████║                
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝  
"""

'''
#Example: Random Walks to End our Numpy : Basics Bundle of Scipts
#wika: https://en.wikipedia.org/wiki/Random_walk
#pure Python
#! blockstart
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
#! blockend
import matplotlib.pyplot as plt
plt.plot(walk[:100])
'''

nsteps = 1000
rng = np.random.default_rng(12345) #random number generator
draws = rng.integers(0, 2, size=nsteps) #draws is an array of 0s and 1s
steps = np.where(draws > 0, 1, -1) #steps is an array of 1s and -1s
walk = steps.cumsum() #cumsum is a method that produces an array of the running sum of the elements
#from this we can extract statistics like the minimum and maximum value along the way
print(walk.min())
print(walk.max())
#we can also compute the first crossing time, the step at which the random walk 
# reaches a particular value
#here we want to know how long it took the random walk to get at least 10 steps 
# away from the origin 0
print((np.abs(walk) >= 10).argmax())

#write this into a @hops component
@hops.component(
    "/ndarray_random_walk_01",
    name="ndarray_random_walk",
    nickname="ndarray_random_walk",
    description="ndarray_random_walk",
    inputs = [
        hs.HopsInteger("nsteps", "nsteps", "nsteps", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("walk", "walk", "walk", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_walk_01(nsteps: int):
    rng = np.random.default_rng(12345)
    draws = rng.integers(0, 2, size=nsteps)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    return walk.tolist()

#Simulate Many Random Walks at Once
#let's say you wanted to simulate many random walks at the same time
#the numpy.random functions if passed a 2-tuple will generate a 2D array of draws
#let's compute a 5000 step random walk with 1000 walks
nwalks = 5000
nsteps = 1000
draws = rng.integers(0, 2, size=(nwalks, nsteps)) #draws is an array of 0s and 1s
steps = np.where(draws > 0, 1, -1) #steps is an array of 1s and -1s
walks = steps.cumsum(1) #cumsum is a method that produces an array of the running sum of the elements
print(walks)
print(walks.max())
print(walks.min())
#compute the minimum crossing time to 30 or -30
#not all 5000 of them reach 30
hits30 = (np.abs(walks) >= 30).any(axis=1)
print(hits30)
print(hits30.sum()) #number that hit 30 or -30 
#we can use this boolean array to select out the rows of walks that actually cross 
# the absolute 30 level
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)
print(crossing_times.mean())
#feel free to experiment with other distributions for the steps other than equal sized coin flips
#to do this, you can pass a 2-tuple for the mean and standard deviation
steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))
print(steps)
#write this into a @hops component
@hops.component(
    "/ndarray_random_walk_02",
    name="ndarray_random_walk",
    nickname="ndarray_random_walk",
    description="ndarray_random_walk",
    inputs = [
        hs.HopsInteger("nwalks", "nwalks", "nwalks", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("nsteps", "nsteps", "nsteps", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("walksList1", "walksList1", "walksList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("walksList2", "walksList2", "walksList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("walksList3", "walksList3", "walksList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("walksList4", "walksList4", "walksList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_random_walk_02(nwalks: int, nsteps: int):
    rng = np.random.default_rng(12345)
    draws = rng.integers(0, 2, size=(nwalks, nsteps))
    steps = np.where(draws > 0, 1, -1)
    walks = steps.cumsum(1)
    print(walks)
    print(walks.max())
    print(walks.min())
    hits30 = (np.abs(walks) >= 30).any(axis=1)
    print(hits30)
    print(hits30.sum())
    crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)
    print(crossing_times.mean())
    steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))
    return walks.tolist()[0], walks.tolist()[1], walks.tolist()[2], walks.tolist()[3]

#conclusion
#numpy is the foundation on which many important Python data science libraries are built

#pandas, scipy, scikit-learn, statsmodels, and many others

#numpy is fast, easy to use, and provides a standard API that enables you to
# quickly develop efficient algorithms using high-level mathematical functions
#numpy arrays are like Python lists, but they are homogeneous and typed
#numpy arrays are memory efficient and fast to operate on
#numpy provides a large library of high-level mathematical functions that operate on arrays
#numpy arrays can be sliced, masked, and iterated on

"""
 █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║
██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║
██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ 
                                                                   
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗                    
████╗  ██║██║   ██║████╗ ████║██╔══██╗╚██╗ ██╔╝                    
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝ ╚████╔╝                     
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔═══╝   ╚██╔╝                      
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║        ██║                       
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝  
"""
#Advanced NumPy
#ndarray object internals
rng = np.random.default_rng(12345)

#ndarray is a generic multidimensional container for homogeneous data 
# (either all integers, floats, or strings) or a mixture of different types
#dtype is a special object containing the information (or metadata, data about data)
#striding is the number of bytes to step in each dimension when traversing the array
#ndim is the number of dimensions
#this does not copy any data, it just creates a new view of the original array
#the data is not copied, and any modifications to the view will be reflected in the source array
#the transpose method, like most numpy functions, returns a view instead of a copy whenever possible
#the copy method makes a complete copy of the array and its data

#the ndarray consists of:
#a pointer to data, a block of memory, keeping track of the start of the array data 
#a data type or dtype, describing fixed-size value cells in the array
#a shape, a tuple indicating the size of each dimension
#a strides, a tuple indicating the number of bytes to step in each dimension when traversing the array

#for example a 3x4x5 float64 array would have shape (3, 4, 5) and dtype float64
#it would have 3*4*5*8 bytes of data, and more bytes for the other information in the ndarray object
#it would have strides (160, 40, 8) indicating the number of bytes to step in each dimension when traversing the array
#the strides are computed from the shape of the array by multiplying the number of bytes per cell by the number of cells to step in each direction
#strides can be negative, indicating that the array is traversed backwards

#write this into a @hops component
@hops.component(
    "/ndarray_strides_02",
    name="ndarray_strides",
    nickname="ndarray_strides",
    description="ndarray_strides",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("depth", "depth", "depth", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("strides", "strides", "strides", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_strides_02(rows: int, columns: int, depth: int):
    X = rng.standard_normal((rows, columns, depth))
    print(X)
    strides = X.strides
    return strides 

#Numpy Data Type Hierarchy
#superclasses of numpy data types
#np.integer
#np.floating
#np.complexfloating
#np.bool
#np.character
#np.flexible
#np.datetime64
#np.timedelta64
#np.void

#np.issubtype is a safe way to check whether one dtype is a subclass of another
ints = np.ones(10, dtype=np.uint16)
floats = np.ones(10, dtype=np.float32)
print(np.issubdtype(ints.dtype, np.integer))
print(np.issubdtype(floats.dtype, np.floating))

#write this into a @hops component
@hops.component(
    "/ndarray_issubdtype_01",
    name="ndarray_issubdtype",
    nickname="ndarray_issubdtype",
    description="ndarray_issubdtype",
    inputs = [
        hs.HopsInteger("ints", "ints", "ints", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("floats", "floats", "floats", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsBoolean("ints", "ints", "ints", access = hs.HopsParamAccess.ITEM),
        hs.HopsBoolean("floats", "floats", "floats", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_issubdtype_01(ints: int, floats: float):
    ints = np.ones(10, dtype=np.uint16)
    floats = np.ones(10, dtype=np.float32)
    ints = np.issubdtype(ints.dtype, np.integer)
    floats = np.issubdtype(floats.dtype, np.floating)
    return ints, floats

#mro method returns a tuple of types that the class is derived from in order 
# from base to subclass
print(np.float64.mro())
print(np.int32.mro())
#therefore , we also have
print(np.issubdtype(np.float64, np.floating))

#write this into a @hops component
@hops.component(
    "/ndarray_mro_01",
    name="ndarray_mro",
    nickname="ndarray_mro",
    description="ndarray_mro",
    inputs = [
        hs.HopsInteger("float64", "float64", "float64", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("int32", "int32", "int32", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsString("float64", "float64", "float64", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("int32", "int32", "int32", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_mro_01(float64: float, int32: int):
    float64 = np.float64.mro()
    int32 = np.int32.mro()
    return str(float64), str(int32)


#Advanced Array Manipulation
#there are many ways to manipulate the data within arrays beyond indexing, slicing, and masking
#fancy indexing, and boolean upsetting

#Reshape Arrays
#reshape method returns a new ndarray object pointing at the same data
#to change a 3x4 array to a 4x3 array, you can pass the shape tuple to reshape
arr = np.arange(8)
print(arr)
print(arr.reshape((4, 2)))
print(arr.reshape((4, 2)).reshape((2, 4)))

#write this into a @hops component
@hops.component(
    "/ndarray_reshape_02",
    name="ndarray_reshape",
    nickname="ndarray_reshape",
    description="ndarray_reshape",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_reshape_02(rows: int, columns: int):
    arr = np.arange(rows * columns)
    print(arr)
    arrReshaped = arr.reshape((rows, columns))
    print(arrReshaped)
    return arrReshaped.tolist()[0], arrReshaped.tolist()[1], arrReshaped.tolist()[2], arrReshaped.tolist()[3]

#write this into a @hops component
@hops.component(
    "/ndarray_reshape_03",
    name="ndarray_reshape",
    nickname="ndarray_reshape",
    description="ndarray_reshape",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_reshape_03(list1: int, rows: int, columns: int):
    arr = np.array(list1)
    print(arr)
    arrReshaped = arr.reshape((rows, columns))
    print(arrReshaped)
    return arrReshaped.tolist()[0], arrReshaped.tolist()[1], arrReshaped.tolist()[2], arrReshaped.tolist()[3]

#a multidimensional array can also be reshaped
#the only requirement is that the size of the initial array matches the size of the reshaped array
#the reshape method can also be called directly as a function
#the following are equivalent
arr = np.arange(8).reshape((4, 2))
print(arr)
print(np.reshape(np.arange(8), (4, 2)))

#write this into a @hops component
@hops.component(
    "/ndarray_reshape_04",
    name="ndarray_reshape",
    nickname="ndarray_reshape",
    description="ndarray_reshape",
    #icon = "images/ndarray_reshape.png",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_reshape_04(rows: int, columns: int):
    arr = np.arange(rows * columns).reshape((rows, columns))
    print(arr)
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2], arr.tolist()[3]


#the opposite operation of reshape from one-dimensional to a higher dimension is typically known as flattening or raveling
#flatten returns a copy of the data in a one-dimensional array
#the -1 value in a reshape operation means to automatically compute the size of the dimension
arr = np.arange(15).reshape((5, 3))
print(arr)
print(arr.ravel())
print(arr.ravel().reshape((5, 3)))
print(arr.ravel().reshape((5, -1)))

#example of raveling
#write this into a @hops component
@hops.component(
    "/ndarray_ravel_02",
    name="ndarray_ravel",
    nickname="ndarray_ravel",
    description="ndarray_ravel",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("List1", "List1", "List1", access = hs.HopsParamAccess.LIST),
        ]
)
def ndarray_ravel_02(rows: int, columns: int):
    arr = np.arange(rows * columns).reshape((rows, columns))
    print(arr)
    arrRaveled = arr.ravel()
    print(arrRaveled)
    return arrRaveled.tolist()

#example of flattening
#write this into a @hops component
@hops.component(
    "/ndarray_flatten_01",
    name="ndarray_flatten",
    nickname="ndarray_flatten",
    description="ndarray_flatten",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("List1", "List1", "List1", access = hs.HopsParamAccess.LIST),
        ]
)
def ndarray_flatten_01(rows: int, columns: int):
    arr = np.arange(rows * columns).reshape((rows, columns))
    print(arr)
    arrFlattened = arr.flatten()
    print(arrFlattened)
    return arrFlattened.tolist()

#C Versus Fortran Order
#when multidimensional data is stored in a one-dimensional block of memory, 
#there is a choice about how to interpret the data as a multidimensional array
#the order= keyword argument can be used to specify whether the array should 
# be stored in row-major order (C) or column-major order (Fortran)
#the default is row-major order
arr = np.arange(12).reshape((3, 4))
print(arr)
print(arr.ravel())
print(arr.ravel('F'))

#reshaping higher dimensional arrays also follows the same ordering
#but it can be a bit more confusing
#C/row major order means that the last axis index varies the fastest, 
# and the first index the slowest
#e.g. axis 1 before advancing on axis 0
#Fortran/column major order means that the first index varies the fastest,
# and the last index the slowest
#e.g. axis 0 before advancing on axis 1
arr = np.arange(12).reshape((3, 4))
print(arr)
print(arr.ravel())
print(arr.ravel('F'))
print(arr.reshape((3, 4), order='F'))
print(arr.reshape((3, 4), order='C'))
print(arr.reshape((4, 3), order='F'))
print(arr.reshape((4, 3), order='C'))

#write this into a @hops component
@hops.component(
    "/ndarray_reshape_02",
    name="ndarray_reshape", 
    nickname="ndarray_reshape",
    description="ndarray_reshape",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_reshape_02(list1: int, rows: int, columns: int):
    arr = np.array(list1).reshape((rows, columns))
    print(arr)
    arrReshaped = arr.reshape((rows, columns), order='F')
    print(arrReshaped)
    return arrReshaped.tolist()[0], arrReshaped.tolist()[1], arrReshaped.tolist()[2], arrReshaped.tolist()[3]

#Concatenate and Splitting Arrays
#numpy.concatenate takes a sequence (tuple, list, etc.) 
#of arrays and joins them together in order along the input axis
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([arr1, arr2], axis=0))
print(np.concatenate([arr1, arr2], axis=1))

#write this into a @hops component
@hops.component(
    "/ndarray_concatenate_02",
    name="ndarray_concatenate",
    nickname="ndarray_concatenate",
    description="ndarray_concatenate",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]   
)
def ndarray_concatenate_01(list1: int, list2: int, list3: int, list4: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    print(arr1)
    print(arr2)
    arrConcatenated = np.concatenate([arr1, arr2], axis=0)
    print(arrConcatenated)
    return arrConcatenated.tolist()[0], arrConcatenated.tolist()[1], arrConcatenated.tolist()[2], arrConcatenated.tolist()[3]

#write this into a @hops component
@hops.component(
    "/ndarray_concatenate_03",
    name="ndarray_concatenate",
    nickname="ndarray_concatenate",
    description="ndarray_concatenate",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_concatenate_02(list1: int, list2: int, list3: int, list4: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    print(arr1)
    print(arr2)
    arrConcatenated = np.concatenate([arr1, arr2], axis=1)
    print(arrConcatenated)
    return arrConcatenated.tolist()[0], arrConcatenated.tolist()[1]

#vstack and hstack are shortcuts for 
# vertical and horizontal concatenation, respectively
print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))

#write this into a @hops component  
@hops.component(
    "/ndarray_vstack_01",
    name="ndarray_vstack",
    nickname="ndarray_vstack",
    description="ndarray_vstack",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_vstack_01(list1: int, list2: int, list3: int, list4: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    print(arr1)
    print(arr2)
    arrVstacked = np.vstack((arr1, arr2))
    print(arrVstacked)
    return arrVstacked.tolist()[0], arrVstacked.tolist()[1], arrVstacked.tolist()[2], arrVstacked.tolist()[3]

#row_stack is equivalent to vstack for any input arrays
#write this into a @hops component
@hops.component(
    "/ndarray_row_stack_01",
    name="ndarray_row_stack",
    nickname="ndarray_row_stack",
    description="ndarray_row_stack",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_row_stack_01(list1: int, list2: int, list3: int, list4: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    print(arr1)
    print(arr2)
    arrRowStacked = np.row_stack((arr1, arr2))
    print(arrRowStacked)
    return arrRowStacked.tolist()[0], arrRowStacked.tolist()[1], arrRowStacked.tolist()[2], arrRowStacked.tolist()[3]

#write this into a @hops component
@hops.component(
    "/ndarray_hstack_01",
    name="ndarray_hstack",
    nickname="ndarray_hstack",
    description="ndarray_hstack",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_hstack_01(list1: int, list2: int, list3: int, list4: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    print(arr1)
    print(arr2)
    arrHstacked = np.hstack((arr1, arr2))
    print(arrHstacked)
    return arrHstacked.tolist()[0], arrHstacked.tolist()[1]

#column_stack is equivalent to hstack only for 2D arrays,
# for 1D arrays it will stack them as columns
#converts 1D arrays into 2D arrays first
#write this into a @hops component
@hops.component(
    "/ndarray_column_stack_01",
    name="ndarray_column_stack",
    nickname="ndarray_column_stack",
    description="ndarray_column_stack",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_column_stack_01(list1: int, list2: int, list3: int, list4: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    print(arr1)
    print(arr2)
    arrColumnStacked = np.column_stack((arr1, arr2))
    print(arrColumnStacked)
    return arrColumnStacked.tolist()[0], arrColumnStacked.tolist()[1]

#dstack stacks arrays along the third axis
#example
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
arr3 = np.array([5, 6])
arr4 = np.array([7, 8])
print(np.dstack(([arr1, arr2], [arr3, arr4])))

#writes this into a @hops component
@hops.component(
    "/ndarray_dstack_01",
    name="ndarray_dstack",
    nickname="ndarray_dstack",
    description="ndarray_dstack",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arr1List1", "arr1List1", "arr1List1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr1List2", "arr1List2", "arr1List2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2List1", "arr2List1", "arr2List1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2List2", "arr2List2", "arr2List2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_dstack_01(list1: int, list2: int, list3: int, list4: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    print(arr1)
    print(arr2)
    arrDstacked = np.dstack(([arr1, arr2]))
    print(arrDstacked)
    return arrDstacked.tolist()[0][0], arrDstacked.tolist()[0][1], arrDstacked.tolist()[1][0], arrDstacked.tolist()[1][1]


#split divides one array into multiple arrays along an axis
#takes a list of indices giving the split points
#example
arr = rng.standard_normal((5, 2))
print(arr)
first, second, third = np.split(arr, [1, 3])
print(first)
print(second)
print(third)

#write this into a @hops component
@hops.component(
    "/ndarray_split_16",
    name="ndarray_split",
    nickname="ndarray_split",
    description="ndarray_split",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("splitStart", "splitStart", "splitStart", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("splitEnd", "splitEnd", "splitEnd", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("first", "first", "first", access = hs.HopsParamAccess.LIST),
        hs.HopsString("second", "second", "second", access = hs.HopsParamAccess.LIST),
        hs.HopsString("third", "third", "third", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_split_16(rows: int, columns: int, splitStart: int, splitEnd: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrSplit = np.split(arr, [splitStart, splitEnd])
    print(arrSplit)
    print(type(arrSplit))
    return arrSplit[0].tolist(), arrSplit[1].tolist(), arrSplit[2].tolist()

#hsplit and vsplit are convenient shortcuts for splitting on axis 0 and axis 1, respectively
#example
arr = rng.standard_normal((5, 2))
print(arr)
first, second = np.hsplit(arr, [1])
print(first)
print(second)

#write this into a @hops component


#example
arr = rng.standard_normal((5, 2))
print(arr)
first, second = np.vsplit(arr, [1])
print(first)
print(second) 

#write this into a component
@hops.component(
    "/ndarray_vsplit_01",
    name="ndarray_vsplit",
    nickname="ndarray_vsplit",
    description="ndarray_vsplit",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("splitStart", "splitStart", "splitStart", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("splitEnd", "splitEnd", "splitEnd", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("first", "first", "first", access = hs.HopsParamAccess.LIST),
        hs.HopsString("second", "second", "second", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_vsplit_01(rows: int, columns: int, splitStart: int, splitEnd: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrVsplit = np.vsplit(arr, [splitStart, splitEnd])
    print(arrVsplit)
    print(type(arrVsplit))
    return arrVsplit[0].tolist(), arrVsplit[1].tolist()

@hops.component(
    "/ndarray_hsplit_01",
    name="ndarray_hsplit",
    nickname="ndarray_hsplit",
    description="ndarray_hsplit",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("splitStart", "splitStart", "splitStart", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("splitEnd", "splitEnd", "splitEnd", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("first", "first", "first", access = hs.HopsParamAccess.LIST),
        hs.HopsString("second", "second", "second", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_hsplit_01(rows: int, columns: int, splitStart: int, splitEnd: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrHsplit = np.hsplit(arr, [splitStart, splitEnd])
    print(arrHsplit)
    print(type(arrHsplit))
    return arrHsplit[0].tolist(), arrHsplit[1].tolist()

#Stacking Helpers: r_ and c_
#numpy.r_ and numpy.c_ are useful tools for creating stacked arrays 
# in a more concise and readable way
#example of r_
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = rng.standard_normal((3, 2))
print(np.r_[arr1, arr2])
print(np.c_[np.r_[arr1, arr2], arr])

#write this into a @hops component
@hops.component(
    "/ndarray_r_02",
    name="ndarray_r_",
    nickname="ndarray_r_",
    description="ndarray_r_",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list2", "list2", "list2", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list3", "list3", "list3", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list4", "list4", "list4", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list5", "list5", "list5", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("list6", "list6", "list6", access = hs.HopsParamAccess.LIST)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList5", "arrList5", "arrList5", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList6", "arrList6", "arrList6", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_r_02(list1: int, list2: int, list3: int, list4: int, list5: int, list6: int):
    arr1 = np.array([list1, list2])
    arr2 = np.array([list3, list4])
    arr3 = np.array([list5, list6])
    print(arr1)
    print(arr2)
    print(arr3)
    arrR_ = np.r_[arr1, arr2, arr3]
    print(arrR_)
    return arrR_.tolist()[0], arrR_.tolist()[1], arrR_.tolist()[2], arrR_.tolist()[3], arrR_.tolist()[4], arrR_.tolist()[5]




#example of c_
np.c_[1:6, -10:-5]

#see the numpy documentation for more information on r_ and c_
#https://numpy.org/doc/stable/reference/generated/numpy.r_.html
#https://numpy.org/doc/stable/reference/generated/numpy.c_.html

#write this into a @hops component
@hops.component(
    "/ndarray_c_02",
    name="ndarray_c_",
    nickname="ndarray_c_",
    description="ndarray_c_",
    inputs = [
        hs.HopsInteger("start1", "start1", "start1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("end1", "end1", "end1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("start2", "start2", "start2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("end2", "end2", "end2", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList5", "arrList5", "arrList5", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_c_02(start1: int, end1: int, start2: int, end2: int):
    arrC_ = np.c_[start1:end1, start2:end2]
    print(arrC_)
    return arrC_.tolist()[0], arrC_.tolist()[1], arrC_.tolist()[2], arrC_.tolist()[3], arrC_.tolist()[4]

#Repeating Elements: tile and repeat
#numpy.tile and numpy.repeat are useful tools for repeating or replicating arrays 
#to produce larger arrays
#example of tile
arr = np.arange(3)
print(arr)
print(np.repeat(arr, 3))
#broadcasting is used to replicate the array more often along different axes with numpy.tile
print(arr.repeat([2, 3, 4]))

#write this into a @hops component
@hops.component(
    "/ndarray_repeat_01",
    name="ndarray_repeat",
    nickname="ndarray_repeat",
    description="ndarray_repeat",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("repeating", "repeating", "repeating", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_repeat_01(list1: int, repeating: int):
    arr = np.array(list1)
    print(arr)
    arrRepeated = np.repeat(arr, repeating)
    print(arrRepeated)
    return arrRepeated.tolist()

#write this into a @hops component
@hops.component(
    "/ndarray_tile_01",
    name="ndarray_tile",
    nickname="ndarray_tile",
    description="ndarray_tile",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("repeating", "repeating", "repeating", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_tile_01(list1: int, repeating: int):
    arr = np.array(list1)
    print(arr)
    arrTile = np.tile(arr, repeating)
    print(arrTile)
    return arrTile.tolist()


#multi-dimensional arrays can have each axis tiled multiple times with a single number
#example
arr = rng.standard_normal((2, 2))
print(arr)  
print(np.repeat(arr, 2, axis=0))
#if no axis is specified, the array is flattened before use


#write this into a @hops component
@hops.component(
    "/ndarray_repeat_07",
    name="ndarray_repeat",
    nickname="ndarray_repeat",
    description="ndarray_repeat",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("repeat", "repeat", "repeat", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_repeat_07(rows: int, columns: int, repeat: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrRepeated = np.repeat(arr, repeat, axis=0)
    print(arrRepeated)
    print(type(arrRepeated))
    return arrRepeated.tolist()[0], arrRepeated.tolist()[1], arrRepeated.tolist()[2], arrRepeated.tolist()[3]

#pass an array of integers specifying the number of repetitions along each axis
#to repeat a given slice a different number of times
print(np.repeat(arr, [2, 3], axis=0))
print(np.repeat(arr, [2, 3], axis=1))

#write this into a @hops component
@hops.component(
    "/ndarray_repeat_08",
    name="ndarray_repeat",
    nickname="ndarray_repeat",
    description="ndarray_repeat",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("repeat1", "repeat1", "repeat1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("repeat2", "repeat2", "repeat2", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList5", "arrList5", "arrList5", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_repeat_08(rows: int, columns: int, repeat1: int, repeat2: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrRepeated = np.repeat(arr, [repeat1, repeat2], axis=0)
    print(arrRepeated)
    print(type(arrRepeated))
    return arrRepeated.tolist()[0], arrRepeated.tolist()[1], arrRepeated.tolist()[2], arrRepeated.tolist()[3], arrRepeated.tolist()[4]

#write this into a @hops component with axis = 1
@hops.component(
    "/ndarray_repeat_09",
    name="ndarray_repeat",
    nickname="ndarray_repeat",
    description="ndarray_repeat",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("repeat1", "repeat1", "repeat1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("repeat2", "repeat2", "repeat2", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_repeat_09(rows: int, columns: int, repeat1: int, repeat2: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrRepeated = np.repeat(arr, [repeat1, repeat2], axis=1)
    print(arrRepeated)
    print(type(arrRepeated))
    return arrRepeated.tolist()[0], arrRepeated.tolist()[1]

#tile on the other hand, takes a tuple specifying the number of repetitions along each axis
#example
print(np.tile(arr, 2))

#write this into a @hops component
@hops.component(
    "/ndarray_tile_03",
    name="ndarray_tile",
    nickname="ndarray_tile",
    description="ndarray_tile",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("tileCount", "tileCount", "tileCount", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_tile_03(rows: int, columns: int, tileCount: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrTiled = np.tile(arr, tileCount)
    print(arrTiled)
    return arrTiled.tolist()[0], arrTiled.tolist()[1]

#second argument can be a tuple of integers specifying the number of repetitions along each axis
#example
print(np.tile(arr, (2, 1)))

#example
print(np.tile(arr, (3, 2)))

#write this into a @hops component
@hops.component(
    "/ndarray_tile_04",
    name="ndarray_tile",
    nickname="ndarray_tile",
    description="ndarray_tile",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("tileCount1", "tileCount1", "tileCount1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("tileCount2", "tileCount2", "tileCount2", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList5", "arrList5", "arrList5", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList6", "arrList6", "arrList6", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_tile_04(rows: int, columns: int, tileCount1: int, tileCount2: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrTiled = np.tile(arr, (tileCount1, tileCount2))
    print(arrTiled)
    return arrTiled.tolist()[0], arrTiled.tolist()[1], arrTiled.tolist()[2], arrTiled.tolist()[3], arrTiled.tolist()[4], arrTiled.tolist()[5]

#Fancy Indexing Equivalents: take and put
#numpy.take and numpy.put are useful tools for performing fancy indexing operations
#example of take
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print(arr[inds])
#alternative ndarray methods that are useful in the special case of making a selection 
#from a single axis
print(np.take(arr, inds))
print(arr.put(inds, 42))
print(arr)

#write this into a @hops component
@hops.component(
    "/ndarray_take_01",
    name="ndarray_take",
    nickname="ndarray_take",
    description="ndarray_take",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index4", "index4", "index4", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_take_01(list1: int, index1: int, index2: int, index3: int, index4: int):
    arr = np.array(list1)
    print(arr)
    arrTake = np.take(arr, [index1, index2, index3, index4])
    print(arrTake)
    return arrTake.tolist()

#write this into a @hops component
@hops.component(
    "/ndarray_put_02",
    name="ndarray_put",
    nickname="ndarray_put",
    description="ndarray_put",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index4", "index4", "index4", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value", "value", "value", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),

        ]
)
def ndarray_put_02(list1: int, index1: int, index2: int, index3: int, index4: int, value: int):
    arr = np.array(list1)
    print(arr)
    inds = [index1, index2, index3, index4]
    print(arr.put(inds, value))
    print(arr)
    arr.put(inds, value)
    return arr.tolist()

@hops.component(
    "/ndarray_put_03",
    name="ndarray_put",
    nickname="ndarray_put",
    description="ndarray_put",
    inputs = [
        hs.HopsInteger("list1", "list1", "list1", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index4", "index4", "index4", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value2", "value2", "value2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value3", "value3", "value3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value4", "value4", "value4", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_put_03(list1: int, index1: int, index2: int, index3: int, index4: int, value1: int, value2: int, value3: int, value4: int):
    arr = np.array(list1)
    print(arr)
    inds = [index1, index2, index3, index4]
    vals = [value1, value2, value3, value4]
    print(arr.put(inds, vals))
    print(arr)
    arr.put(inds, vals)
    return arr.tolist()

# to take along a different axis, pass the axis keyword argument
#example
inds = [2, 0, 2, 1]
arr = rng.standard_normal((2, 4))
print(arr)
print(np.take(arr, inds, axis=1))

#write this into a @hops component
@hops.component(
    "/ndarray_take_02",
    name="ndarray_take",
    nickname="ndarray_take",
    description="ndarray_take",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index4", "index4", "index4", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_take_02(rows: int, columns: int, index1: int, index2: int, index3: int, index4: int, axis: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    inds = [index1, index2, index3, index4]
    arrTake = np.take(arr, inds, axis=axis)
    print(arrTake)
    return arrTake.tolist()[0], arrTake.tolist()[1]

#put does not accept an axis argument but instead flattens the array (one-dimensional, C order)
#when you need to set elements using an array on other axes, it is best to use fancy indexing
# []-based indexing or the equivalent take method

"""
██████╗ ██████╗  ██████╗  █████╗ ██████╗  ██████╗ █████╗ ███████╗████████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ 
██████╔╝██████╔╝██║   ██║███████║██║  ██║██║     ███████║███████╗   ██║   ██║██╔██╗ ██║██║  ███╗
██╔══██╗██╔══██╗██║   ██║██╔══██║██║  ██║██║     ██╔══██║╚════██║   ██║   ██║██║╚██╗██║██║   ██║
██████╔╝██║  ██║╚██████╔╝██║  ██║██████╔╝╚██████╗██║  ██║███████║   ██║   ██║██║ ╚████║╚██████╔╝
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""
#Broadcasting
#Broadcasting is a powerful tool that allows numpy to work with arrays of different shapes
#when performing arithmetic operations
#powerful but can lead to confusion, even for experienced users
#the simplest broadcasting example occurs when combining a scalar value with an array
#example
arr = np.arange(5)
print(arr)
print(arr * 4)

#the scalar value 4 has been broadcast to all of the other elements in the multiplication operation
#we can think of the scalar 4 as a 1d array with the shape (1,) that has been broadcast to (5,)
#we demean the array by subtracting the mean value of each column
#example
arr = rng.standard_normal((4, 3))
print(arr.mean(0))
demeaned = arr - arr.mean(0)
print(demeaned)
print(demeaned.mean(0))

#write this into a @hops component
@hops.component(
    "/ndarray_broadcasting_01",
    name="ndarray_broadcasting",
    nickname="ndarray_broadcasting",
    description="ndarray_broadcasting",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_broadcasting_01(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrMean = arr.mean(0)
    print(arrMean)
    demeaned = arr - arrMean
    print(demeaned)
    print(demeaned.mean(0))
    return demeaned.tolist()[0], demeaned.tolist()[1], demeaned.tolist()[2], demeaned.tolist()[3]

#Demeaning the rows as a broadcasting operation requires a bit more care
#Broadcasting is performed on the rightmost dimensions of the arrays
#subtracting the row means from each column of a 2d array
#this is possible if you follow the rules

#the Broadcasting Rule
#two dimensions are compatible for broadcasting if for each trailing dimension
#(starting from the end), the axis lengths match or if either of the lengths is 1
#Broadcasting is then performed over the missing or length 1 dimensions

#Broadcasting over axis 0 with a 1d array
#example
arr = np.random.randn(4, 3)
print(arr.mean(0))
print(arr - arr.mean(0))

#Broadcasting over axis 1 with a 2d array
#to subtract over axis 1 (i.e. subtract the column means from each row), we need to
#reshape the mean array to be a column vector
#example
arr = np.random.randn(4, 3)
print(arr.mean(1))
print(arr.mean(1).reshape((4, 1)))
print(arr - arr.mean(1).reshape((4, 1)))

#Broadcasting over axis 1 with a 2d array
#write this into a @hops component
@hops.component(
    "/ndarray_broadcasting_02",
    name="ndarray_broadcasting",
    nickname="ndarray_broadcasting",
    description="ndarray_broadcasting",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_broadcasting_02(rows: int, columns: int):   
    arr = rng.standard_normal((rows, columns))
    print(arr)
    arrMean = arr.mean(1)
    print(arrMean)
    arrMeanReshaped = arrMean.reshape((rows, 1))
    print(arrMeanReshaped)
    demeaned = arr - arrMeanReshaped
    print(demeaned)
    print(demeaned.mean(1))
    return demeaned.tolist()[0], demeaned.tolist()[1], demeaned.tolist()[2], demeaned.tolist()[3]

#Broadcasting over axis 0 of a 3d array
#example
arr = np.random.randn(3, 4, 2)
arr2 = np.random.randn(4, 2)
#broadcast over the first dimension of arr
print(arr.mean(0).shape)
print(arr2.shape)
print(arr - arr.mean(0))

#write this into a @hops component
#Broadcasting over axis 0 of a 3d array
@hops.component(
    "/ndarray_broadcasting_3d",
    name="ndarray_broadcasting",
    nickname="ndarray_broadcasting",
    description="ndarray_broadcasting",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("depth", "depth", "depth", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_broadcasting_3e(rows: int, columns: int, depth: int):
    arr = rng.standard_normal((rows, columns, depth))
    arr2 = rng.standard_normal((columns, depth))
    print(arr.mean(0).shape)
    print(arr2.shape)
    print(arr - arr.mean(0))
    return (arr - arr.mean(0)).tolist()

#write this into a @hops component
#Broadcasting over axis 0 of a 3d array
@hops.component(
    "/ndarray_broadcasting_3f",
    name="ndarray_broadcasting",
    nickname="ndarray_broadcasting",
    description="ndarray_broadcasting",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("depth", "depth", "depth", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arr1List1", "arr1List1", "arr1List1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr1List2", "arr1List2", "arr1List2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2List1", "arr2List1", "arr2List1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr2List2", "arr2List2", "arr2List2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3List1", "arr3List1", "arr3List1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr3List2", "arr3List2", "arr3List2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4List1", "arr4List1", "arr4List1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arr4List2", "arr4List2", "arr4List2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_broadcasting_3f(rows: int, columns: int, depth: int):
    arr = rng.standard_normal((rows, columns, depth))
    arr2 = rng.standard_normal((columns, depth))
    print(arr.mean(0).shape)
    print(arr2.shape)
    print(arr - arr.mean(0))
    return (arr - arr.mean(0)).tolist()[0][0], (arr - arr.mean(0)).tolist()[0][1], (arr - arr.mean(0)).tolist()[1][0], (arr - arr.mean(0)).tolist()[1][1], (arr - arr.mean(0)).tolist()[2][0], (arr - arr.mean(0)).tolist()[2][1], (arr - arr.mean(0)).tolist()[3][0], (arr - arr.mean(0)).tolist()[3][1]

#Broadcasting over Other Axes
#broadcasting with higher dimensional arrays can seem even more mind-bending
#just follow the rules
#if you don't you will get an error or unexpected result like this
#ValueError: operands could not be broadcast together with shapes (4,3) (4,)

#according to the Broadcasting Rule, the "broadcasting dimensions" must be 1 in the smaller array
#example
arr = np.random.randn(4, 3)
arr - arr.mean(1).reshape((4, 1))
print(arr.mean(1).reshape((4, 1)))

#in the 3D case, you can think of the operation as subtracting a 2d array from a 3d array
#where the 2d array is broadcast across the 3d array
#broadcasting over any of the 3 dimensions is only a matter of reshaping the data
#to be compatible with the higher dimensional array

#broadcast over each axis of a three-dimensional array
#Compatible 2D array of shapes for broadcasting over a 3D array
#the common problem is needing a new axis with length 1 for broadcasting purposes
#using reshape is one option, but inserting an axis requires constructing a tuple indicating
#the new shape
#this can be tedious
#Numpy arrays offer another way to insert a new axis directly with np.newaxis
#along the "full" slices to insert the new axis
#example
arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]
print(arr_3d.shape)

arr_1d = np.random.normal(size=3)
print(arr_1d[:, np.newaxis])
print(arr_1d[np.newaxis, :])

#write this into a @hops component
@hops.component(
    "/ndarray_newaxis_01",
    name="ndarray_newaxis",
    nickname="ndarray_newaxis",
    description="ndarray_newaxis",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("depth", "depth", "depth", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_newaxis_01(rows: int, columns: int, depth: int, count: int):
    arr = rng.standard_normal((rows, columns, depth))
    arr_3d = arr[:, np.newaxis, :]
    print(arr_3d.shape)
    arr_1d = np.random.normal(size=count)
    print(arr_1d[:, np.newaxis])
    print(arr_1d[np.newaxis, :])
    return arr_3d.tolist(), arr_1d[:, np.newaxis].tolist(), arr_1d[np.newaxis, :].tolist()

#write this into a @hops component
@hops.component(
    "/ndarray_newaxis_01c",
    name="ndarray_newaxis",
    nickname="ndarray_newaxis",
    description="ndarray_newaxis",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("depth", "depth", "depth", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_newaxis_01c(rows: int, columns: int, depth: int, count: int):
    arr = rng.standard_normal((rows, columns, depth))
    arr_3d = arr[:, np.newaxis, :]
    print(arr_3d.shape)
    arr_1d = np.random.normal(size=count)
    print(arr_1d[:, np.newaxis])
    print(arr_1d[np.newaxis, :])
    return arr_1d[np.newaxis, :].tolist()[0]

#if we had a 3D array and wanted to demean axis 2, we would need to insert a new axis
#at position 2
#example
arr = rng.standard_normal((3, 4, 5))
depth_means = arr.mean(2)
print(depth_means)
depth_means.shape
demeaned = arr - depth_means[:, :, np.newaxis]
print(demeaned.mean(2))

#write this into a @hops component
@hops.component(
    "/ndarray_newaxis_02c",
    name="ndarray_newaxis",
    nickname="ndarray_newaxis",
    description="ndarray_newaxis",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("depth", "depth", "depth", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_newaxis_02c(rows: int, columns: int, depth: int, count: int):
    arr = rng.standard_normal((rows, columns, depth))
    depth_means = arr.mean(2)
    print(depth_means)
    print(depth_means.shape)
    demeaned = arr - depth_means[:, :, np.newaxis]
    print(demeaned.mean(2))
    return depth_means.tolist(), demeaned.tolist(), demeaned.mean(2).tolist()

#write this into a @hops component
@hops.component(
    "/ndarray_newaxis_02e",
    name="ndarray_newaxis",
    nickname="ndarray_newaxis",
    description="ndarray_newaxis",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("depth", "depth", "depth", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList5", "arrList5", "arrList5", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList6", "arrList6", "arrList6", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList7", "arrList7", "arrList7", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList8", "arrList8", "arrList8", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_newaxis_02e(rows: int, columns: int, depth: int, count: int):
    arr = rng.standard_normal((rows, columns, depth))
    depth_means = arr.mean(2)
    print(depth_means)
    print(depth_means.shape)
    demeaned = arr - depth_means[:, :, np.newaxis]
    print(demeaned)
    print(demeaned.mean(2))
    return demeaned.tolist()[0][0], demeaned.tolist()[0][1], demeaned.tolist()[1][0], demeaned.tolist()[1][1], demeaned.tolist()[2][0], demeaned.tolist()[2][1], demeaned.tolist()[3][0], demeaned.tolist()[3][1]

#you might want to generalize demeaning over an axis without sacrificing performance
#you can do this by writing some indexing gymnastics
#example 
arr = rng.standard_normal((3, 4, 5))
row_means = arr.mean(1)
print(row_means)
print(row_means.shape)
demeaned = arr - row_means[:, np.newaxis, :]
print(demeaned.mean(1))

#example
def demean_axis(arr, axis=0):
    means = arr.mean(axis)

    #this generalized things like [:, :, np.newaxis] to work across any number of dimensions
    #the tuple (slice(None),) is equivalent to [:]
    #the tuple (slice(None), np.newaxis) is equivalent to [:, np.newaxis]
    #the tuple (slice(None), np.newaxis, :, np.newaxis) is equivalent to [:, np.newaxis, :, np.newaxis]
    #and so on
    indexer = [slice(None)] * arr.ndim
    indexer[axis] = np.newaxis
    return arr - means[indexer]

#Setting Array Values by Broadcasting
#you can use broadcasting to set multiple values in a regular fashion
#indexing with slices and integers always creates a view of the original array
#this is a nice feature as it means that you can modify the view and the original array
#will be modified as well
#example
arr = np.zeros((4, 3))
arr[:] = 5
print(arr)

#write this into a @hops component
@hops.component(
    "/ndarray_broadcasting_03",
    name="ndarray_broadcasting",
    nickname="ndarray_broadcasting",
    description="ndarray_broadcasting",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value", "value", "value", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_broadcasting_03(rows: int, columns: int, value: int):
    arr = np.zeros((rows, columns))
    arr[:] = value
    print(arr)
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2], arr.tolist()[3]

#however if we had a 1D array of values we wanted to set into the columns of the array
#we can do it like this so long as the shape is compatible
#example
col = np.array([1.28, -0.42, 0.44, 1.6])
arr[:] = col[:, np.newaxis]
print(arr)

#set up until the first two columns
arr[:2] = [[-1.37], [0.509]]
print(arr)

#write this into a @hops component
@hops.component(
    "/ndarray_broadcasting_04",
    name="ndarray_broadcasting",
    nickname="ndarray_broadcasting",
    description="ndarray_broadcasting",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value2", "value2", "value2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value3", "value3", "value3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value4", "value4", "value4", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value5", "value5", "value5", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_broadcasting_04(rows: int, columns: int, value1: int, value2: int, value3: int, value4: int, value5: int):
    arr = np.zeros((rows, columns))
    arr[:] = value1
    print(arr)
    col = np.array([value2, value3, value4, value5])
    arr[:] = col[:, np.newaxis]
    print(arr)
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2], arr.tolist()[3]

#write this into a @hops component
@hops.component(
    "/ndarray_broadcasting_06",
    name="ndarray_broadcasting",
    nickname="ndarray_broadcasting",
    description="ndarray_broadcasting",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value2", "value2", "value2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value3", "value3", "value3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_broadcasting_06(rows: int, columns: int, value1: int, value2: int, value3: int, index1: int):
    arr = np.zeros((rows, columns))
    arr[:] = value1
    print(arr)
    arr[:index1] = [[value2], [value3]]
    print(arr)
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2], arr.tolist()[3]

#Advanced ufunc Usage
#some ufuncs can be used in a more advanced fashion
#to help you write more concise code
#and avoid for loops

#ufunc Instance Methods
#NumPy's ufuncs have a number of useful methods that can be used to perform operations
#accumulate: performs a binary reduce operation on all elements in the array
#at(x, indices, b=None): performs an in-place application of the binary operation at the specified indices
#reduce(x, axis=0, dtype=None, out=None, keepdims=False): performs a reduce operation on the array
#reduceat(x, indices, axis=0, dtype=None, out=None): performs a reduce operation on all elements in the array grouped by the indices
#outer(a, b, out=None): performs a vectorized cross product between a and b

#reduce takes a single array and aggregates its values successively along an axis
#optionally along a different axis by performing a binary operation
#an alternative way to sum an array's values is to use the reduce method
#np.add.reduce is equivalent to np.sum
#example
arr = np.arange(10)
print(np.add.reduce(arr))
print(arr.sum())

#write this into a @hops component
@hops.component(
    "/ndarray_reduce_02",
    name="ndarray_reduce",
    nickname="ndarray_reduce",
    description="ndarray_reduce",
    inputs = [
        hs.HopsNumber("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_reduce_02(count: int):
    arr = np.arange(count)
    print(np.add.reduce(arr))
    print(arr.sum())
    return arr.sum()

#use the np.logical_and to check whether the values in each row of a 2d array are sorted
#example
my_rng = np.random.default_rng(12346) #for reproducibility
arr = my_rng.standard_normal((5, 5))
print(arr)
print(arr[::2].sort(1)) #sort a few rows
print(arr[:, :-1] < arr[:, 1:]) #check whether rows are sorted
print(np.logical_and.reduce(arr[:, :-1] < arr[:, 1:], axis=1)) #check whether rows are sorted
#note that logical_and.reduce is equivalent to all method

#write this into a @hops component
@hops.component(
    "/ndarray_reduce_12",
    name="ndarray_reduce",
    nickname="ndarray_reduce",
    description="ndarray_reduce",   
    inputs = [  
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsBoolean("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_reduce_12(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(arr)
    print(arr[::2].sort(1))
    print(arr[:, :-1] < arr[:, 1:])
    print(np.logical_and.reduce(arr[:, :-1] < arr[:, 1:], axis=1))  
    return np.logical_and.reduce(arr[:, :-1] < arr[:, 1:], axis=1).tolist()

#accumulate performs a binary operation on all elements in the array
#like cumsum is related to sum, accumulate is related to reduce
#accumulate is equivalent to calling reduce with keepdims=True
#example
arr = np.arange(15).reshape((3, 5))
print(np.add.accumulate(arr, axis=1))

#write this into a @hops component
@hops.component(
    "/ndarray_accumulate_01",
    name="ndarray_accumulate",
    nickname="ndarray_accumulate",
    description="ndarray_accumulate",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_accumulate_01(rows: int, columns: int):
    arr = rng.standard_normal((rows, columns))
    print(np.add.accumulate(arr, axis=1))
    return np.add.accumulate(arr, axis=1).tolist()[0], np.add.accumulate(arr, axis=1).tolist()[1], np.add.accumulate(arr, axis=1).tolist()[2]



#outer performs a vectorized cross product between two arrays
#example
arr = np.arange(3).repeat([1, 2, 2])
print(arr)
print(np.multiply.outer(arr, np.arange(5)))

#write this into a @hops component
@hops.component(
    "/ndarray_outer_01",
    name="ndarray_outer",
    nickname="ndarray_outer",
    description="ndarray_outer",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList5", "arrList5", "arrList5", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_outer_01(count: int):
    arr = np.arange(count).repeat([1, 2, 2])
    print(arr)
    print(np.multiply.outer(arr, np.arange(5)))
    return np.multiply.outer(arr, np.arange(5)).tolist()[0], np.multiply.outer(arr, np.arange(5)).tolist()[1], np.multiply.outer(arr, np.arange(5)).tolist()[2], np.multiply.outer(arr, np.arange(5)).tolist()[3], np.multiply.outer(arr, np.arange(5)).tolist()[4]

#the output of the outer will have a dimension that is the concatenation of the dimensions of the inputs
#example
x, y = rng.standard_normal((3, 4)), rng.standard_normal(5)
result = np.subtract.outer(x, y)
print(result.shape)

#write this into a @hops component
@hops.component(
    "/ndarray_outer_03",
    name="ndarray_outer",
    nickname="ndarray_outer",
    description="ndarray_outer",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsString("shape", "shape", "shape", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_outer_03(rows: int, columns: int, count: int):
    x, y = rng.standard_normal((rows, columns)), rng.standard_normal(count)
    result = np.subtract.outer(x, y)
    print(result.shape)
    return result.tolist()[0][0], result.shape

#reduceat performs a reduce operation on all elements in the array grouped by the indices
#slices are agragate together
#it accepts a sequence of "bins" that indicate how to split the values
#bin edges are inclusive on the left and exclusive on the right
#example
arr = np.arange(10)
print(np.add.reduceat(arr, [0, 5, 8]))
#the results are equivalent to calling reduce with the slices, arr[:5], arr[5:8], arr[8:]

#write this into a @hops component
@hops.component(
    "/ndarray_reduceat_01",
    name="ndarray_reduceat",
    nickname="ndarray_reduceat",
    description="ndarray_reduceat",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.ITEM)
        ]
)
def ndarray_reduceat_01(count: int, index1: int, index2: int, index3: int):
    arr = np.arange(count)
    print(np.add.reduceat(arr, [index1, index2, index3]))
    return np.add.reduceat(arr, [index1, index2, index3]).tolist()[0], np.add.reduceat(arr, [index1, index2, index3]).tolist()[1], np.add.reduceat(arr, [index1, index2, index3]).tolist()[2]

#you can also pass a second argument to reduceat to specify the axis
#example
arr = np.multiply.outer(np.arange(4), np.arange(5))
print(arr)
print(np.add.reduceat(arr, [0, 2, 4], axis=1))

#write this into a @hops component
@hops.component(
    "/ndarray_reduceat_03",
    name="ndarray_reduceat",
    nickname="ndarray_reduceat",
    description="ndarray_reduceat",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_reduceat_03(rows: int, columns: int, index1: int, index2: int, index3: int, axis: int):
    arr = np.multiply.outer(np.arange(rows), np.arange(columns))
    print(arr)
    print(np.add.reduceat(arr, [index1, index2, index3], axis=axis))
    return np.add.reduceat(arr, [index1, index2, index3], axis=axis).tolist()[0], np.add.reduceat(arr, [index1, index2, index3], axis=axis).tolist()[1], np.add.reduceat(arr, [index1, index2, index3], axis=axis).tolist()[2], np.add.reduceat(arr, [index1, index2, index3], axis=axis).tolist()[3]

#writing new ufuncs in Python
#NumPy provides a mechanism for creating your own ufuncs in Python
#use NumPy C API to write a ufunc in C
#use NumPy's ufunc machinery to create a ufunc in Python
#the second option is easier and sufficient for most purposes

#numpy.frompyfunc accepts a Python function along with the number of input and output arguments
#and returns a NumPy ufunc
#example
def add_elements(x, y):
    return x + y

add_them = np.frompyfunc(add_elements, 2, 1)
print(add_them(np.arange(8), np.arange(8))) #returns array([0, 2, 4, 6, 8, 10, 12, 14], dtype=object)

#write this into a @hops component
@hops.component(
    "/ndarray_frompyfunc_01",
    name="ndarray_frompyfunc",
    nickname="ndarray_frompyfunc",
    description="ndarray_frompyfunc",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_frompyfunc_01(count: int):
    add_them = np.frompyfunc(add_elements, 2, 1)
    print(add_them(np.arange(count), np.arange(count)))
    return add_them(np.arange(count), np.arange(count)).tolist()


#these always return Python objects rather than NumPy arrays
#you can convert the output to an array with astype
# or use the np.vectorize decorator, that allows your to specify the output type
#example
add_them = np.vectorize(add_elements, otypes=[np.float64])
print(add_them(np.arange(8), np.arange(8)))

#these functions provide a way to create NumPy ufuncs in Python, but they are slow 
#which is much slower that the numpy C-based ufuncs loops
#you should only use them for low-performance applications
#or when there is no other option

arr = rng.standard_normal((10000))
#run in IPython
"""
%timeit add_them(arr, arr) #returns 1000 loops, best of 3: 1.02 ms per loop
%timeit np.add(arr, arr) #returns 10000 loops, best of 3: 32.8 µs per loop
"""

#Structured and Record Arrays
#NumPy allows you to create arrays of compound data types
#Tabular data or other heterogeneous data can be represented
#by structured arrays
#a structured array is an array whose datatype is a composition of simpler datatypes
#a struct in C or a record in Pascal or a DataFrame in pandas or a table in SQL or a dict in Python
#or a Series in pandas or a list in Python or a tuple in Python or a namedtuple in Python
#example
dtype = [('x', np.float64), ('y', np.int32)]
sarr = np.array([(1.5, 6), (np.pi, -2)], dtype=dtype)
print(sarr) #returns array([(1.5, 6), (3.141592653589793, -2)], dtype=[('x', '<f8'), ('y', '<i4')])
#also returns (1.5, 6) (3.141592653589793, -2)

#there are many ways to specify a structured dtype (see the online NumPy documentation)
#one typical way is as a list of tuples with (field_name, field_data_type)
#Now, the elements of the array are tuple-like objects and can be accessed by a dictionary-like syntax
#example
print(sarr[0]) #returns (1.5, 6)
print(sarr[0]['y'])

#write this into a @hops component
@hops.component(
    "/ndarray_structured_03",
    name="ndarray_structured",
    nickname="ndarray_structured",
    description="ndarray_structured",
    inputs = [
        hs.HopsNumber("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value2", "value2", "value2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("value3", "value3", "value3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("value4", "value4", "value4", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_structured_03(value1: int, value2: int, value3: int, value4: int):
    dtype = [('x', np.float64), ('y', np.int32)]
    sarr = np.array([(value1, value2), (value3, value4)], dtype=dtype)
    print(sarr) #returns array([(1.5, 6), (3.141592653589793, -2)], dtype=[('x', '<f8'), ('y', '<i4')])
    print(sarr[0]) #returns (1.5, 6)
    print(sarr[0]['y']) #returns 6
    return sarr[0]['y'].tolist(), sarr[0]['x'].tolist(), sarr[1]['y'].tolist()

#Nested dtypes and Multidimensional Fields
#you can create a dtype where one of the fields is another structured dtype
#example
dtype = [('x', np.int64, 3), ('y', np.int32)]
arr = np.zeros(4, dtype=dtype)
print(arr) 
#returns array([([0, 0, 0], 0), ([0, 0, 0], 0), ([0, 0, 0], 0), ([0, 0, 0], 0)], dtype=[('x', '<i8', (3,)), ('y', '<i4')])
print(arr[0]['x']) #returns [0 0 0]
print(arr['x']) #returns [[0 0 0] [0 0 0] [0 0 0] [0 0 0]]
print(arr['y']) #returns [0 0 0 0]
print(arr['y'][0]) #returns 0

#write this into a @hops component
@hops.component(
    "/ndarray_structured_06",
    name="ndarray_structured",
    nickname="ndarray_structured",
    description="ndarray_structured",
    inputs = [
        hs.HopsNumber("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_structured_06(value1: int):
    dtype = [('x', np.int64, 3), ('y', np.int32)]
    arr = np.zeros(4, dtype=dtype)
    print(arr) 
    print(arr[0]['x']) 
    print(arr['x']) 
    print(arr['y']) 
    print(arr['y'][0]) 
    return arr[0]['x'].tolist(), arr['x'].tolist(), arr['y'].tolist(), arr['y'][0].tolist()

#this allows you to express more complicated data sets, nested data structures, 
# or multidimensional data as a single NumPy array
#example
dtype = [('x', [('a', 'f8'), ('b', 'f4')]), ('y', np.int32)]
data = np.array([((1, 2), 5), ((3, 4), 6)], dtype=dtype)
print(data['x']) #returns array[[(1., 1.) (2., 2.)] [(3., 3.) (4., 4.)]], dtype=[('a', '<f8'), ('b', '<f4')])
print(data['y']) #returns array([5, 6], dtype=int32)
print(data['x']['a']) #returns array([[1., 2.], [3., 4.]]), dtype=float64)  

#write this into a @hops component
@hops.component(
    "/ndarray_structured_07",
    name="ndarray_structured",
    nickname="ndarray_structured",
    description="ndarray_structured",
    inputs = [
        hs.HopsNumber("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList4", "arrList4", "arrList4", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_structured_07(value1: int):
    dtype = [('x', [('a', 'f8'), ('b', 'f4')]), ('y', np.int32)]
    data = np.array([((1, 2), 5), ((3, 4), 6)], dtype=dtype)
    print(data['x']) 
    print(data['y']) 
    print(data['x']['a']) 
    return data['x']['a'].tolist(), data['x'].tolist(), data['y'].tolist(), data['y'][0].tolist()

#why use structured arrays?
#structured arrays are a way to represent compound data in NumPy
#they are useful for interfacing with other libraries and systems
#they are not as efficient as using a dictionary or a DataFrame
#time to learn about pandas

#More about Sorting
#NumPy arrays can be sorted in-place using the sort method
#example
arr = np.random.randn(6)
print(arr) #returns array([-0.2047, 0.4789, -0.5194, -0.5557, 1.9658, 1.3934])
arr.sort() #returns array([-0.5557, -0.5194, -0.2047, 0.4789, 1.3934, 1.9658])
print(arr)
# if the array is a view on a larger array, the original array will be modified
#example
arr = np.random.randn(3, 5)
print(arr) #returns array([[-0.2047, 0.4789, -0.5194, -0.5557, 1.9658], [1.3934, 0.0929, 0.2817, 0.769 , 1.2464], [1.0072, -1.2962, 0.275 , 0.2289, 1.3529]])
arr[:, 0].sort() #returns array([-0.2047, 1.0072, 1.3934])
print(arr) #returns array([[-0.2047, 0.4789, -0.5194, -0.5557, 1.9658], [1.0072, 0.0929, 0.2817, 0.769 , 1.2464], [1.3934, -1.2962, 0.275 , 0.2289, 1.3529]])

#write this into a @hops component
@hops.component(
    "/ndarray_sort_05",
    name="ndarray_sort",
    nickname="ndarray_sort",
    description="ndarray_sort",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_sort_05(rows: int, columns: int):
    arr = np.random.randn(rows, columns)
    print(arr)
    arr[:, 0].sort()
    print(arr)
    return arr[:, 0].tolist(), arr[:, 1].tolist(), arr[:, 2].tolist()

#numpy.sort returns a sorted copy of an array instead of modifying the array in-place
#example
arr = np.random.randn(5)
print(arr) #returns array([0.8864, -0.729 , 0.7452, 0.3906, 0.3557])
print(np.sort(arr)) #returns array([-0.729 , 0.3557, 0.3906, 0.7452, 0.8864])
print(arr) #returns array([0.8864, -0.729 , 0.7452, 0.3906, 0.3557])

#write this into a @hops component
@hops.component(
    "/ndarray_sort_06",
    name="ndarray_sort",
    nickname="ndarray_sort",
    description="ndarray_sort",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_sort_06(count: int):
    arr = np.random.randn(count)
    print(arr)
    print(np.sort(arr))
    print(arr)
    return np.sort(arr).tolist(), arr.tolist()

#these take an optional axis argument to sort along a row or column
#example
arr = np.random.randn(3, 5)
print(arr) #returns array([[-0.2047, 0.4789, -0.5194, -0.5557, 1.9658], [1.3934, 0.0929, 0.2817, 0.769 , 1.2464], [1.0072, -1.2962, 0.275 , 0.2289, 1.3529]])
arr.sort(axis=1)
print(arr) #returns array([[-0.5557, -0.5194, -0.2047, 0.4789, 1.9658], [0.0929, 0.2464, 0.2817, 0.769 , 1.3934], [-1.2962, 0.2289, 0.275 , 1.0072, 1.3529]])

#write this into a @hops component
@hops.component(
    "/ndarray_sort_07",
    name="ndarray_sort",
    nickname="ndarray_sort",
    description="ndarray_sort",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_sort_07(rows: int, columns: int, axis: int):
    arr = np.random.randn(rows, columns)
    print(arr)
    arr.sort(axis=axis)
    print(arr)
    return arr[:, 0].tolist(), arr[:, 1].tolist(), arr[:, 2].tolist()

#notice that the top row is sorted in ascending order
#use "TRICK" to sort the top row in descending order
#values[::-1] reverses the values
#example
arr = np.random.randn(3, 5)
print(arr) #returns array([[-0.2047, 0.4789, -0.5194, -0.5557, 1.9658], [1.3934, 0.0929, 0.2817, 0.769 , 1.2464], [1.0072, -1.2962, 0.275 , 0.2289, 1.3529]])
arr.sort(axis=1)
print(arr) #returns array([[-0.5557, -0.5194, -0.2047, 0.4789, 1.9658], [0.0929, 0.2464, 0.2817, 0.769 , 1.3934], [-1.2962, 0.2289, 0.275 , 1.0072, 1.3529]])
arr[:, ::-1] #returns array([[1.9658, 0.4789, -0.2047, -0.5194, -0.5557], [1.3934, 0.769 , 0.2817, 0.2464, 0.0929], [1.3529, 1.0072, 0.275 , 0.2289, -1.2962]])

#write this into a @hops component
@hops.component(
    "/ndarray_sort_08",
    name="ndarray_sort",
    nickname="ndarray_sort",
    description="ndarray_sort",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("axis", "axis", "axis", access = hs.HopsParamAccess.ITEM)
        ],
    outputs = [
        hs.HopsNumber("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
        ]
)
def ndarray_sort_08(rows: int, columns: int, axis: int):
    arr = np.random.randn(rows, columns)
    print(arr)
    arr.sort(axis=axis)
    print(arr)
    print(arr[:, ::-1])
    return arr[:, ::-1].tolist()[0], arr[:, ::-1].tolist()[1], arr[:, ::-1].tolist()[2]

#indirect sorts: argsort and lexsort
#you may need to reorder datasets based on one or more keys
#indexers that return integer indices are called indirect sorts
#example
values = np.array([5, 0, 1, 3, 2])
indexer = values.argsort()
print(indexer) #returns array([1, 2, 4, 3, 0])
print(values[indexer]) #returns array([0, 1, 2, 3, 5])

#write this into a @hops component
@hops.component(
    "/ndarray_argsort_01",
    name="ndarray_argsort",
    nickname="ndarray_argsort",
    description="ndarray_argsort",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_argsort_01(count: int):
    values = np.random.randn(count)
    indexer = values.argsort()
    print(indexer)
    print(values[indexer])
    return indexer.tolist(), values[indexer].tolist()

#you can also sort along a particular axis of a multidimensional array
#example
arr = np.random.randn(3, 5)
print(arr) #returns array([[-0.2047, 0.4789, -0.5194, -0.5557, 1.9658], [1.3934, 0.0929, 0.2817, 0.769 , 1.2464], [1.0072, -1.2962, 0.275 , 0.2289, 1.3529]])
arr[0] = values

#write this into a @hops component
@hops.component(
    "/ndarray_argsort_03",
    name="ndarray_argsort",
    nickname="ndarray_argsort",
    description="ndarray_argsort",
    inputs = [
        hs.HopsInteger("rows", "rows", "rows", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("columns", "columns", "columns", access = hs.HopsParamAccess.ITEM),
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList2", "arrList2", "arrList2", access = hs.HopsParamAccess.LIST),
        hs.HopsString("arrList3", "arrList3", "arrList3", access = hs.HopsParamAccess.LIST)
    ]
)
def ndarray_argsort_03(rows: int, columns: int):
    arr = np.random.randn(rows, columns)
    print(arr)
    arr[0] = values
    print(arr)
    print(arr[:, arr[0].argsort()])
    return arr[:, arr[0].argsort()].tolist()[0], arr[:, arr[0].argsort()].tolist()[1], arr[:, arr[0].argsort()].tolist()[2]

#lexsort is a more general version of argsort that can perform indirect sorts 
# on multiple key arrays
#example
first_name = np.array(['Bob', 'Jane', 'Steve', 'Bill', 'Barbara'])
last_name = np.array(['Jones', 'Arnold', 'Arnold', 'Jones', 'Walters'])
sorter = np.lexsort((first_name, last_name))
print(sorter) #returns array([1, 2, 3, 0, 4])
print(zip(last_name[sorter], first_name[sorter])) #returns <zip object at 0x7f8b1c0b6a00>

#write this into a @hops component
@hops.component(
    "/ndarray_lexsort_02",
    name="ndarray_lexsort",
    nickname="ndarray_lexsort",
    description="ndarray_lexsort",
    inputs = [
        hs.HopsString("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value2", "value2", "value2", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value3", "value3", "value3", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value4", "value4", "value4", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value5", "value5", "value5", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_lexsort_02(value1: str, value2: str, value3: str, value4: str, value5: str):
    first_name = np.array([value1, value2, value3, value4, value5])
    last_name = np.array(['Jones', 'Arnold', 'Arnold', 'Jones', 'Walters'])
    sorter = np.lexsort((first_name, last_name))
    print(sorter)
    zippedList = list(zip(last_name[sorter], first_name[sorter]))
    print(zip(last_name[sorter], first_name[sorter]))
    return zippedList

#Alternative Sort Algorithms
#A stable sort preserves the relative position of elements with equal values
#important where relative ordering is meaningful
#example
values = np.array(['2:first', '2:second', '1:first', '1:second', '1:third'])
key = np.array([2, 2, 1, 1, 1])
indexer = key.argsort(kind='mergesort')
print(indexer) #returns array([2, 3, 4, 0, 1])
values.take(indexer) #returns array(['1:first', '1:second', '1:third', '2:first', '2:second'], dtype='<U8')

#write this into a @hops component
@hops.component(
    "/ndarray_argsort_04",
    name="ndarray_argsort",
    nickname="ndarray_argsort",
    description="ndarray_argsort",
    inputs = [
        hs.HopsString("value1", "value1", "value1", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value2", "value2", "value2", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value3", "value3", "value3", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value4", "value4", "value4", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("value5", "value5", "value5", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_argsort_04(value1: str, value2: str, value3: str, value4: str, value5: str):
    values = np.array([value1, value2, value3, value4, value5])
    key = np.array([2, 2, 1, 1, 1])
    indexer = key.argsort(kind='mergesort')
    print(indexer)
    print(values.take(indexer))
    return values.take(indexer).tolist()

#the only stable sorting algorithm is mergesort, which has 
# a worst-case complexity of O(n log n)
#the default quicksort algorithm is O(n log n) on average, but O(n^2) in the worst case

#array sorting methods, speed, and stability, and work space, worst case
#quicksort, O(n log n), no, O(n^2)
#mergesort, O(n log n), yes, O(n log n)
#heapsort, O(n log n), no, O(n log n)

#Partially Sorting Arrays
#numpy.partition takes an array and a number K
#the result is a new array with the smallest K values to the left of the partition
#and the remaining values to the right, in arbitrary order
#example
arr = np.array([7, 2, 3, 1, 6, 5, 4])
print(arr) #returns array([7, 2, 3, 1, 6, 5, 4])
print(np.partition(arr, 3)) #returns array([2, 1, 3, 4, 6, 5, 7])

#write this into a @hops component
@hops.component(
    "/ndarray_partition_03",
    name="ndarray_partition",
    nickname="ndarray_partition",
    description="ndarray_partition",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_partition_03(count: int, index1: int):
    rng = np.random.default_rng(12345)
    arr = rng.standard_normal(count)
    print(arr)
    print(np.partition(arr, index1))
    return np.partition(arr, index1).tolist()

#numpy.argpartition is the indirect partition analogue of numpy.partition
#example
indices = np.argpartition(arr, 3)
print(indices) #returns array([3, 1, 2, 6, 4, 5, 0])
print(arr.take(indices)) #returns array([1, 2, 3, 4, 6, 5, 7])

#write this into a @hops component
@hops.component(
    "/ndarray_argpartition_02",
    name="ndarray_argpartition",
    nickname="ndarray_argpartition",
    description="ndarray_argpartition",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_argpartition_02(count: int, index1: int):
    rng = np.random.default_rng(12345)
    arr = rng.standard_normal(count)
    print(arr)
    indices = np.argpartition(arr, index1)
    print(indices)
    print(arr.take(indices))
    return arr.take(indices).tolist()

#numpy.searchsorted is an array method that performs a binary search on a sorted array
#returns the index at which a value would need to be inserted to maintain sortedness
#example
arr = np.array([0, 1, 7, 12, 15])
print(arr) #returns array([0, 1, 7, 12, 15])
print(arr.searchsorted(9)) #returns 3

#write this into a @hops component
@hops.component(
    "/ndarray_searchsorted_01",
    name="ndarray_searchsorted",
    nickname="ndarray_searchsorted",
    description="ndarray_searchsorted",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_searchsorted_01(count: int, index1: int):
    arr = np.random.randn(count)
    print(arr)
    print(arr.searchsorted(index1))
    return arr.searchsorted(index1).tolist()

#you can also pass in an array of values to be inserted
#example
arr = np.array([0, 1, 7, 12, 15])
print(arr) #returns array([0, 1, 7, 12, 15])
print(arr.searchsorted([0, 8, 11, 16])) #returns array([0, 3, 3, 5])

#write this into a @hops component
@hops.component(
    "/ndarray_searchsorted_03",
    name="ndarray_searchsorted",
    nickname="ndarray_searchsorted",
    description="ndarray_searchsorted",
    inputs = [
        hs.HopsInteger("list1", "list", "list", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_searchsorted_03(list1: list, index1: int, index2: int, index3: int):
    arr = np.array(list1)
    print(arr)
    print(arr.searchsorted([index1, index2, index3]))
    return arr.searchsorted([index1, index2, index3]).tolist()

#numpy.searchsorted has a side parameter that specifies whether to return
# the leftmost index or rightmost index if the value is not found
#example
arr = np.array([0, 1, 7, 12, 15])
print(arr) #returns array([0, 1, 7, 12, 15])
print(arr.searchsorted(9)) #returns 3
print(arr.searchsorted(9, side='right')) #returns 3
print(arr.searchsorted([0, 8, 11, 16])) #returns array([0, 3, 3, 5])
print(arr.searchsorted([0, 8, 11, 16], side='right')) #returns array([1, 3, 3, 5])

#write this into a @hops component
@hops.component(
    "/ndarray_searchsorted_04",
    name="ndarray_searchsorted",
    nickname="ndarray_searchsorted",
    description="ndarray_searchsorted",
    inputs = [
        hs.HopsInteger("list1", "list", "list", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_searchsorted_04(list1: list, index1: int, index2: int, index3: int):
    arr = np.array(list1)
    print(arr)
    print(arr.searchsorted([index1, index2, index3], side='right'))
    return arr.searchsorted([index1, index2, index3], side='right').tolist()

#numpy.searchsorted is useful for implementing search algorithms
#example
data = np.floor(np.random.uniform(0, 10000, size=50))
bins = np.array([0, 100, 1000, 5000, 10000])
print(data) 
#to get a label for each data point, where I would mean the bucket [0, 100)) 
labels = bins.searchsorted(data)
print(labels) 
#combined with groupby, this can be used to perform a very fast bucket analysis
import pandas as pd
print(pd.Series(data).groupby(labels).mean()) #returns 1    50.0000 2    550.0000 3    2750.0000 4    7500.0000 dtype: float64

#write this into a @hops component  
@hops.component(
    "/ndarray_searchsorted_05",
    name="ndarray_searchsorted",
    nickname="ndarray_searchsorted",
    description="ndarray_searchsorted",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index1", "index1", "index1", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "index2", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index3", "index3", "index3", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index4", "index4", "index4", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index5", "index5", "index5", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_searchsorted_05(count: int, index1: int, index2: int, index3: int, index4: int, index5: int):
    data = np.floor(np.random.uniform(0, 10000, size=count))
    bins = np.array([index1, index2, index3, index4, index5])
    print(data)
    labels = bins.searchsorted(data)
    print(labels)
    print(pd.Series(data).groupby(labels).mean())
    return pd.Series(data).groupby(labels).mean().tolist()

"""
███╗   ██╗██╗   ██╗███╗   ███╗██████╗  █████╗ 
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝███████║
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝
"""

'''
#Writing Fast NumPy Functions with Numba
#Numba is a just-in-time compiler for Python that works best 
# on code that uses NumPy arrays
#https://numba.pydata.org/
#uses CPU and GPU
#uses LLVM compiler infrastructure project, https://llvm.org/
#to translate Python functions into compiled code based on the NumPy array types
#example
import numpy as np
def mean_distance(x, y):
    nx = len(x)
    sum = 0.0
    for i in range(nx):
        result = x[i] - y[i]
        sum += result
    return sum / nx
x = rng.standard_normal(10000000)
y = rng.standard_normal(10000000)
#%timeit mean_distance(x, y) 
#returns 1.2 s ± 8.21 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#NumPy version is much faster
#%timeit (x - y).mean() 
#returns 5.5 ms ± 21.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

#we can turn the function into a Numba function
import numba as nb
#numba_mean_distance = nb.jit(mean_distance)
#%timeit numba_mean_distance(x, y)
#returns 1.2 s ± 8.21 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#we could also have this as a decorator
@nb.jit
def numba_mean_distance(x, y):
    nx = len(x)
    sum = 0.0
    for i in range(nx):
        result = x[i] - y[i]
        sum += result
    return sum / nx

#%timeit numba_mean_distance(x, y)
#returns 1.2 s ± 8.21 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#we could have written
from numba import float64, njit
@njit(float64(float64[:], float64[:]))
def numba_mean_distance(x, y):
    return (x - y).mean() #returns 5.5 ms ± 21.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

#write this into a @hops component
@hops.component(
    "/ndarray_numba_01",
    name="ndarray_numba",
    nickname="ndarray_numba",
    description="ndarray_numba",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_numba_01(count: int):
    rng = np.random.default_rng(12345)
    x = rng.standard_normal(count)
    y = rng.standard_normal(count)
    print(x)
    print(y)
    return (x - y).mean().tolist()

#numba.vectorize decorator creates a NumPy universal function (ufunc)
#that can be used on arrays of any size or dimensionality
#example
import numba as nb
@nb.vectorize
def nb_add(x, y):
    return x + y
x = np.arange(10)
print(nb_add(x, x)) #returns array([ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18])    

#write this into a @hops component
@hops.component(
    "/ndarray_numba_02",
    name="ndarray_numba",
    nickname="ndarray_numba",
    description="ndarray_numba",
    inputs = [
        hs.HopsInteger("count", "count", "count", access = hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsString("arrList1", "arrList1", "arrList1", access = hs.HopsParamAccess.ITEM)
    ]
)
def ndarray_numba_02(count: int):
    rng = np.random.default_rng(12345)
    x = rng.standard_normal(count)
    print(x)
    print(nb_add(x, x))
    return nb_add(x, x).tolist()
'''
#Advanced Array Input and Output























   














if __name__ == "__main__":
    app.run(debug=True)