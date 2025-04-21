from typing import Dict, Any

# In-memory storage (reset on restart)
user_profiles: Dict[str, str] = {}
user_chunks:   Dict[str, list[str]] = {}
user_index:    Dict[str, Any] = {}
