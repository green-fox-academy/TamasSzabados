export default class Employee {
    constructor(name, experience = 0){
        this.name = name;
        this.experience = experience;
    }
    work(){

    }
}





/*Every employee has a name, an experience (number), and a method work
The experience should start from 0 by default if it is not provided
Every employee should be able to work, however, the specific behavior is different for every kind
We cannot hire or create basic employee because they should always be some kind of specific employees like Chef, Manager, or Waiter.
*/