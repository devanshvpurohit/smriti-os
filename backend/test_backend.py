#!/usr/bin/env python3
"""
Test script for Smriti backend
Run this to verify the backend is working
"""

import asyncio
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(__file__))

from config import settings
from db.database import init_db
from services.llm.ollama_service import check_ollama_connection, list_models


async def test_backend():
    """Test all backend components"""
    print("🧪 Testing Smriti Backend Components\n")
    
    # Test 1: Configuration
    print("1. Testing Configuration...")
    print(f"   ✅ Database URL: {settings.database_url}")
    print(f"   ✅ Ollama URL: {settings.ollama_base_url}")
    print(f"   ✅ Upload Dir: {settings.upload_dir}")
    print(f"   ✅ Default Model: {settings.default_model}")
    
    # Test 2: Database
    print("\n2. Testing Database...")
    try:
        init_db()
        print("   ✅ Database initialized successfully")
    except Exception as e:
        print(f"   ❌ Database error: {e}")
        return False
    
    # Test 3: Ollama Connection
    print("\n3. Testing Ollama Connection...")
    try:
        connected = await check_ollama_connection()
        if connected:
            print("   ✅ Ollama connected successfully")
            
            # List models
            models = await list_models()
            if models:
                print(f"   ✅ Found {len(models)} models:")
                for model in models[:3]:  # Show first 3
                    print(f"      - {model.get('name', 'Unknown')}")
            else:
                print("   ⚠️  No models found - you may need to pull some models")
                print("   💡 Try: ollama pull mistral")
        else:
            print("   ❌ Ollama not connected")
            print("   💡 Make sure Ollama is running: ollama serve")
            return False
    except Exception as e:
        print(f"   ❌ Ollama error: {e}")
        return False
    
    # Test 4: Directory Structure
    print("\n4. Testing Directory Structure...")
    required_dirs = [
        settings.upload_dir,
        os.path.dirname(settings.database_url.replace("sqlite:///", "")),
        settings.chroma_persist_dir
    ]
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"   ✅ {directory}")
        else:
            print(f"   ⚠️  Creating {directory}")
            os.makedirs(directory, exist_ok=True)
    
    print("\n🎉 All tests passed! Backend is ready to run.")
    print("\n🚀 To start the backend:")
    print("   python main.py")
    print("\n📚 API will be available at:")
    print(f"   http://{settings.host}:{settings.port}")
    print(f"   http://{settings.host}:{settings.port}/docs (API documentation)")
    
    return True


if __name__ == "__main__":
    success = asyncio.run(test_backend())
    sys.exit(0 if success else 1)