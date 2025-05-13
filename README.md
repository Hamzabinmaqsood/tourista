# Tourista 🚀
[![Build Status](https://github.com/hamzabinmaqsood/tourista/actions/workflows/ci.yml/badge.svg)](https://github.com/Hamzabinmaqsood/tourista)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/hamzabinmaqsood/tourista.svg)](https://github.com/hamzabinmaqsood/tourista/stargazers)

> Django & PostgreSQL web app for real-time, location-based tour recommendations  

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## ✨ Features
- Personalized tour suggestions by category, distance, and budget
- Role-based access control (RBAC) with Django permissions
- Caching with Redis for 25% faster page loads
- OWASP Top 10 mitigations for injection, XSS, and CSRF
- Dockerized setup and CI/CD via GitHub Actions

## 🏗️ Tech Stack
| Layer        | Technology                         |
| ------------ | ---------------------------------- |
| Backend      | Python, Django, Django REST Framework |
| Database     | PostgreSQL                         |
| Caching      | Redis                              |
| Frontend     | Bootstrap 5, JavaScript            |
| DevOps       | Docker, GitHub Actions             |
| Security     | OWASP ZAP, Django Security Middleware |
| Project Mgmt | Jira, Trello, Scrum                |

## ⚙️ Installation

```bash
git clone https://github.com/hamzabinmaqsood/tourista.git
cd tourista

# Create & activate virtual env
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# ➜ then edit .env to set SECRET_KEY, DATABASE_URL, REDIS_URL

# Run migrations & start server
python manage.py migrate
python manage.py runserver
```

Clear, numbered steps expedite onboarding :contentReference[oaicite:11]{index=11}.

### 2.7. Usage  
```markdown
## 🚀 Usage
- Navigate to `http://localhost:8000`
- Register as a user or log in with demo credentials (`user/demo123`)
- Explore recommendation filters and view detailed tour pages
```

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the [MIT License](LICENSE).

## 📫 Contact
Hamza Bin Maqsood – hbinmaqsood@gmail.com 
Project Link: https://github.com/hamzabinmaqsood/tourista

