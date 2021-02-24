import Tree from './tree.js'
import Whitebarkpine from './whitebarkpine.js'
import LumberJack from './lumberJack.js'
import Foxtailpine from './foxtailpine.js'




export default class Forest {
    constructor(trees){
        this.trees = trees;

}








/*It should have a list of trees.
We should be able to create a forest by receiving a list of trees.
It has a rain method which should iterate through the trees and irrigate them one by one.
It has a cutTrees(lumberjack) which should remove all the trees which can be cut by the lumberjack. (It calls the can_cut method on the lumberjack).
It has an isEmpty method which returns true if there is no tree in the forest.
It has a get status method that returns a list with status reports about each tree in the forest. For example:

  'There is a 3 tall WhitebarkPine in the forest.',
  'There is a 2 tall WhitebarkPine in the forest.',
  'There is a 4 tall FoxtailPine in the forest.'

*/