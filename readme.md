<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <title>ARDA - Autonomous Risk Decision Agent</title>

  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      background: #0b0f19;
      color: #e5e7eb;
      line-height: 1.7;
      padding: 40px;
      max-width: 1150px;
      margin: auto;
    }

    h1, h2, h3 {
      color: #38bdf8;
      margin-top: 40px;
    }

    h1 {
      font-size: 34px;
      margin-bottom: 10px;
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
      margin: 14px 0;
      color: #e5e7eb;
    }

    ul {
      margin-left: 22px;
    }

    li {
      margin: 8px 0;
    }

    pre {
      background: #020617;
      padding: 16px;
      border-radius: 8px;
      overflow-x: auto;
      color: #e5e7eb;
      font-family: Consolas, monospace;
      font-size: 14px;
    }

    .box {
      background: #111827;
      border-left: 5px solid #38bdf8;
      padding: 16px;
      margin: 24px 0;
      border-radius: 6px;
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
      margin-top: 70px;
      padding-top: 20px;
      border-top: 1px solid #1e293b;
      font-size: 14px;
      color: #94a3b8;
      text-align: center;
    }

    .badge {
      display: inline-block;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 13px;
      margin-right: 8px;
      background: #020617;
      border: 1px solid #1e293b;
    }
  </style>
</head>

<body>

<h1>ARDA - Autonomous Risk Decision Agent</h1>

<p>
<span class="badge">Project 07</span>
<span class="badge">Real-World Python Series</span>
<span class="badge">Security Engineering</span>
</p>

<p>
ARDA is a <strong>production-style insider threat detection and autonomous response system</strong>
that simulates how real Security Operations Centers (SOC) detect, analyze, and respond
to risky employee behavior.
</p>

<div class="box danger">
<strong>Core Idea:</strong><br/>
Move beyond raw logs and dashboards into <strong>behavioral intelligence, risk scoring,
and automated enforcement</strong>.
</div>

<h2>Problem Statement</h2>

<p>
Most beginner cybersecurity projects stop at:
</p>

<ul>
  <li>Logging events</li>
  <li>Displaying raw data</li>
  <li>Manual interpretation</li>
</ul>

<p>
<strong>Real organizations do not work this way.</strong>
</p>

<p>
Security teams care about:
</p>

<ul>
  <li>Behavior over time (not isolated events)</li>
  <li>Privilege escalation patterns</li>
  <li>Risk scoring with confidence</li>
  <li>Explainable, automated response</li>
</ul>

<div class="box note">
ARDA was built to close the gap between academic demos and real SOC workflows.
</div>

<h2>What ARDA Does</h2>

<ul>
  <li>Simulates realistic employee activity logs</li>
  <li>Detects abnormal access and privilege misuse</li>
  <li>Computes behavioral risk scores</li>
  <li>Classifies incidents (Critical, Warning, Safe)</li>
  <li>Triggers autonomous decisions:
    <ul>
      <li>WARN</li>
      <li>RESTRICT</li>
      <li>LOCK</li>
    </ul>
  </li>
  <li>Generates structured incident reports</li>
  <li>Provides replayable activity timelines</li>
  <li>Exports incidents as PDF reports</li>
</ul>

<h2>High-Level Architecture</h2>

<pre>
Activity Logs
   ↓
Threat Detection Engine
   ↓
Risk Scoring Engine
   ↓
Autonomous Decision Agent
   ↓
Enforcement + Reporting
   ↓
SOC Dashboard
</pre>

<div class="box note">
Each layer is modular and replaceable, mirroring real enterprise system design.
</div>

<h2>Technology Stack</h2>

<h3>Backend</h3>
<ul>
  <li>Python 3.12</li>
  <li>FastAPI (high-performance APIs)</li>
  <li>SQLAlchemy ORM</li>
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

<h2>Repository Structure</h2>

<pre>
ARDA/
├── app.py              FastAPI entry point
├── agent.py            Autonomous decision logic
├── detector.py         Threat detection engine
├── reporter.py         Incident builder
├── exporter.py         PDF export
├── models.py           Database models
├── seed.py             Log generator
│
├── ui/
│   ├── index.html      SOC dashboard
│   ├── script.js
│   ├── style.css
│   ├── nginx.conf
│   └── Dockerfile
│
├── docker-compose.yml
└── README.html
</pre>

<h2>How to Run the Project</h2>

<pre>
git clone https://github.com/Adi3182004/Autonomous-Risk-Decision-Agent-ARDA-.git
cd Autonomous-Risk-Decision-Agent-ARDA-
docker compose build --no-cache
docker compose up
</pre>

<ul>
  <li>Dashboard: http://localhost:8080</li>
  <li>API Docs: http://localhost:8000/docs</li>
</ul>

<h2>Demo Flow (Recruiter Friendly)</h2>

<ol>
  <li>Show API JSON endpoints (/report, /timeline)</li>
  <li>Explain risk scoring and decision logic</li>
  <li>Open dashboard and replay user timeline</li>
  <li>Export incident PDF</li>
  <li>Explain autonomous enforcement reasoning</li>
</ol>

<div class="box success">
This demonstrates backend engineering, system design, security thinking,
and UI in under three minutes.
</div>

<h2>Real-World Extensions</h2>

<ul>
  <li>Replace SQLite with PostgreSQL</li>
  <li>Integrate SIEM log ingestion</li>
  <li>Connect IAM or Active Directory</li>
  <li>Send alerts via Slack or Email</li>
  <li>Introduce ML-based scoring if required</li>
</ul>

<h2>Intentional Limitations</h2>

<ul>
  <li>No real user blocking (simulation only)</li>
  <li>No authentication layer</li>
  <li>Rule-based logic for explainability</li>
</ul>

<h2>Author</h2>

<p>
<strong>Aditya Andhalkar</strong><br/>
Backend and Security Engineering<br/>
Builder of production-style systems
</p>

<footer>
ARDA - Autonomous Risk Decision Agent | Project 07
</footer>

</body>
</html>
