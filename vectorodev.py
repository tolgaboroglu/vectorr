 # we will implement the Vector ADT using the Array class implements in the chapter.
 from array_2 import Array

class Vector:
    # Creates a vector capacity of two.
    def __init__(self,size):
        self._size=size
        self._capacity=size*2 
        print(self._size, '--',self._capacity) 
        self._theVector=Array(self._capacity)
        
        #I write code for increase append list
        def append(self,ndxList,item): 
          self._theVector.append(item)
        
    # Returns the number of items in the Vector.
    def __len__(self):
      return self._theVector._len()
    
   #Determines whether the given item is in the vector.
    def __contains__( self,item):
        for i in range(self):
            if self._theVector.item==item:
                return  
        return None
  
    #Returns the item stored in the ndx element of the list.Ndx value must be in valid range
    def __getitem__(self,ndxList):
        return self._theVector[ndxList[0]]
 
    
    # Puts the value in the value at the index position.
    def __setitem__(self,ndxList,item):
        self._theVector[ndxList[0]]=item
    
    def __add__(self,ndxList,item):
        if item not in self._theVector:
            self._theVector.append(item) 
    
     # uses an iterator to return the elements of the vector. creates and returns an iterator.
    def __iter__( self ):
        return _theVector( self._theVector ) 
    
     #Inserts the specified item at its position in the item ndx.Items in given location and subsequent items moved down to make room for the new item. must be in ndx valid range.
    def __insert__(self, item):
        if item not in self._theVector:
            self._theVector.insert(item)
        
     
