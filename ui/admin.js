if (localStorage.getItem("role") !== "admin") {
  window.location.href = "/";
}

const API = "/api";

async function loadReports() {
  const res = await fetch(`${API}/report`);
  const data = await res.json();

  let critical = 0,
    warning = 0,
    safe = 0;
  const dash = document.getElementById("dashboard");
  dash.innerHTML = "";

  data.forEach((i) => {
    if (i.severity === "Critical") critical++;
    else if (i.severity === "Medium") warning++;
    else safe++;

    const card = document.createElement("div");
    card.className = "card pulse";
    card.onclick = () => loadTimeline(i.user);

    card.innerHTML = `
      <div class="user">${i.user}</div>
      <div class="meta">${i.incident_id}</div>
      <div class="decision ${i.decision}">${i.decision}</div>
      <div class="bar"><div class="fill" style="width:${i.confidence}%"></div></div>
    `;

    dash.appendChild(card);
  });

  criticalCount.innerText = critical;
  warningCount.innerText = warning;
  safeCount.innerText = safe;
}

async function loadTimeline(user) {
  const res = await fetch(`${API}/timeline/${user}`);
  const events = await res.json();

  const panel = document.getElementById("timeline");
  panel.innerHTML = `<h3>${user}</h3>`;

  events.forEach((e) => {
    const row = document.createElement("div");
    row.className = "log " + e.action;
    row.innerText = `${e.timestamp} | ${e.action} | ${e.resource}`;
    panel.appendChild(row);
  });
}

setInterval(loadReports, 3000);
