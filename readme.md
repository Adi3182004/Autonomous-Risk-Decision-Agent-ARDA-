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

    h1 { font-size: 32px; }
    h2 {
      font-size: 24px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 6px;
    }
    h3 { font-size: 18px; }

    p { margin: 12px 0; }

    ul { margin-left: 20px; }
    li { margin: 6px 0; }

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

    .danger { border-left-color: #ef4444; }
    .success { border-left-color: #22c55e; }
    .note { border-left-color: #f59e0b; }

    footer {
      margin-top: 60px;
      font-size: 14px;
      color: #94a3b8;
      text-align: center;
    }
  </style>
</head>

<body>

<h1>ARDA - Autonomous Risk Decision Agent</h1>
<p><strong>Project 07 - Real-World Python Series</strong></p>

<p>
ARDA is a <strong>production-style insider threat detection and autonomous response system</strong>
designed to simulate how real Security Operations Centers (SOC) detect, analyze,
and respond to risky employee behavior.
</p>

<div class="box danger">
<strong>Core idea:</strong> Move beyond logs and dashboards into
<strong>behavioral intelligence and automated enforcement</strong>.
</div>

<h2>Problem Statement</h2>

<p>
Most beginner security projects stop at logging events or visualizing data.
Real organizations do not.
</p>

<ul>
  <li>Behavior over time</li>
  <li>Privilege escalation detection</li>
  <li>Risk scoring with confidence</li>
  <li>Fast, explainable automated response</li>
</ul>

<h2>What ARDA Does</h2>

<ul>
  <li>Simulates employee activity logs</li>
  <li>Detects abnormal access patterns</li>
  <li>Calculates behavioral risk scores</li>
  <li>Classifies incidents</li>
  <li>Triggers actions: WARN, RESTRICT, LOCK</li>
  <li>Generates reports and timeline replay</li>
  <li>Exports incidents as PDF</li>
</ul>

<h2>High-Level Architecture</h2>

<pre>
Activity Logs
   ↓
Detection Engine
   ↓
Risk Scoring
   ↓
Decision Agent
   ↓
Enforcement + Reporting
   ↓
SOC Dashboard
</pre>

<h2>Technology Stack</h2>

<h3>Backend</h3>
<ul>
  <li>Python 3.12</li>
  <li>FastAPI</li>
  <li>SQLAlchemy</li>
  <li>SQLite</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>HTML, CSS (Dark SOC theme)</li>
  <li>Vanilla JavaScript</li>
</ul>

<h3>Infrastructure</h3>
<ul>
  <li>Docker</li>
  <li>Docker Compose</li>
  <li>Nginx</li>
</ul>

<h2>How to Run</h2>

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

<h2>Author</h2>

<p>
<strong>Aditya Andhalkar</strong><br />
Backend and Security Engineering<br />
Production-style system builder
</p>

<footer>
ARDA - Autonomous Risk Decision Agent | Project 07
</footer>

</body>
</html>
