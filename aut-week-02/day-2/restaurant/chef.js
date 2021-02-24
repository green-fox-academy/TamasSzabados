import Employee from "./employee.js";

export default class Chef extends Employee {
    constructor(name, experience = 0){
        super(name, experience = 0);
        this.meals = {};
    }
    work(food){
        this.experience +=1;
        if (this.meals[food] == undefined){
            this.meals[food] = 1;
        }
        else{
            this.meals[food] +=1;

        }
    }
}

/*It should store information about the meals it ever cooked (name of the food + amount of times it was cooked)
Whenever it is instructed to work:
It should increase its experience by 1
It should have a cook behavior
This should get the name of the food as an input
This should update the meals information so we are able to track that it cooked this specific food again
Manager*/