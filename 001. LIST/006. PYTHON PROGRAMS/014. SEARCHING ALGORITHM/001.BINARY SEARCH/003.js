 /* BINARY SEARCH IN JS */


let arr = [10,20,30,40,50]
let s=40
let l=0
let r= arr.length-1

while(l<=r){
    let m = Math.floor((l + r) / 2);
    if(arr[m]==s){
        console.log(m)
        break
    }
    else if(arr[m]<s){
        l = m+1
    }
    else if(arr[m]>s){
        r =m-1
    }
}

/* WHY Math.floor()  ???


search in chatgpt */


