// // // async function  getData() { //sync js --> async js
// // //    let data=await fetch("https://fakestoreapi.com/products")
// // //    .then(res=>res.json())
// // //    console.log(data,"data fetched")

// // // }
// // // getData()

// // // let a=fetch("https://fakestoreapi.com/products")
// // // .then(res=>res.json())
// // // .then(res=>console.log(res,"12"))
// // // console.log(a,"13")
// // // console.log("10000","14")

// // async function  getData() {//sync js --> async js
// //    let data=await fetch("https://fakestoreapi.com/products")
// //    .then(res=>res.json())
// //    console.log(data,"data fetched")
// // }
// // getData()
// // console.log(data)

// console.log("Start");

// const start = Date.now();
// while (Date.now() - start < 10000) { // js engine waits here until time expires
//   // busy wait — blocks main thread
// }

// console.log("After 10 seconds");

// // //  20sec 20sec wait
// // let a=fetch('https://dummyjson.com/products')
// // .then(res => res.json())

// // console.log(a,"46")

// // let b=fetch("https://fakestoreapi.com/products")
// // .then(res=>res.json())
// // console.log(b,"51")

// async function getData() {
//   let data = await fetch("https://fakestoreapi.com/products").then((res) =>
//     res.json(),
//   );
//   console.log(data, "data fetched");
// }
// getData()
let cardsContainer=document.getElementById("cardsContainer")

async function getData2() {
  let data =await fetch("https://dummyjson.com/recipes").then((res) =>
    res.json(),
  );
  console.log(data)
  for ( let i =0;i<data.recipes.length;i++){
    // console.log(data.products[i])
    let cardDiv=document.createElement("div")
    cardDiv.style.backgroundColor="yellow"
    cardDiv.style.padding="10px"
    cardDiv.style.margin="10px"
    cardDiv.style.width="250px"
    cardDiv.style.height="300px"
    cardDiv.innerHTML=`
    <img src="${data.recipes[i].image}" width="100%"/>
    <h2>${data.recipes[i].name}</h2>
    <span>${data.recipes[i].rating}</span>
    `
    cardsContainer.append(cardDiv)
  }
}
getData2()

