import Employee from "./employee.js";

export default class Manager extends Employee {
    constructor(name, experience = 0){
        super(name, experience = 0);
        this.moodLevel = 400;
        this.meetingBehavior = false
    }
    work(){
        this.experience +=1;
    }
    meeting(){
        this.meetingBehavior = true;
        this.moodLevel -= this.experience;
    }
}


/*It should have a mood level - in the beginning, this is 400
Whenever it is instructed to work:
It should increase the experience by 1
It should invoke its have a meeting behavior
Whenever have a meeting is invoked, the mood level should decrease by the managers’ experience*/