function login() {
  const role = document.getElementById("role").value;
  localStorage.setItem("role", role);

  if (role === "admin") {
    window.location.href = "/admin.html";
  } else {
    window.location.href = "/employee.html";
  }
}
