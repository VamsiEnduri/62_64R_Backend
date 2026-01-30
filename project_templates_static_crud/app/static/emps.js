// console.log("hello")
let pBtn = document.getElementById("btn");
let employeesListDiv = document.getElementById("employeesListDiv");

// console.log(pBtn)
function fetchAllEmps(){
    employeesListDiv.innerHTML=""
    fetch("http://127.0.0.1:8000/get_employees/")
    .then((res) => res.json())
    .then((res) => {
        let data=res.data
        for(let i=0;i<data.length;i++){
            // console.log(data[i])
            let empDiv= document.createElement("div")
            empDiv.style.backgroundColor="yellow"
            empDiv.innerHTML=`
            <p>${data[i].name}</p>
            `
            employeesListDiv.append(empDiv)
        }
    })
    .catch((err) => console.log(err));
}
document.addEventListener("DOMContentLoaded", () => {
  fetchAllEmps()
});

pBtn.addEventListener("click", () => {
  let n = document.getElementById("name").value;
  let a = document.getElementById("age").value;
  let e = document.getElementById("email").value;
  let d = document.getElementById("dept").value;
  let empData = {
    name: n,
    age: a,
    email: e,
    dept: d,
  };
  console.log(n, a, e, d);
  fetch("http://127.0.0.1:8000/add_employee/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(empData),
  })
    .then((res) => res.json())
    .then((res) => {
        document.getElementById("name").innerHTML=""
        document.getElementById("age").value=""
        document.getElementById("email").value=""
        document.getElementById("dept").value=""
        console.log(res)
        fetchAllEmps()
    })
    .catch((err) => console.log(err));
});
