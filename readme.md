<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ARDA - Autonomous Risk Decision Agent</title>
  
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
      background: linear-gradient(135deg, #0a0e1a 0%, #1a1f35 100%);
      color: #e5e7eb;
      line-height: 1.7;
      padding: 0;
      margin: 0;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 40px 20px;
    }

    /* Header Section */
    .header {
      text-align: center;
      padding: 60px 20px;
      background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
      border-radius: 16px;
      margin-bottom: 50px;
      box-shadow: 0 20px 60px rgba(59, 130, 246, 0.3);
      position: relative;
      overflow: hidden;
    }

    .header::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
      background-size: 50px 50px;
      animation: drift 20s linear infinite;
    }

    @keyframes drift {
      0% { transform: translate(0, 0); }
      100% { transform: translate(50px, 50px); }
    }

    .header-content {
      position: relative;
      z-index: 1;
    }

    h1 {
      font-size: 48px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 15px;
      text-shadow: 0 4px 12px rgba(0,0,0,0.3);
      letter-spacing: -1px;
    }

    .tagline {
      font-size: 20px;
      color: #dbeafe;
      font-weight: 300;
      margin-bottom: 30px;
    }

    .badges {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
      margin-top: 25px;
    }

    .badge {
      display: inline-block;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      transition: all 0.3s ease;
    }

    .badge:hover {
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
    }

    /* Section Styles */
    section {
      background: #111827;
      border-radius: 12px;
      padding: 35px;
      margin-bottom: 30px;
      border: 1px solid #1e293b;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    section:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(59, 130, 246, 0.2);
    }

    h2 {
      font-size: 28px;
      color: #38bdf8;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 2px solid #1e3a8a;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    h2::before {
      content: '▸';
      color: #3b82f6;
      font-size: 32px;
    }

    h3 {
      font-size: 20px;
      color: #60a5fa;
      margin-top: 25px;
      margin-bottom: 12px;
      font-weight: 600;
    }

    p {
      margin: 16px 0;
      color: #d1d5db;
      font-size: 16px;
    }

    ul, ol {
      margin-left: 25px;
      margin-top: 12px;
    }

    li {
      margin: 10px 0;
      color: #d1d5db;
      padding-left: 8px;
    }

    ul li::marker {
      color: #3b82f6;
    }

    /* Info Boxes */
    .info-box {
      padding: 20px;
      border-radius: 10px;
      margin: 24px 0;
      border-left: 5px solid;
      background: rgba(0,0,0,0.3);
      backdrop-filter: blur(10px);
    }

    .info-box.primary {
      border-left-color: #3b82f6;
      background: rgba(59, 130, 246, 0.1);
    }

    .info-box.danger {
      border-left-color: #ef4444;
      background: rgba(239, 68, 68, 0.1);
    }

    .info-box.success {
      border-left-color: #22c55e;
      background: rgba(34, 197, 94, 0.1);
    }

    .info-box.warning {
      border-left-color: #f59e0b;
      background: rgba(245, 158, 11, 0.1);
    }

    .info-box strong {
      color: #ffffff;
      display: block;
      margin-bottom: 8px;
      font-size: 17px;
    }

    /* Code Blocks */
    pre {
      background: #020617;
      padding: 20px;
      border-radius: 10px;
      overflow-x: auto;
      color: #e5e7eb;
      font-family: 'Courier New', Consolas, monospace;
      font-size: 14px;
      border: 1px solid #1e293b;
      line-height: 1.6;
      margin: 20px 0;
    }

    code {
      background: #1e293b;
      padding: 3px 8px;
      border-radius: 4px;
      font-family: 'Courier New', Consolas, monospace;
      font-size: 14px;
      color: #38bdf8;
    }

    /* Architecture Diagram */
    .architecture {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      padding: 30px;
      border-radius: 12px;
      text-align: center;
      font-family: monospace;
      font-size: 15px;
      line-height: 2;
      border: 2px solid #1e3a8a;
      margin: 25px 0;
    }

    .architecture .arrow {
      color: #3b82f6;
      font-size: 20px;
    }

    /* Features Grid */
    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 25px 0;
    }

    .feature-card {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      padding: 25px;
      border-radius: 10px;
      border: 1px solid #1e3a8a;
      transition: all 0.3s ease;
    }

    .feature-card:hover {
      border-color: #3b82f6;
      transform: translateY(-4px);
      box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
    }

    .feature-card h4 {
      color: #38bdf8;
      margin-bottom: 10px;
      font-size: 18px;
      font-weight: 600;
    }

    .feature-card p {
      color: #94a3b8;
      font-size: 14px;
      margin: 0;
    }

    /* Tech Stack */
    .tech-stack {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin: 20px 0;
    }

    .tech-item {
      background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 600;
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.2);
      transition: all 0.3s ease;
    }

    .tech-item:hover {
      transform: scale(1.05);
      box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }

    /* Quick Start */
    .quick-start {
      background: linear-gradient(135deg, #065f46 0%, #059669 100%);
      padding: 30px;
      border-radius: 12px;
      margin: 30px 0;
    }

    .quick-start h3 {
      color: #ffffff;
      margin-top: 0;
    }

    .quick-start pre {
      background: rgba(0,0,0,0.4);
      border: 1px solid rgba(255,255,255,0.2);
    }

    /* Footer */
    footer {
      margin-top: 60px;
      padding: 30px 20px;
      text-align: center;
      border-top: 2px solid #1e293b;
      background: #0a0e1a;
      border-radius: 12px;
    }

    .author-section {
      margin-bottom: 20px;
    }

    .author-section h3 {
      color: #38bdf8;
      margin-bottom: 10px;
    }

    .author-links {
      display: flex;
      gap: 15px;
      justify-content: center;
      margin-top: 15px;
    }

    .author-links a {
      color: #3b82f6;
      text-decoration: none;
      padding: 8px 16px;
      border: 1px solid #3b82f6;
      border-radius: 6px;
      transition: all 0.3s ease;
    }

    .author-links a:hover {
      background: #3b82f6;
      color: #ffffff;
    }

    .copyright {
      color: #64748b;
      font-size: 14px;
      margin-top: 20px;
    }

    /* Responsive */
    @media (max-width: 768px) {
      h1 {
        font-size: 36px;
      }

      .tagline {
        font-size: 18px;
      }

      section {
        padding: 25px;
      }

      h2 {
        font-size: 24px;
      }

      .features-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Scroll Animations */
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(30px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    section {
      animation: fadeInUp 0.6s ease-out;
    }
  </style>
</head>

<body>
  <div class="container">
    
    <!-- Header -->
    <div class="header">
      <div class="header-content">
        <h1>🛡️ ARDA</h1>
        <p class="tagline">Autonomous Risk Decision Agent</p>
        <p style="color: #dbeafe; font-size: 16px; max-width: 800px; margin: 0 auto;">
          A production-style insider threat detection and autonomous response system that simulates real Security Operations Center workflows
        </p>
        <div class="badges">
          <span class="badge">🔒 Security Engineering</span>
          <span class="badge">🐍 Python 3.12</span>
          <span class="badge">⚡ FastAPI</span>
          <span class="badge">🐳 Docker</span>
          <span class="badge">📊 Real-Time Analytics</span>
        </div>
      </div>
    </div>

    <!-- Overview -->
    <section>
      <h2>📋 Overview</h2>
      <p>
        ARDA bridges the gap between academic cybersecurity demos and real-world Security Operations Center (SOC) implementations. 
        While most beginner projects stop at logging events and displaying raw data, ARDA demonstrates enterprise-grade 
        behavioral intelligence, risk scoring, and automated enforcement.
      </p>
      
      <div class="info-box danger">
        <strong>🎯 Core Mission</strong>
        Move beyond raw logs and dashboards into behavioral intelligence, risk scoring, and automated enforcement 
        that mirrors production SOC environments.
      </div>

      <p>
        Real security teams don't analyze isolated events. They track behavior over time, detect privilege escalation patterns, 
        compute risk scores with confidence, and implement explainable automated responses. ARDA does exactly that.
      </p>
    </section>

    <!-- Problem Statement -->
    <section>
      <h2>❌ The Problem</h2>
      <p>Most beginner cybersecurity projects focus on:</p>
      <ul>
        <li>Simple event logging without context</li>
        <li>Raw data visualization without intelligence</li>
        <li>Manual interpretation requiring human analysis</li>
        <li>No automated decision-making capabilities</li>
      </ul>

      <div class="info-box warning">
        <strong>⚠️ Reality Check</strong>
        Real organizations require behavioral analysis, automated threat response, and explainable decision systems 
        that can operate at scale without constant human intervention.
      </div>
    </section>

    <!-- Key Features -->
    <section>
      <h2>✨ Key Features</h2>
      
      <div class="features-grid">
        <div class="feature-card">
          <h4>🎭 Realistic Simulation</h4>
          <p>Generates authentic employee activity logs with normal and anomalous behavior patterns</p>
        </div>
        
        <div class="feature-card">
          <h4>🔍 Threat Detection</h4>
          <p>Identifies abnormal access patterns, privilege misuse, and suspicious activities</p>
        </div>
        
        <div class="feature-card">
          <h4>📊 Risk Scoring</h4>
          <p>Computes behavioral risk scores based on multiple factors and historical patterns</p>
        </div>
        
        <div class="feature-card">
          <h4>🤖 Autonomous Decisions</h4>
          <p>Automatically triggers WARN, RESTRICT, or LOCK actions based on threat levels</p>
        </div>
        
        <div class="feature-card">
          <h4>📝 Incident Reporting</h4>
          <p>Generates structured incident reports with full context and reasoning</p>
        </div>
        
        <div class="feature-card">
          <h4>⏱️ Timeline Replay</h4>
          <p>Provides replayable activity timelines for forensic analysis</p>
        </div>
        
        <div class="feature-card">
          <h4>📄 PDF Export</h4>
          <p>Exports professional incident reports for compliance and documentation</p>
        </div>
        
        <div class="feature-card">
          <h4>🎨 SOC Dashboard</h4>
          <p>Modern, dark-themed dashboard for real-time monitoring and analysis</p>
        </div>
      </div>
    </section>

    <!-- Architecture -->
    <section>
      <h2>🏗️ System Architecture</h2>
      
      <div class="architecture">
        <div>📝 Activity Logs Generation</div>
        <div class="arrow">↓</div>
        <div>🔍 Threat Detection Engine</div>
        <div class="arrow">↓</div>
        <div>📊 Risk Scoring Engine</div>
        <div class="arrow">↓</div>
        <div>🤖 Autonomous Decision Agent</div>
        <div class="arrow">↓</div>
        <div>⚡ Enforcement + Reporting</div>
        <div class="arrow">↓</div>
        <div>🖥️ SOC Dashboard</div>
      </div>

      <div class="info-box primary">
        <strong>🔧 Modular Design</strong>
        Each layer is independently replaceable and scalable, mirroring real enterprise system architecture. 
        This allows for easy integration with existing security infrastructure.
      </div>
    </section>

    <!-- Technology Stack -->
    <section>
      <h2>🛠️ Technology Stack</h2>
      
      <h3>Backend Technologies</h3>
      <div class="tech-stack">
        <span class="tech-item">Python 3.12</span>
        <span class="tech-item">FastAPI</span>
        <span class="tech-item">SQLAlchemy ORM</span>
        <span class="tech-item">SQLite</span>
        <span class="tech-item">Pydantic</span>
      </div>

      <h3>Frontend Technologies</h3>
      <div class="tech-stack">
        <span class="tech-item">HTML5</span>
        <span class="tech-item">CSS3</span>
        <span class="tech-item">Vanilla JavaScript</span>
        <span class="tech-item">Responsive Design</span>
      </div>

      <h3>Infrastructure & DevOps</h3>
      <div class="tech-stack">
        <span class="tech-item">Docker</span>
        <span class="tech-item">Docker Compose</span>
        <span class="tech-item">Nginx</span>
        <span class="tech-item">RESTful API</span>
      </div>
    </section>

    <!-- Repository Structure -->
    <section>
      <h2>📁 Repository Structure</h2>
      
      <pre>
ARDA/
├── 🐍 app.py              # FastAPI entry point & API endpoints
├── 🤖 agent.py            # Autonomous decision logic & enforcement
├── 🔍 detector.py         # Threat detection engine & pattern analysis
├── 📝 reporter.py         # Incident report builder & formatter
├── 📄 exporter.py         # PDF export functionality
├── 💾 models.py           # SQLAlchemy database models
├── 🌱 seed.py             # Activity log generator & simulator
│
├── 🎨 ui/
│   ├── index.html         # SOC dashboard interface
│   ├── script.js          # Frontend logic & API integration
│   ├── style.css          # Dashboard styling
│   ├── nginx.conf         # Nginx configuration
│   └── Dockerfile         # Frontend container definition
│
├── 🐳 docker-compose.yml  # Multi-container orchestration
├── 📚 requirements.txt    # Python dependencies
└── 📖 README.html         # Project documentation
      </pre>
    </section>

    <!-- Quick Start -->
    <section>
      <h2>🚀 Quick Start</h2>
      
      <div class="quick-start">
        <h3>Installation & Setup</h3>
        <pre>
# Clone the repository
git clone https://github.com/Adi3182004/Autonomous-Risk-Decision-Agent-ARDA-.git

# Navigate to project directory
cd Autonomous-Risk-Decision-Agent-ARDA-

# Build Docker containers (no cache for fresh build)
docker compose build --no-cache

# Start all services
docker compose up
        </pre>
      </div>

      <div class="info-box success">
        <strong>🌐 Access Points</strong>
        <ul style="margin: 10px 0 0 0;">
          <li><strong>SOC Dashboard:</strong> <code>http://localhost:8080</code></li>
          <li><strong>API Documentation:</strong> <code>http://localhost:8000/docs</code></li>
          <li><strong>Alternative API Docs:</strong> <code>http://localhost:8000/redoc</code></li>
        </ul>
      </div>
    </section>

    <!-- API Endpoints -->
    <section>
      <h2>🔌 API Endpoints</h2>
      
      <h3>Core Endpoints</h3>
      <ul>
        <li><code>GET /report</code> - Retrieve comprehensive incident analysis report</li>
        <li><code>GET /timeline/{employee_id}</code> - Get activity timeline for specific employee</li>
        <li><code>GET /incidents</code> - List all detected security incidents</li>
        <li><code>GET /risk-scores</code> - View current risk scores for all employees</li>
        <li><code>POST /analyze</code> - Trigger manual analysis of recent activities</li>
      </ul>

      <div class="info-box primary">
        <strong>📖 Interactive Documentation</strong>
        Visit <code>/docs</code> for Swagger UI with live API testing capabilities and full endpoint documentation.
      </div>
    </section>

    <!-- Demo Flow -->
    <section>
      <h2>🎬 Demo Flow (Recruiter Guide)</h2>
      
      <p>Perfect for showcasing technical capabilities in interviews:</p>
      
      <ol>
        <li><strong>API Demonstration</strong> - Show JSON endpoints (<code>/report</code>, <code>/timeline</code>) with live data</li>
        <li><strong>Risk Analysis</strong> - Explain the risk scoring algorithm and decision logic</li>
        <li><strong>Dashboard Tour</strong> - Navigate the SOC dashboard and demonstrate real-time monitoring</li>
        <li><strong>Timeline Replay</strong> - Show activity replay for a high-risk employee</li>
        <li><strong>Incident Export</strong> - Generate and download a PDF incident report</li>
        <li><strong>Autonomous Response</strong> - Explain the automated enforcement reasoning process</li>
      </ol>

      <div class="info-box success">
        <strong>⏱️ Time-Efficient</strong>
        This complete demonstration showcases backend engineering, system design, security thinking, 
        and UI development in under 5 minutes.
      </div>
    </section>

    <!-- Decision Logic -->
    <section>
      <h2>🧠 Decision Logic</h2>
      
      <h3>Risk Classification</h3>
      <ul>
        <li><strong>Critical (Risk ≥ 70):</strong> Immediate account lock + incident report</li>
        <li><strong>Warning (40 ≤ Risk < 70):</strong> Access restrictions + monitoring escalation</li>
        <li><strong>Safe (Risk < 40):</strong> Normal operation + continued observation</li>
      </ul>

      <h3>Risk Factors</h3>
      <ul>
        <li>After-hours access patterns</li>
        <li>Failed authentication attempts</li>
        <li>Privilege escalation activities</li>
        <li>Access to sensitive resources</li>
        <li>Unusual geographic locations</li>
        <li>Rapid successive actions (potential automation)</li>
      </ul>

      <div class="info-box warning">
        <strong>🎯 Explainability First</strong>
        All decisions include detailed reasoning to ensure transparency and auditability, 
        critical for compliance and human oversight.
      </div>
    </section>

    <!-- Real-World Extensions -->
    <section>
      <h2>🌍 Production-Ready Extensions</h2>
      
      <p>ARDA's modular architecture enables straightforward enterprise integration:</p>
      
      <h3>Database & Persistence</h3>
      <ul>
        <li>Replace SQLite with PostgreSQL or MySQL for production scale</li>
        <li>Implement TimescaleDB for time-series log optimization</li>
        <li>Add Redis for caching and real-time analytics</li>
      </ul>

      <h3>Integration Capabilities</h3>
      <ul>
        <li>Connect to SIEM platforms (Splunk, ELK Stack, QRadar)</li>
        <li>Integrate with IAM systems (Okta, Active Directory, Azure AD)</li>
        <li>Link to ticketing systems (Jira, ServiceNow)</li>
      </ul>

      <h3>Alerting & Notifications</h3>
      <ul>
        <li>Slack/Teams integration for real-time alerts</li>
        <li>Email notifications for critical incidents</li>
        <li>PagerDuty integration for on-call escalation</li>
        <li>Webhook support for custom integrations</li>
      </ul>

      <h3>Advanced Analytics</h3>
      <ul>
        <li>Machine learning-based anomaly detection</li>
        <li>User behavior analytics (UBA)</li>
        <li>Peer group analysis for baseline comparison</li>
        <li>Predictive threat modeling</li>
      </ul>
    </section>

    <!-- Design Decisions -->
    <section>
      <h2>🎯 Intentional Design Decisions</h2>
      
      <div class="info-box primary">
        <strong>Why These Limitations Exist</strong>
      </div>

      <h3>Simulation-Focused</h3>
      <ul>
        <li><strong>No actual user blocking:</strong> Safe demonstration without production impact</li>
        <li><strong>Synthetic data generation:</strong> Reproducible scenarios for testing</li>
      </ul>

      <h3>Security & Authentication</h3>
      <ul>
        <li><strong>No authentication layer:</strong> Simplified setup for demonstration purposes</li>
        <li><strong>Local-only deployment:</strong> No exposure to security risks during development</li>
      </ul>

      <h3>Explainability Over Complexity</h3>
      <ul>
        <li><strong>Rule-based logic:</strong> Clear, auditable decision-making process</li>
        <li><strong>Transparent scoring:</strong> Every decision is explainable to stakeholders</li>
        <li><strong>No ML black boxes:</strong> Prioritizes understanding over complexity</li>
      </ul>

      <div class="info-box success">
        <strong>💡 Philosophy</strong>
        ARDA demonstrates production-ready thinking while maintaining simplicity for educational 
        and demonstrative purposes. Every limitation is intentional and documented.
      </div>
    </section>

    <!-- Use Cases -->
    <section>
      <h2>💼 Use Cases</h2>
      
      <div class="features-grid">
        <div class="feature-card">
          <h4>🎓 Educational</h4>
          <p>Learn enterprise security patterns, SOC workflows, and automated threat response systems</p>
        </div>
        
        <div class="feature-card">
          <h4>📊 Portfolio Project</h4>
          <p>Demonstrate full-stack security engineering capabilities to potential employers</p>
        </div>
        
        <div class="feature-card">
          <h4>🔬 Research Platform</h4>
          <p>Test new detection algorithms and response strategies in a controlled environment</p>
        </div>
        
        <div class="feature-card">
          <h4>🏢 POC Foundation</h4>
          <p>Starting point for enterprise proof-of-concept implementations</p>
        </div>
      </div>
    </section>

    <!-- Contributing -->
    <section>
      <h2>🤝 Contributing</h2>
      
      <p>Contributions are welcome! Here's how you can help improve ARDA:</p>
      
      <ul>
        <li>🐛 <strong>Report bugs</strong> - Open an issue with detailed reproduction steps</li>
        <li>💡 <strong>Suggest features</strong> - Share your ideas for new capabilities</li>
        <li>📝 <strong>Improve documentation</strong> - Help make ARDA more accessible</li>
        <li>🔧 <strong>Submit pull requests</strong> - Add new features or fix issues</li>
      </ul>

      <div class="info-box primary">
        <strong>📋 Before Contributing</strong>
        Please ensure your code follows the existing style, includes appropriate tests, 
        and updates documentation as needed.
      </div>
    </section>

    <!-- License -->
    <section>
      <h2>📜 License</h2>
      <p>
        This project is open source and available under the MIT License. 
        Feel free to use, modify, and distribute as needed while maintaining attribution.
      </p>
    </section>

    <!-- Footer -->
    <footer>
      <div class="author-section">
        <h3>👨‍💻 Author</h3>
        <p style="color: #e5e7eb; font-size: 18px; margin: 10px 0;"><strong>Aditya Andhalkar</strong></p>
        <p style="color: #94a3b8; margin: 5px 0;">Backend & Security Engineering</p>
        <p style="color: #94a3b8; margin: 5px 0;">Builder of Production-Style Systems</p>
        
        <div class="author-links">
          <a href="https://github.com/Adi3182004" target="_blank">🐙 GitHub</a>
          <a href="https://github.com/Adi3182004/Autonomous-Risk-Decision-Agent-ARDA-" target="_blank">⭐ Star This Project</a>
        </div>
      </div>

      <div class="copyright">
        <p>© 2025 ARDA - Autonomous Risk Decision Agent | Project 07</p>
        <p style="margin-top: 10px;">Built with 💙 for the Security Engineering Community</p>
      </div>
    </footer>

  </div>
</body>
</html>
