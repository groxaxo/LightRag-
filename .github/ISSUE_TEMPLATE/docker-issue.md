---
name: Report a Startup Issue
about: Docker image pulling, service startup, port conflicts, and other related issues
title: 'Startup: '
labels: startup
assignees: ''

---

## 1️⃣ Problem Description

Please clearly describe the issue you encountered when using Docker or starting services:
- Operation Steps: What did you do?
- Expected Result: What did you expect to happen?
- Actual Result: What actually happened?

For example: "After executing `docker compose up -d`, the api-dev service keeps restarting, and logs show it cannot connect to Milvus"

You can first check common issues and solutions: https://xerrors.github.io/Yuxi-Know/latest/changelog/faq.html


## 2️⃣ Environment Information

Please provide the following information to help us quickly locate the issue:
- Operating System: Windows/macOS/Linux and version
- Docker Version: Output of `docker --version`
- Docker Compose Version: Output of `docker compose --version`
- Project Version: Output of `git rev-parse HEAD`


## 3️⃣ Startup Command

Please provide the complete startup command you used:
```bash
# For example
docker compose up -d
# Or
make start
```


## 4️⃣ Log Information

Please provide logs from relevant services (at least the last 100 lines):

```bash
# Check all service statuses
docker ps

# Check api-dev service logs
docker logs --tail=100 api-dev

# Check all service logs
docker compose logs --tail=100
```

Paste logs below (select relevant portions based on the issue):

```
# api-dev logs
...

# Other relevant service logs
...
```


## 5️⃣ Configuration Files (Optional)

If you modified `docker-compose.yml` or `.env` files, please provide relevant configuration snippets (hide sensitive information):

```yaml
# docker-compose.yml relevant parts
...

# .env relevant parts
...
```


## 6️⃣ Additional Information

You can also provide the following information to help us solve the issue:
- Have you tried restarting Docker service?
- Have you cleaned Docker cache or old containers?
- Does your network environment have special configurations (such as proxy, firewall, etc.)?
- Are there any other related error messages or screenshots?
