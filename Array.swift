//array example

var myarray = [Int]()

myarray.append(20)

myarray.append(100)

myarray.append(10)

var somevar = myarray[1]

//accessing the array element by its index

print(somevar)

//modify element by index value

myarray[2]=1000

print("Iterating through array \n")
//iterating through array

for item in myarray{
    print(item)
}
