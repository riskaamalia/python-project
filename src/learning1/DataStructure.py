# learning python for new project , I use python 3.5
# Thanks to tutorialpoint.com
# riskaamalia

# I define all module here

def examplePrint (str) :
    print ("1. Normal string%s \n",str)
    print ("1. Sub string%s \n",str[0:3])

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;


# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

def listAndTuple () :
    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, "john"]

    # tuple can not be update
    tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
    tinytuple = (123, 'john')

    print (tuple)           # Prints complete list
    print (tuple[0])        # Prints first element of the list
    print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
    print (tuple[2:])       # Prints elements starting from 3rd element
    print (tinytuple * 2)   # Prints list two times
    print (tuple + tinytuple) # Prints concatenated lists

    print(list)
    print(list[2])


def exampleDictionary () :
    dict = {}
    dict['one'] = "This is one"
    dict[2]     = "This is two"

    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


    print (dict['one'])       # Prints value for 'one' key
    print (dict[2])           # Prints value for 2 key
    print (tinydict)          # Prints complete dictionary
    print (tinydict.keys())   # Prints all the keys
    print (tinydict.values()) # Prints all the values


# call method here
# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))


# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
