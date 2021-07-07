// Variables 
var number = 4;
var myString = "Variables are great!"
var myBoolean = false
console.log(number)
console.log(myString)
console.log(myBoolean)


// Arrays
var myArray = [1,2,3,4,5];
var theSameArray = new Array(1,2,3)
console.log(myArray[1])
var spaceArray = []
spaceArray[3] = "hello"
console.log(spaceArray)
var specialArray = ["What is the meaning of life",42,true]
console.log(specialArray)

// Push and Pop 
var myStack = [];
myStack.push(1);
myStack.push(2);
myStack.push(3);
console.log(myStack.pop());
console.log(myStack);
var myQueue = [];
myQueue.push(1);
myQueue.push(2);
myQueue.push(3);

// Shifting/Unshifting
console.log(myQueue.shift())
console.log(myQueue.shift())
console.log(myQueue.shift())
myArray.unshift(0);
console.log(myArray)

// Splicing 
var splicedArray = [0,1,2,3,4,5,6,7,8,9];
var splice = splicedArray.splice(3,4);
console.log(splice);
console.log(splicedArray)

// Push/Shift/Pop
var testArray = [1,2,3,4,5];
testArray.push(42);
testArray.shift();
console.log(testArray.pop())
console.log(testArray)

// Arrows
const greet = (name,number,NewName) => {return 1*name + 4+ number + " "+ NewName}
//console.log(greet("4",4,"Antonio"))

// Class/Objects
function Person(name,age) {
    this.name = name
    this.age  = age
    this.describe = function(){
    return this.name+ ","+" " + this.age + " "+ "years old"
    }
}
var pal = new Person("Antonio",23)
//console.log(pal.describe())

// Call/Bind
var  person = {
    name: "Antonio"

}

var Animal = {
    Sheep : "Georgie"
}

function printName(){
    console.log(this.name)
}
function printAnimal(){
    console.log(this.Sheep)
}
var Human = printName.bind(person)
var Animal= printAnimal.bind(Animal)
Human()
Animal()

// Prototype 
function Person(name, age)
{
    this.name = name;
    this.age = age;

    function describe()
    {
        return this.name + ", " + this.age + " years old.";
    }
}