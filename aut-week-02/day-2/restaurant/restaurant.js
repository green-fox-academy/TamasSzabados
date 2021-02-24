export default class Restaurant {
    constructor(name, year){
        this.name = name;
        this.year = year;
        this.employees = [];
    }
    guestsArrive(){
        for(let i of this.employees){
            i.work();
        }
    }
    hireEmployee(employee){
        this.employees.push(employee);
    }
}



/*Every restaurant has a name, the year it was founded, and a list of employees who are working there.
It should have a method called “guests arrived” which should instruct all employees to work
We should be able to hire an employee which will add it to the list of employees*/