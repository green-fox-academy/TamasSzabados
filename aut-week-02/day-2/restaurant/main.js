import Restaurant from "./restaurant.js";
import Employee from "./employee.js";
import Waiter from "./waiter.js";
import Chef from "./chef.js";
import Manager from "./manager.js";

let waiter1 = new Waiter("John");
waiter1.work();
let restaurant = new Restaurant("Michelin Star", 1988);
restaurant.hireEmployee(waiter1);
restaurant.guestsArrive();
console.log(waiter1.tips);
console.log(waiter1.name);
