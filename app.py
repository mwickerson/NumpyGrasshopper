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

#conberting or casting an array from one dtype to another
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

"""
#Universal Functions: Fast Element-Wise Array Functions
#ufuncs perform element-wise operations on data in ndarrays
#can be used as a fast vectorized wrapper for simple functions that take 
# one or more scalar values and produce one or more scalar results
#many ufuncs are simple element-wise transformations, like sqrt or exp
#these are referred to as unary ufuncs
#others, such as add or maximum, take 2 arrays (thus, binary ufuncs) and
#return a single array as the result

#examples
#sqrt and exp





















if __name__ == "__main__":
    app.run(debug=True)