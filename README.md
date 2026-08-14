# 💥 Dynamight-Blog API

An appreciation blog API for the character "Bakugo Katsuki" from the anime *My Hero Academia*.

[![Live API](https://img.shields.io/badge/Live_API-View_Swagger_Docs-85ea2d?style=for-the-badge&logo=swagger)](https://dynamight-blog-api.onrender.com/api/docs/)
[![GitHub repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/yoongles7/Dynamight-Blog)

---

## 🚀 Live Endpoints

The API is live and fully functional. You can explore and test all endpoints using the interactive Swagger documentation:

🔗 **[https://dynamight-blog-api.onrender.com/api/docs/](https://dynamight-blog-api.onrender.com/api/docs/)**

### Current Features

| Feature | Endpoint | Description |
| :--- | :--- | :--- |
| **Bakugo Details** | `GET /bakugo-details` | Retrieve general information about Bakugo Katsuki. |
| **User Registration** | `POST /users/register` | Create a new user account. |
| **User Login** | `POST /users/login` | Authenticate and obtain JWT access/refresh tokens. |
| **User Logout** | `POST /users/logout` | Blacklist the refresh token. |
| **Token Refresh** | `POST /users/refresh` | Obtain a new access token using a refresh token. |
| **API Docs** | `GET /api/docs` | Interactive Swagger UI for all available endpoints. |

---

## 🛠️ Tech Stack

- **Backend Framework**: Django 6.0 & Django REST Framework 3.17
- **Authentication**: JWT (`djangorestframework-simplejwt`) with token blacklisting
- **Database**: PostgreSQL 18 (production), development uses a local PostgreSQL container
- **Containerization**: Docker & Docker Compose for development and production
- **Deployment**: Deployed on Render
- **API Documentation**: `drf-spectacular` (OpenAPI 3.0) with Swagger UI & ReDoc

---

## 🏗️ Project Structure

```plaintext
.
├── apps/
│   ├── blog/          # Core blog functionality (Bakugo details)
│   ├── users/         # Custom user model & authentication logic
│   └── fanarts/       # (Coming soon) Fanart upload and management
├── config/
│   ├── settings/
│   │   ├── base.py           # Common settings for all environments
│   │   ├── development.py    # Development-specific settings
│   │   └── production.py     # Production-specific settings
│   ├── urls.py
│   └── wsgi.py
├── requirements/
│   ├── base.txt        # Core project dependencies
│   └── development.txt # Additional dependencies for local development
├── .dockerignore
├── .env.example
├── docker-compose.yaml # Local development orchestration
├── Dockerfile          # Multi-stage Docker build
├── entrypoint.sh       # Container entrypoint for migrations and server start
├── manage.py
└── README.md
```

---

## 🔧 Local Development Setup

### Prerequisites
- Docker and Docker Compose
- Python 3.12+ (for local runs without Docker)
- PostgreSQL (if running outside Docker)

### Option 1: Using Docker (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yoongles7/Dynamight-Blog.git
    cd Dynamight-Blog
    ```

2.  **Create your environment file:**
    ```bash
    cp .env.example .env.development
    ```
    *Edit `.env.development` and fill in your database credentials and `SECRET_KEY`.*

3.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```
    The API will be available at `http://localhost:8000`.

### Option 2: Without Docker (Local Python Environment)

1.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements/development.txt
    ```

3.  **Set up your environment:**
    ```bash
    cp .env.example .env.development
    # Edit .env.development with your local database credentials
    export DJANGO_SETTINGS_MODULE=config.settings.development
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

---

## ⚙️ Environment Variables

This project uses a `.env` file for configuration. A sample `.env.example` should be present in the root.

| Variable | Description | Example |
| :--- | :--- | :--- |
| `SECRET_KEY` | Django's secret key for cryptographic signing. | `django-insecure-...` |
| `DEBUG` | Debug mode (set to `True` for development). | `True` |
| `DB_NAME` | PostgreSQL database name. | `dynamightblog` |
| `DB_USER` | PostgreSQL user. | `blasty` |
| `DB_PASSWORD` | PostgreSQL password. | `secure_password` |
| `DB_HOST` | PostgreSQL host. | `localhost` (or `db` for Docker) |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts. | `localhost,127.0.0.1` |

---

## 🐳 Dockerization & Deployment

- **Development**: `docker-compose.yaml` orchestrates the Django app and a PostgreSQL container with volume mounts for live code reloading.
- **Production**: A multi-stage `Dockerfile` builds a lightweight image using Gunicorn. The app is configured via environment variables, and migrations run automatically via `entrypoint.sh`.
- **Hosting**: The production image is deployed on **Render**, connected to a PostgreSQL database.

---

## 🧪 Testing & Linting

*The foundation for testing is in place, with `pytest` and `ruff` available in the development requirements. This section can be expanded as tests are written.*

---

## 🤝 Contributing

As this is a personal appreciation project, external contributions are not currently open. However, feel free to fork the repository for your own learning or inspiration.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact & Acknowledgments

- **Author**: yoongles7
- **API**: Explore the live docs at [https://dynamight-blog-api.onrender.com/api/docs/](https://dynamight-blog-api.onrender.com/api/docs/)
- **Character**: Bakugo Katsuki, from *My Hero Academia* by Kohei Horikoshi.

**Great Explosion Murder God Dynamight** 🧡