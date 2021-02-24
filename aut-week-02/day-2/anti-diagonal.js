/*Create and test a function called get_anti_diagonal_avg that takes a multidimensional array which represents a square matrix, as a parameter, and returns the average of the numbers in the anti diagonal.

Example 1
Input:

[
  [1, 2, 3],
  [3, 4, 6],
  [5, 2, 5]
]
Output:

4 */

const diagonal = (arr) =>{
    var sum = null;
    for (let i=0; i<arr.length; i++){
        for (let j=0; j<arr[i].length; j++){
            if (i+j == arr.length-1){
                sum += arr[i][j];
            }
        }  
    }
    let average = sum / arr.length;
    console.log(average);
}


const arr2 = [
    [1, 2, 3],
    [3, 4, 6],
    [5, 2, 5]
  ]

diagonal(arr2)

const arr3 = [
    [3, 5, 11, -2],
    [3, 1, 7, 4],
    [5, 0, 2, 9],
    [21, 7, 8, 2]
  ]

  diagonal(arr3)