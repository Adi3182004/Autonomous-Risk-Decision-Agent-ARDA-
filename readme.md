<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>ARDA – Autonomous Risk Decision Agent</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.6;
      background: #0b0f19;
      color: #e5e7eb;
      padding: 40px;
    }
    h1, h2, h3 {
      color: #38bdf8;
    }
    code, pre {
      background: #020617;
      color: #e5e7eb;
      padding: 12px;
      display: block;
      border-radius: 6px;
      overflow-x: auto;
    }
    ul {
      margin-left: 20px;
    }
    .note {
      background: #111827;
      border-left: 4px solid #f59e0b;
      padding: 12px;
      margin: 20px 0;
    }
    .danger {
      background: #111827;
      border-left: 4px solid #ef4444;
      padding: 12px;
      margin: 20px 0;
    }
    .success {
      background: #111827;
      border-left: 4px solid #22c55e;
      padding: 12px;
      margin: 20px 0;
    }
  </style>
</head>
<body>

<h1>🛡️ ARDA – Autonomous Risk Decision Agent</h1>
<p><strong>Project 07 – Real-World Python Series</strong></p>

<p>
ARDA is a <strong>production-style insider threat detection and automated response system</strong>  
designed to simulate how real Security Operations Centers (SOC) detect, analyze, and respond to risky employee behavior.
</p>

<hr />

<h2>❗ Problem Statement (Why This Exists)</h2>

<p>
Most academic or beginner security projects stop at:
</p>

<ul>
  <li>Logging events</li>
  <li>Displaying raw data</li>
  <li>No real decision-making</li>
</ul>

<p>
<strong>Real companies don’t work like that.</strong>
</p>

<p>
Security teams care about:
</p>

<ul>
  <li>Behavior over time (not single events)</li>
  <li>Privilege misuse</li>
  <li>Risk scoring</li>
  <li>Automated enforcement</li>
</ul>

<div class="danger">
ARDA was built to close this gap — moving from <strong>logs → intelligence → decisions → enforcement</strong>.
</div>

<hr />

<h2>🔍 What ARDA Actually Does</h2>

<ul>
  <li>Generates realistic employee activity logs</li>
  <li>Detects abnormal behavior patterns</li>
  <li>Scores user risk dynamically</li>
  <li>Classifies incidents (Critical / Warning / Safe)</li>
  <li>Triggers autonomous actions:
    <ul>
      <li>WARN</li>
      <li>RESTRICT</li>
      <li>LOCK</li>
    </ul>
  </li>
  <li>Produces incident reports</li>
  <li>Replays user timelines visually</li>
  <li>Exports incident reports as PDF</li>
</ul>

<hr />

<h2>🏗️ High-Level Architecture</h2>

<pre>
[ Activity Logs ]
        ↓
[ Detection Engine ]
        ↓
[ Risk Scoring Engine ]
        ↓
[ Decision Agent ]
        ↓
[ Enforcement + Reporting ]
        ↓
[ SOC Dashboard ]
</pre>

<p>
Each layer is modular and replaceable — exactly how enterprise systems are designed.
</p>

<hr />

<h2>🧠 Tech Stack</h2>

<h3>Backend</h3>
<ul>
  <li>Python 3.12</li>
  <li>FastAPI</li>
  <li>SQLAlchemy</li>
  <li>SQLite (local simulation)</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>HTML + CSS (Dark SOC theme)</li>
  <li>Vanilla JavaScript</li>
  <li>Animated timeline replay</li>
</ul>

<h3>Infrastructure</h3>
<ul>
  <li>Docker</li>
  <li>Docker Compose</li>
  <li>Nginx reverse proxy</li>
</ul>

<hr />

<h2>📁 Repository Structure</h2>

<pre>
ARDA/
│
├── app.py                → FastAPI entry point
├── agent.py              → Autonomous decision logic
├── detector.py           → Threat detection engine
├── reporter.py           → Incident construction
├── exporter.py           → PDF report generator
├── models.py             → Database models
├── database.py           → DB connection
├── seed.py               → Log generation
├── reset_db.py           → DB reset utility
│
├── ui/
│   ├── index.html        → SOC dashboard
│   ├── style.css
│   ├── script.js
│   ├── nginx.conf
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
└── README.html
</pre>

<hr />

<h2>🚀 How to Run (Step-by-Step)</h2>

<h3>1️⃣ Prerequisites</h3>
<ul>
  <li>Docker Desktop (running)</li>
  <li>Docker Compose</li>
</ul>

<h3>2️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/Adi3182004/Autonomous-Risk-Decision-Agent-ARDA-.git
cd Autonomous-Risk-Decision-Agent-ARDA-
</pre>

<h3>3️⃣ Build & Start the System</h3>
<pre>
docker compose build --no-cache
docker compose up
</pre>

<div class="note">
First startup seeds the database with simulated employee activity.
</div>

<h3>4️⃣ Access the System</h3>
<ul>
  <li>SOC Dashboard: <strong>http://localhost:8080</strong></li>
  <li>API Docs: <strong>http://localhost:8000/docs</strong></li>
</ul>

<hr />

<h2>🧪 How to Demo This Project (Recruiter-Ready)</h2>

<h3>Recommended Demo Flow</h3>

<ol>
  <li>Open API Docs → show /alerts & /report JSON</li>
  <li>Explain risk scores and decisions</li>
  <li>Open Dashboard → click incidents</li>
  <li>Replay timeline animation</li>
  <li>Export incident PDF</li>
  <li>Explain autonomous enforcement logic</li>
</ol>

<div class="success">
This flow demonstrates backend logic, system design, UI, and security thinking in under 3 minutes.
</div>

<hr />

<h2>🏢 How This Can Be Used in a Real Company</h2>

<ul>
  <li>Replace SQLite with PostgreSQL</li>
  <li>Stream logs from SIEM tools</li>
  <li>Integrate IAM / Active Directory</li>
  <li>Connect to Slack / Email for alerts</li>
  <li>Replace rule engine with ML models</li>
</ul>

<p>
ARDA is intentionally <strong>rule-based first</strong> — because companies demand explainability before ML.
</p>

<hr />

<h2>⚠️ Limitations (Intentional)</h2>

<ul>
  <li>No real user blocking (simulation only)</li>
  <li>No authentication layer (demo focus)</li>
  <li>No ML — deterministic decisions by design</li>
</ul>

<div class="note">
These are conscious trade-offs to keep the system inspectable and demo-friendly.
</div>

<hr />

<h2>👨‍💻 Author</h2>

<p>
<strong>Aditya Andhalkar</strong><br />
Builder of real-world, production-style systems.<br />
Focused on backend engineering, security automation, and applied AI.
</p>

<hr />

<h2>📜 License</h2>
<p>Open-source for learning, experimentation, and portfolio use.</p>

</body>
</html>
