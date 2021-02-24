import Employee from './employee.js'

export default class Waiter extends Employee {
    constructor(name, experience = 0,  tips = 0){
        super(name, experience = 0);
        this.tips = tips;
    }
    work(){
        this.tip +=1;
        this.experience +=1;
    }
}



/*It should store the number of tips it has - in the beginning, this is 0
Whenever it is instructed to work:
It should increase the number of tips by 1
It should increase its experience by 1*/