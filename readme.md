# 🛡️ ARDA - Autonomous Risk Decision Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Security](https://img.shields.io/badge/Security-Engineering-red?style=for-the-badge)

**A production-style insider threat detection and autonomous response system**

[Features](#-key-features) • [Quick Start](#-quick-start) • [Architecture](#️-system-architecture) • [API Docs](#-api-endpoints) • [Demo](#-demo-flow)

</div>

---

## 📋 Overview

ARDA bridges the gap between academic cybersecurity demos and **real-world Security Operations Center (SOC)** implementations. While most beginner projects stop at logging events and displaying raw data, ARDA demonstrates enterprise-grade behavioral intelligence, risk scoring, and automated enforcement.

### 🎯 Core Mission

> **Move beyond raw logs and dashboards into behavioral intelligence, risk scoring, and automated enforcement that mirrors production SOC environments.**

Real security teams don't analyze isolated events. They:
- Track **behavior over time**, not isolated incidents
- Detect **privilege escalation patterns**
- Compute **risk scores** with confidence
- Implement **explainable automated responses**

ARDA does exactly that.

---

## ❌ The Problem

Most beginner cybersecurity projects focus on:

- ❌ Simple event logging without context
- ❌ Raw data visualization without intelligence
- ❌ Manual interpretation requiring human analysis
- ❌ No automated decision-making capabilities

### ⚠️ Reality Check

**Real organizations require:**
- ✅ Behavioral analysis over time
- ✅ Automated threat response
- ✅ Explainable decision systems
- ✅ Scalable operations without constant human intervention

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🎭 Realistic Simulation
Generates authentic employee activity logs with normal and anomalous behavior patterns

### 🔍 Threat Detection
Identifies abnormal access patterns, privilege misuse, and suspicious activities

### 📊 Risk Scoring
Computes behavioral risk scores based on multiple factors and historical patterns

### 🤖 Autonomous Decisions
Automatically triggers **WARN**, **RESTRICT**, or **LOCK** actions based on threat levels

</td>
<td width="50%">

### 📝 Incident Reporting
Generates structured incident reports with full context and reasoning

### ⏱️ Timeline Replay
Provides replayable activity timelines for forensic analysis

### 📄 PDF Export
Exports professional incident reports for compliance and documentation

### 🎨 SOC Dashboard
Modern, dark-themed dashboard for real-time monitoring and analysis

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
┌─────────────────────────────┐
│  📝 Activity Logs Generation │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│  🔍 Threat Detection Engine  │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│   📊 Risk Scoring Engine     │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ 🤖 Autonomous Decision Agent │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│  ⚡ Enforcement + Reporting   │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│      🖥️ SOC Dashboard        │
└─────────────────────────────┘
```

> **🔧 Modular Design:** Each layer is independently replaceable and scalable, mirroring real enterprise system architecture.

---

## 🛠️ Technology Stack

### Backend
- **Python 3.12** - Core programming language
- **FastAPI** - High-performance API framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Local simulation database
- **Pydantic** - Data validation

### Frontend
- **HTML5 / CSS3** - Modern web standards
- **Vanilla JavaScript** - No framework dependencies
- **Responsive Design** - Mobile-friendly interface

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Reverse proxy and web server

---

## 📁 Repository Structure

```
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
└── 📖 README.md           # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose installed
- Git installed

### Installation

```bash
# Clone the repository
git clone https://github.com/Adi3182004/Autonomous-Risk-Decision-Agent-ARDA-.git

# Navigate to project directory
cd Autonomous-Risk-Decision-Agent-ARDA-

# Build Docker containers (no cache for fresh build)
docker compose build --no-cache

# Start all services
docker compose up
```

### 🌐 Access Points

| Service | URL | Description |
|---------|-----|-------------|
| **SOC Dashboard** | `http://localhost:8080` | Main monitoring interface |
| **API Documentation** | `http://localhost:8000/docs` | Swagger UI |
| **Alternative API Docs** | `http://localhost:8000/redoc` | ReDoc interface |

---

## 🔌 API Endpoints

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/report` | Retrieve comprehensive incident analysis report |
| `GET` | `/timeline/{employee_id}` | Get activity timeline for specific employee |
| `GET` | `/incidents` | List all detected security incidents |
| `GET` | `/risk-scores` | View current risk scores for all employees |
| `POST` | `/analyze` | Trigger manual analysis of recent activities |

> **📖 Interactive Documentation:** Visit `/docs` for Swagger UI with live API testing capabilities and full endpoint documentation.

---

## 🎬 Demo Flow (Recruiter Guide)

Perfect for showcasing technical capabilities in interviews:

1. **🔗 API Demonstration** - Show JSON endpoints (`/report`, `/timeline`) with live data
2. **📊 Risk Analysis** - Explain the risk scoring algorithm and decision logic
3. **🖥️ Dashboard Tour** - Navigate the SOC dashboard and demonstrate real-time monitoring
4. **⏱️ Timeline Replay** - Show activity replay for a high-risk employee
5. **📄 Incident Export** - Generate and download a PDF incident report
6. **🤖 Autonomous Response** - Explain the automated enforcement reasoning process

> **⏱️ Time-Efficient:** This complete demonstration showcases backend engineering, system design, security thinking, and UI development in **under 5 minutes**.

---

## 🧠 Decision Logic

### Risk Classification

| Risk Level | Score Range | Automated Action |
|------------|-------------|------------------|
| **🔴 Critical** | Risk ≥ 70 | Immediate account lock + incident report |
| **🟡 Warning** | 40 ≤ Risk < 70 | Access restrictions + monitoring escalation |
| **🟢 Safe** | Risk < 40 | Normal operation + continued observation |

### Risk Factors

- ⏰ After-hours access patterns
- 🚫 Failed authentication attempts
- ⬆️ Privilege escalation activities
- 🔐 Access to sensitive resources
- 🌍 Unusual geographic locations
- ⚡ Rapid successive actions (potential automation)

> **🎯 Explainability First:** All decisions include detailed reasoning to ensure transparency and auditability, critical for compliance and human oversight.

---

## 🌍 Production-Ready Extensions

ARDA's modular architecture enables straightforward enterprise integration:

### Database & Persistence
- Replace SQLite with **PostgreSQL** or **MySQL** for production scale
- Implement **TimescaleDB** for time-series log optimization
- Add **Redis** for caching and real-time analytics

### Integration Capabilities
- Connect to **SIEM platforms** (Splunk, ELK Stack, QRadar)
- Integrate with **IAM systems** (Okta, Active Directory, Azure AD)
- Link to **ticketing systems** (Jira, ServiceNow)

### Alerting & Notifications
- **Slack/Teams** integration for real-time alerts
- **Email** notifications for critical incidents
- **PagerDuty** integration for on-call escalation
- **Webhook** support for custom integrations

### Advanced Analytics
- **Machine learning**-based anomaly detection
- **User behavior analytics** (UBA)
- **Peer group analysis** for baseline comparison
- **Predictive threat modeling**

---

## 🎯 Intentional Design Decisions

### Why These Limitations Exist

#### Simulation-Focused
- **No actual user blocking:** Safe demonstration without production impact
- **Synthetic data generation:** Reproducible scenarios for testing

#### Security & Authentication
- **No authentication layer:** Simplified setup for demonstration purposes
- **Local-only deployment:** No exposure to security risks during development

#### Explainability Over Complexity
- **Rule-based logic:** Clear, auditable decision-making process
- **Transparent scoring:** Every decision is explainable to stakeholders
- **No ML black boxes:** Prioritizes understanding over complexity

> **💡 Philosophy:** ARDA demonstrates production-ready thinking while maintaining simplicity for educational and demonstrative purposes. Every limitation is intentional and documented.

---

## 💼 Use Cases

| Use Case | Description |
|----------|-------------|
| **🎓 Educational** | Learn enterprise security patterns, SOC workflows, and automated threat response systems |
| **📊 Portfolio Project** | Demonstrate full-stack security engineering capabilities to potential employers |
| **🔬 Research Platform** | Test new detection algorithms and response strategies in a controlled environment |
| **🏢 POC Foundation** | Starting point for enterprise proof-of-concept implementations |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help improve ARDA:

- 🐛 **Report bugs** - Open an issue with detailed reproduction steps
- 💡 **Suggest features** - Share your ideas for new capabilities
- 📝 **Improve documentation** - Help make ARDA more accessible
- 🔧 **Submit pull requests** - Add new features or fix issues

> **📋 Before Contributing:** Please ensure your code follows the existing style, includes appropriate tests, and updates documentation as needed.

---

## 📜 License

This project is open source and available under the **MIT License**.

Feel free to use, modify, and distribute as needed while maintaining attribution.

---

## 👨‍💻 Author

**Aditya Andhalkar**  
Backend & Security Engineering  
*Builder of Production-Style Systems*

[![GitHub](https://img.shields.io/badge/GitHub-Adi3182004-181717?style=for-the-badge&logo=github)](https://github.com/Adi3182004)
[![Project](https://img.shields.io/badge/Project-ARDA-blue?style=for-the-badge&logo=shield)](https://github.com/Adi3182004/Autonomous-Risk-Decision-Agent-ARDA-)

---

<div align="center">

**© 2025 ARDA - Autonomous Risk Decision Agent | Project 07**

*Built with 💙 for the Security Engineering Community*

⭐ **Star this repository** if you find it helpful!

</div>
