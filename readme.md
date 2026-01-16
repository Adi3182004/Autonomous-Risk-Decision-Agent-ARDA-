<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>ARDA - Autonomous Risk Decision Agent</title>

  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      background: #0b0f19;
      color: #e5e7eb;
      line-height: 1.65;
      padding: 40px;
      max-width: 1100px;
      margin: auto;
    }

    h1, h2, h3 {
      color: #38bdf8;
      margin-top: 40px;
    }

    h1 {
      font-size: 32px;
    }

    h2 {
      font-size: 24px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 6px;
    }

    h3 {
      font-size: 18px;
    }

    p {
      margin: 12px 0;
    }

    ul {
      margin-left: 20px;
    }

    li {
      margin: 6px 0;
    }

    pre, code {
      background: #020617;
      color: #e5e7eb;
      padding: 14px;
      border-radius: 6px;
      overflow-x: auto;
      font-family: Consolas, monospace;
    }

    .box {
      background: #111827;
      border-left: 4px solid #38bdf8;
      padding: 14px;
      margin: 20px 0;
    }

    .danger {
      border-left-color: #ef4444;
    }

    .success {
      border-left-color: #22c55e;
    }

    .note {
      border-left-color: #f59e0b;
    }

    footer {
      margin-top: 60px;
      font-size: 14px;
      color: #94a3b8;
      text-align: center;
    }
  </style>
</head>

<body>

<h1>🛡️ ARDA – Autonomous Risk Decision Agent</h1>
<p><strong>Project 07 – Real-World Python Series</strong></p>

<p>
ARDA is a <strong>production-style insider threat detection and autonomous response system</strong>
designed to simulate how real Security Operations Centers (SOC) detect, analyze,
and respond to risky employee behavior.
</p>

<div class="box danger">
<strong>Core idea:</strong> Move beyond logs and dashboards into
<strong>behavioral intelligence and automated enforcement</strong>.
</div>

<h2>❗ Problem Statement</h2>

<p>
Most beginner security projects stop at logging events or visualizing data.
Real organizations don’t.
</p>

<p>
Security teams care about:
</p>

<ul>
  <li>Behavior over time (not isolated events)</li>
  <li>Privilege escalation detection</li>
  <li>Risk scoring and confidence levels</li>
  <li>Fast, explainable automated response</li>
</ul>

<p>
ARDA was built to close this gap.
</p>

<h2>🔍 What ARDA Does</h2>

<ul>
  <li>Simulates realistic employee activity logs</li>
  <li>Detects abnormal access and privilege misuse</li>
  <li>Calculates behavioral risk scores</li>
  <li>Classifies incidents (Critical / Warning / Safe)</li>
  <li>Triggers autonomous actions:
    <ul>
      <li>WARN</li>
      <li>RESTRICT</li>
      <li>LOCK</li>
    </ul>
  </li>
  <li>Generates structured incident reports</li>
  <li>Replays activity timelines visually</li>
  <li>Exports incidents as PDF reports</li>
</ul>

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

<div class="box note">
Each component is modular and replaceable — mirroring real enterprise systems.
</div>

<h2>🧠 Technology Stack</h2>

<h3>Backend</h3>
<ul>
  <li>Python 3.12</li>
  <li>FastAPI</li>
  <li>SQLAlchemy</li>
  <li>SQLite (simulation)</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>HTML, CSS (Dark SOC theme)</li>
  <li>Vanilla JavaScript</li>
  <li>Animated timeline replay</li>
</ul>

<h3>Infrastructure</h3>
<ul>
  <li>Docker</li>
  <li>Docker Compose</li>
  <li>Nginx reverse proxy</li>
</ul>

<h2>📁 Repository Structure</h2>

<pre>
ARDA/
├── app.py              # FastAPI entry point
├── agent.py            # Autonomous decision logic
├── detector.py         # Threat detection
├── reporter.py         # Incident builder
├── exporter.py         # PDF export
├── models.py           # Database models
├── seed.py             # Log generator
│
├── ui/
│   ├── index.html      # SOC dashboard
│   ├── script.js
│   ├── style.css
│   ├── nginx.conf
│   └── Dockerfile
│
├── docker-compose.yml
└── README.html
</pre>

<h2>🚀 How to Run</h2>

<pre>
git clone https://github.com/Adi3182004/Autonomous-Risk-Decision-Agent-ARDA-.git
cd Autonomous-Risk-Decision-Agent-ARDA-
docker compose build --no-cache
docker compose up
</pre>

<ul>
  <li>SOC Dashboard → http://localhost:8080</li>
  <li>API Docs → http://localhost:8000/docs</li>
</ul>

<h2>🧪 Demo Flow (Recruiter-Friendly)</h2>

<ol>
  <li>Show API JSON (/report, /timeline)</li>
  <li>Explain risk score and decision logic</li>
  <li>Open dashboard and replay timeline</li>
  <li>Export PDF report</li>
  <li>Explain autonomous enforcement</li>
</ol>

<div class="box success">
This demonstrates backend engineering, system design, security thinking,
and UI — in under 3 minutes.
</div>

<h2>🏢 Real-World Extensions</h2>

<ul>
  <li>PostgreSQL instead of SQLite</li>
  <li>SIEM log ingestion</li>
  <li>IAM / Active Directory integration</li>
  <li>Slack / Email alerts</li>
  <li>ML-based scoring (optional)</li>
</ul>

<h2>⚠️ Intentional Limitations</h2>

<ul>
  <li>No real user blocking (simulation only)</li>
  <li>No authentication layer</li>
  <li>Rule-based logic for explainability</li>
</ul>

<h2>👨‍💻 Author</h2>

<p>
<strong>Aditya Andhalkar</strong><br />
Backend & Security-focused Engineer<br />
Building real-world, production-style systems
</p>

<footer>
ARDA – Autonomous Risk Decision Agent • Project 07
</footer>

</body>
</html>
