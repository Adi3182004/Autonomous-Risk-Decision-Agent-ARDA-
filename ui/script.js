const API = "/api";

async function loadReports() {
  try {
    const res = await fetch(`${API}/report`);
    if (!res.ok) throw new Error("Report API failed");

    const data = await res.json();

    const dashboard = document.getElementById("dashboard");
    dashboard.innerHTML = "";

    let critical = 0;
    let warning = 0;
    let safe = 0;

    data.forEach((incident) => {
      if (incident.severity === "Critical") critical++;
      else if (incident.severity === "High" || incident.severity === "Medium")
        warning++;
      else safe++;

      const card = document.createElement("div");
      card.className = incident.severity === "Critical" ? "card pulse" : "card";

      card.onclick = () => loadTimeline(incident.user);

      card.innerHTML = `
        <div class="user">${incident.user}</div>
        <div class="meta">${incident.incident_id}</div>

        <span class="badge ${incident.severity}">
          ${incident.severity}
        </span>
        <span class="badge">${incident.threat_type}</span>

        <div class="bar">
          <div class="fill" style="width:${incident.confidence}%"></div>
        </div>

        <div class="decision ${incident.decision}">
          ACTION: ${incident.decision}
        </div>

        <div class="summary">${incident.summary}</div>

        <div class="footer">
          ${incident.time_window.start} → ${incident.time_window.end}<br/>
          System Action: ${incident.system_action}
        </div>
      `;

      dashboard.appendChild(card);
    });

    const c = document.getElementById("criticalCount");
    const w = document.getElementById("warningCount");
    const s = document.getElementById("safeCount");

    if (c) c.innerText = critical;
    if (w) w.innerText = warning;
    if (s) s.innerText = safe;
  } catch (err) {
    console.error("Dashboard load failed:", err);
  }
}

async function loadTimeline(user) {
  try {
    const res = await fetch(`${API}/timeline/${user}`);
    if (!res.ok) throw new Error("Timeline API failed");

    const events = await res.json();
    const panel = document.getElementById("timeline");

    panel.innerHTML = `<h3>User: ${user}</h3>`;

    let i = 0;
    const interval = setInterval(() => {
      if (i >= events.length) {
        clearInterval(interval);
        return;
      }

      const e = events[i];
      const row = document.createElement("div");

      row.className = "log " + e.action;

      if (
        e.resource &&
        (e.resource.includes("HR") || e.resource.includes("FINANCE"))
      ) {
        row.classList.add("sensitive");
      }

      row.innerText = `${e.timestamp} | ${e.action} | ${e.resource} | ${e.location}`;
      panel.appendChild(row);
      i++;
    }, 80);
  } catch (err) {
    console.error("Timeline load failed:", err);
  }
}

loadReports();
setInterval(loadReports, 3000);
