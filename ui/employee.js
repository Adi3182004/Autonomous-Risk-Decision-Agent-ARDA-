if (localStorage.getItem("role") !== "employee") {
  window.location.href = "/";
}

function send(action) {
  fetch("/api/agent", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user: "aditya",
      action: action,
    }),
  });
}
