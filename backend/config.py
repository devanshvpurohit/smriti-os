"""
Smriti Configuration
Centralized configuration management using Pydantic Settings
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # Server Configuration
    host: str = Field(default="0.0.0.0", env="HOST")
    port: int = Field(default=8000, env="PORT")
    debug: bool = Field(default=True, env="DEBUG")
    
    # Database
    database_url: str = Field(
        default="sqlite:///./data/smriti.db",
        env="DATABASE_URL"
    )
    
    # Ollama Configuration
    ollama_base_url: str = Field(
        default="http://localhost:11434",
        env="OLLAMA_BASE_URL"
    )
    default_model: str = Field(default="mistral", env="DEFAULT_MODEL")
    default_embedding_model: str = Field(
        default="all-MiniLM-L6-v2",
        env="DEFAULT_EMBEDDING_MODEL"
    )
    
    # Document Processing
    max_file_size: int = Field(default=104857600, env="MAX_FILE_SIZE")  # 100MB
    upload_dir: str = Field(default="./uploads", env="UPLOAD_DIR")
    chunk_size: int = Field(default=512, env="CHUNK_SIZE")
    chunk_overlap: int = Field(default=50, env="CHUNK_OVERLAP")
    
    # Vector Store
    chroma_persist_dir: str = Field(
        default="./data/chroma",
        env="CHROMA_PERSIST_DIR"
    )
    collection_name: str = Field(
        default="smriti_documents",
        env="COLLECTION_NAME"
    )
    
    # Security
    secret_key: str = Field(
        default="your-secret-key-change-this-in-production",
        env="SECRET_KEY"
    )
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30,
        env="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    
    # CORS
    cors_origins: List[str] = Field(
        default=["http://localhost:4100", "http://puter.localhost:4100"],
        env="CORS_ORIGINS"
    )
    
    # Features
    enable_ocr: bool = Field(default=True, env="ENABLE_OCR")
    enable_reranking: bool = Field(default=True, env="ENABLE_RERANKING")
    confidence_threshold: float = Field(default=0.5, env="CONFIDENCE_THRESHOLD")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()


# Ensure required directories exist
def ensure_directories():
    """Create required directories if they don't exist"""
    directories = [
        settings.upload_dir,
        os.path.dirname(settings.database_url.replace("sqlite:///", "")),
        settings.chroma_persist_dir,
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Directory ensured: {directory}")


if __name__ == "__main__":
    # Test configuration
    print("Smriti Configuration:")
    print(f"  Host: {settings.host}:{settings.port}")
    print(f"  Database: {settings.database_url}")
    print(f"  Ollama: {settings.ollama_base_url}")
    print(f"  Model: {settings.default_model}")
    print(f"  Embedding: {settings.default_embedding_model}")
    print(f"  Upload Dir: {settings.upload_dir}")
    print(f"  Chunk Size: {settings.chunk_size}")
    print(f"  OCR Enabled: {settings.enable_ocr}")
    
    ensure_directories()
