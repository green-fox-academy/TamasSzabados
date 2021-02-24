import Tree from './tree.js'

export default class LumberJack extends Tree {
    constructor(height = 0){
        super(height = 0);
    }
    
    cutTree(tree){
        if (this.height >4){
            return true;
        }
        else {
            return false;
        }
    }
}

//You should be able to create a lumberjack without providing any parameters.
//It has a canCut(tree) method which takes a tree as a parameter and returns true if it is taller than 4 units.