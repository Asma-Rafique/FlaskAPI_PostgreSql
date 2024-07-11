# FlaskAPI_PostgreSql

### README Description

#### Template Management API

This API allows for the creation and management of templates with nested structures in a PostgreSQL database using FastAPI. The templates include tabs, sections, and fields, supporting a hierarchical and customizable configuration. 

Key features:
- **Create Template**: A POST endpoint to create a template with nested tabs, sections, and fields.
- **Retrieve Templates**: A GET endpoint to retrieve all created templates, displaying their hierarchical structure.
- **Database Integration**: Utilizes PostgreSQL with SQLAlchemy for relational data management.

#### User Authentication and Authorization API

This API provides user management functionality including registration and login using FastAPI and PostgreSQL, with secure password handling and JWT-based authentication.

Key features:
- **User Registration**: A POST endpoint for new user registration, ensuring email uniqueness and secure password hashing.
- **User Login**: A POST endpoint for user login, verifying credentials and issuing JWT access tokens for session management.
- **User Retrieval**: GET endpoints to fetch all users or a specific user by username, excluding password details for security.
- **JWT Authentication**: Secure JWT token generation and validation to manage user sessions.
