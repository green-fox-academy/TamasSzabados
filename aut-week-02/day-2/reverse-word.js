str1="lleW ,enod taht saw ton taht drah"

const reverser= (str) =>{
    new_str = str.split(" ");
    var str2 = ""
    for (let i of new_str){
        str2 += [...i].reverse().join("") + " ";
    }
    console.log(str2);
    
}
reverser(str1)