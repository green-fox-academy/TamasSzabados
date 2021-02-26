import Tree from './tree.js'

export default class Whitebarpine extends Tree {
    constructor(height = 0){
        super(height);
    }
    irrigate(){
        this.height += 2;
    }
}

//This tree type grows by 2 units each time its irrigated.