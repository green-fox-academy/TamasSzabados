import Tree from './tree.js'

export default class Foxtailpine extends Tree {
    constructor(height = 0){
        super(height);
    }
    irrigate(){
        this.height += 1;
    }
}

//This tree type grows by 1 unit each time its irrigated.