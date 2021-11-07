const myarray=["Java","C++","C++","Python"]

console.log(myarray);
console.log(myarray[2])
console.log(myarray[4]) //undefined

//we can store different types of data inside the array even functions

const newArray =[
    {1:"Python"},
    [12,45,55],
    function display(){console.log("This is inside the array function");}

]

console.log(newArray)

console.log(newArray[1][2]) //55

