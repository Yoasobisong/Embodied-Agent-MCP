import jwt
from functools import wraps
from typing import Callable, Any
import os

JWT_SECRET = os.environ.get("JWT_SECRET_KEY", "enterprise-super-secret-key-256bit")

def require_auth(func: Callable) -> Callable:
    """
    Enterprise MCP Middleware: JWT Authentication and Role-Based Access Control (RBAC).
    Ensures that only authorized Agents can call specific hardware actuation tools.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # In a real FastMCP request context, we would extract the Bearer token
        # from the metadata or HTTP headers. For demonstration, we assume a context injection.
        token = kwargs.get("auth_token", None)
        
        if not token:
            raise Exception("Authentication required: Missing token.")
        
        try:
            decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            roles = decoded.get("roles", [])
            
            # Example RBAC logic
            if "HARDWARE_CONTROL" not in roles:
                raise Exception("Authorization failed: Missing HARDWARE_CONTROL role.")
                
        except jwt.ExpiredSignatureError:
            raise Exception("Authentication failed: Token expired.")
        except jwt.InvalidTokenError:
            raise Exception("Authentication failed: Invalid token.")
            
        # Strip token from kwargs before passing to actual tool
        if "auth_token" in kwargs:
            del kwargs["auth_token"]
            
        return func(*args, **kwargs)
    return wrapper
