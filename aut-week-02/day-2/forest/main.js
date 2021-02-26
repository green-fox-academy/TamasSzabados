import Tree from './tree.js'
import Whitebarpine from './whitebarpine.js'
import LumberJack from './lumberJack.js'
import Foxtailpine from './foxtailpine.js'
import Forest from './forest.js'

let tree1 = new Foxtailpine(10)
let tree2 = new Whitebarpine(5)
let blackForest = new Forest(tree1,tree2)
blackForest.isEmpty()
blackForest.getStatus()