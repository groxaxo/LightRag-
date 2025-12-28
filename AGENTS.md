
# Project Directory Structure (Project Overview)

Yuxi-Know is an AI-powered knowledge base and knowledge graph agent development platform that integrates RAG technology and knowledge graph technology, built on LangGraph v1 + Vue.js + FastAPI + LightRAG architecture. The project is fully managed through Docker Compose and supports hot reload development.

## Development Principles

Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused.

Don't add features, refactor code, or make "improvements" beyond what was asked. A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability.

Don't add error handling, fallbacks, or validation for scenarios that can't happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs). Don't use backwards-compatibility shims when you can just change the code.

Don't create helpers, utilities, or abstractions for one-time operations. Don't design for hypothetical future requirements. The right amount of complexity is the minimum needed for the current task. Reuse existing abstractions where possible and follow the DRY principle.

## Development & Debugging Workflow

This project is fully managed through Docker Compose. All development and debugging should be performed in the running container environment. Use the `docker compose up -d` command to build and start.

**Core Principle**: Since both api-dev and web-dev services are configured with hot-reloading, there's no need to restart containers after modifying code locally - services will update automatically. First check if the project is already running in the background (`docker ps`), view logs (`docker logs api-dev --tail 100`). For details, see [docker-compose.yml](docker-compose.yml).

### Frontend Development Standards

- API Interface Standards: All API interfaces should be defined in web/src/apis
- Icons should be from @ant-design/icons-vue or lucide-vue-next (recommended, but pay attention to sizing)
- Vue styles use less, and must use color variables from [base.css](web/src/assets/css/base.css) unless absolutely necessary
- UI style should be simple and consistent, avoid hover displacement, don't overuse shadows and gradients
- Never attempt to use npm/pnpm to run the frontend development server


### Backend Development Standards

```bash
# Code checking and formatting
make lint          # Check code standards
make format        # Format code

# Execute commands directly in container
docker compose exec api uv run python test/your_script.py  # Place in test folder
```

Notes:

- Python code should conform to Python standards and pythonic style
- Use newer syntax when possible, avoid old version syntax (compatible with 3.12+)

**Other**:

- Use YUXI_SUPER_ADMIN_NAME / YUXI_SUPER_ADMIN_PASSWORD to debug interfaces
- If you need to create new documentation (only visible to developers, don't create unless necessary), save it in the `docs/vibe` folder
- After code updates, check if there are any parts of the documentation that need updating. The documentation directory is defined in `docs/.vitepress/config.mts`. Documentation should be updated in the latest version (`docs/latest`)
