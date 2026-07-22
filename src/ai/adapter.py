"""
AI Adapter Interface.
Defines abstract interface for LLM / AI assistance with provider-neutral implementation.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAIAdapter(ABC):
    @abstractmethod
    def generate_summary(self, prompt_template_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate summary text given a prompt template and data context.
        Returns dictionary with text, generation_mode, confidence, and timestamp.
        """
        pass
