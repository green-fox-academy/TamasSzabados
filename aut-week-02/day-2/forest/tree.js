export default class Tree{
    constructor(height = 0){
        this.height = height;
    }
    irrigate(){

    }
    getHeight(){
        return this.height;
    }
}


/*Trees should have a height.

We should be able to create trees in two ways:

providing height
not providing height, in this case, the height will be 0 by default.
It has an irrigate method which will increase the height of the tree. The implementation should depend on the type of tree.
It has a get height method that returns the tree's height.*/