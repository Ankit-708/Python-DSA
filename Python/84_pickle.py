import pickle

# pickling a python object

# cars = ["audi", "bmw", "maruti suzuki"]       #Here we has pickle the object and maked a file and stored them now we will unpickled it 
# file = "mycar.pkl"                            #Here we has pickle the object and maked a file and stored them now we will unpickled it 
# fileobj = open(file, 'wb') (word, binary)     #Here we has pickle the object and maked a file and stored them now we will unpickled it 
# pickle.dumb(cars, fileobj)                    #Here we has pickle the object and maked a file and stored them now we will unpickled it 
# fileobj.close()                               #Here we has pickle the object and maked a file and stored them now we will unpickled it 

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
