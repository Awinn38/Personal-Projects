//describe('hello world', function(){
//    it('hello test', function(){

//    });
//});
class Calculator{

    add(a,b){
        return a + b;
    
    }
}

describe('Calculate addition', function(){
    
    it('Should be able to add two numbers together',function(){
     console.log('I was able to add two numbers together')   
    });
    it('Should be able to add two numbers together',function(){
        console.log('I was able to add three numbers together')
    });
    describe('calculate addition with minus numbers',function(){

        it('should be able to add -2 and -2',function(){
            console.log('Just added two minus numbers together')
        })
    })
});
