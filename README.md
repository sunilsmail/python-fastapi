# python-fastapi
python-fastapi

## pip install fastapi uvicorn sqlalchemy alembic pydantic
### pip install python-jose[cryptography] passlib[bcrypt] python-multipart
#### pip install httpx pytest

# Run tests: pytest tests/
## Install Dependencies: pip install -r requirements.txt
# Run the application: uvicorn main:app --reload

<pre>
📂 fastapi_crud_app/
 ├── __init__.py          
 ├── main.py               # FastAPI application entry point
 ├── database.py           # Database connection setup
 ├── models.py             # SQLAlchemy models
 ├── schemas.py            # Pydantic schemas for validation
 ├── repository.py         # Repository layer for CRUD operations
 ├── services.py           # Service layer for business logic
 ├── routes.py             # User API routes
 ├── auth.py               # Authentication (JWT)
 ├── tests/                # Unit tests
 │   ├── __init__.py
 │   ├── test_main.py       # Test cases

 </pre>

SOLID Principle	Implementation
Single Responsibility	Each module (database.py, models.py, repository.py, etc.) has a specific task.
Open/Closed	New features can be added without modifying existing code (e.g., new repository methods).
Liskov Substitution	The repository follows an interface-like structure, ensuring interchangeable implementations.
Interface Segregation	The API endpoints are modular, not forcing consumers to use unwanted methods.
Dependency Injection	Database sessions (get_db()) are injected, making testing and refactoring easy.
