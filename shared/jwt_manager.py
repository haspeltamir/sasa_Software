import jwt
import datetime
from typing import Dict, Any, Optional


class JWTManager:
    """Manages JWT token creation and validation"""
    
    def __init__(self, secret: str, algorithm: str = "HS256"):
        self.secret = secret
        self.algorithm = algorithm
    
    def create_token(self, issuer: str, expiry_minutes: int = 5, **additional_claims) -> str:
        """Create a JWT token with the specified claims"""
        payload = {
            "iss": issuer,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=expiry_minutes),
            "iat": datetime.datetime.utcnow(),
            **additional_claims
        }
        
        token = jwt.encode(payload, self.secret, algorithm=self.algorithm)
        return token
    
    def validate_token(self, token: str, expected_issuer: str = None) -> Dict[str, Any]:
        """Validate a JWT token and return its payload"""
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            
            # Check issuer if specified
            if expected_issuer and payload.get("iss") != expected_issuer:
                raise jwt.InvalidTokenError("Invalid issuer")
            
            return payload
            
        except jwt.ExpiredSignatureError:
            raise jwt.InvalidTokenError("Token has expired")
        except jwt.InvalidTokenError:
            raise jwt.InvalidTokenError("Invalid token")
    
    def extract_token_from_header(self, authorization_header: str) -> str:
        """Extract JWT token from Authorization header"""
        if not authorization_header:
            raise ValueError("Authorization header is missing")
        
        if not authorization_header.startswith("Bearer "):
            raise ValueError("Authorization header must start with 'Bearer '")
        
        return authorization_header[7:]  # Remove "Bearer " prefix