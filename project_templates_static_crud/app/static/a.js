// console.log("hello")
let pBtn = document.getElementById("btn");
let employeesListDiv = document.getElementById("employeesListDiv");
employeesListDiv.style.width = "100%";
let tBody = document.getElementById("tBody");
let btn_edit = document.getElementById("btn-edit");
tBody.backgroundColor = "yellow";


function deleteEmp(emp_id) {
  // alert(`dlte func triggered ${emp_id}`)
  fetch(`http://127.0.0.1:8000/delete_emp/${emp_id}/`, {
    method: "DELETE",
  })
    .then((res) => res.json())
    .then((res) => {
      alert(`${res}`);
      fetchAllEmps();
    });
}

function editEmp(emp_id, emp_name, emp_age, emp_email, emp_dept) {
  document.getElementById("name").value = emp_name;
  document.getElementById("age").value = emp_age;
  document.getElementById("email").value = emp_email;
  document.getElementById("dept").value = emp_dept;
  document.getElementById("btn").style.display = "none";
  document.getElementById("btn-edit").style.display = "block";
  console.log(emp_id, emp_name);
  btn_edit.addEventListener("click", () => {
    let n = document.getElementById("name").value;
    let a = document.getElementById("age").value;
    let e = document.getElementById("email").value;
    let d = document.getElementById("dept").value;

    fetch(`http://127.0.0.1:8000/update_emp/${emp_id}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: n, age: a, email: e, dept: d }),
    })
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
        document.getElementById("name").value = "";
        document.getElementById("age").value = "";
        document.getElementById("email").value = "";
        document.getElementById("dept").value = "";
        fetchAllEmps()
      });
  });
}
// console.log(pBtn)
function fetchAllEmps() {
  // alert("aaa")

  employeesListDiv.innerHTML = "";
  fetch("http://127.0.0.1:8000/get_employees/")
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
      // e.preventDefault()
      let data = res.data;
      let empTH = document.createElement("tr");
      empTH.innerHTML = `
            <th>name</th>
                <th>age</th>
                <th>email</th>
                <th>dept</th>
                <th>operations</th>
            
            `;
      for (let i = 0; i < data.length; i++) {
        // console.log(data[i])

        let empTR = document.createElement("tr");
        // empTR.style.backgroundColor="purple"
        empTR.innerHTML = `
            <td>${data[i].name}</td>
            <td>${data[i].age}</td>
            <td>${data[i].email}</td>
            <td>${data[i].dept}</td>
            <td>
            <button onclick="editEmp('${data[i].id}','${data[i].name}','${data[i].age}','${data[i].email}','${data[i].dept}')">Edit</button>
            <button onclick="deleteEmp('${data[i].id}')">Delete</button>
            </td>
            `;
        tBody.append(empTR);
        employeesListDiv.append(empTH, tBody);
      }
    })
    .catch((err) => console.log(err));
}
// fetchAllEmps()
document.addEventListener("DOMContentLoaded", () => {
  fetchAllEmps();
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
      document.getElementById("name").value = "";
      document.getElementById("age").value = "";
      document.getElementById("email").value = "";
      document.getElementById("dept").value = "";
      console.log(res);
      fetchAllEmps();
    })
    .catch((err) => console.log(err));
});
