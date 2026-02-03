"""
Communication Assistance Module

Provides communication support for individuals with autism including:
- Natural language processing for simplified communication
- Visual communication aids (picture exchange communication system)
- Speech-to-text and text-to-speech adapters
"""

from typing import Dict, List, Optional
from datetime import datetime
import logging
import re

logger = logging.getLogger(__name__)


class LanguageSimplifier:
    """Simplifies complex language into easier-to-understand formats."""
    
    def __init__(self):
        self.complexity_patterns = {
            'idiom': r'\b(piece of cake|raining cats and dogs|break a leg)\b',
            'sarcasm': r'\b(yeah right|as if|sure thing)\b',
            'metaphor': r'\b(time is money|life is a journey)\b',
        }
    
    def simplify_text(self, text: str) -> Dict:
        """
        Simplify complex text into clearer language.
        
        Args:
            text: Input text to simplify
            
        Returns:
            Dict with simplified text and explanations
        """
        simplified = text
        explanations = []
        
        # Detect and explain idioms
        idioms_found = re.findall(self.complexity_patterns['idiom'], text, re.IGNORECASE)
        if idioms_found:
            explanations.append(f"Idioms detected: {', '.join(idioms_found)}")
            # Simple replacements
            simplified = re.sub(r'piece of cake', 'easy', simplified, flags=re.IGNORECASE)
            simplified = re.sub(r'raining cats and dogs', 'raining heavily', simplified, flags=re.IGNORECASE)
            simplified = re.sub(r'break a leg', 'good luck', simplified, flags=re.IGNORECASE)
        
        # Break long sentences
        sentences = re.split(r'[.!?]+', simplified)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        # Simplify sentence structure
        simplified_sentences = []
        for sentence in sentences:
            # Remove filler words
            words = sentence.split()
            if len(words) > 15:
                explanations.append("Long sentence broken into simpler parts")
            simplified_sentences.append(sentence)
        
        result = {
            'original': text,
            'simplified': simplified,
            'sentences': simplified_sentences,
            'explanations': explanations,
            'complexity_score': self._calculate_complexity(text),
            'timestamp': datetime.now().isoformat()
        }
        
        return result
    
    def _calculate_complexity(self, text: str) -> float:
        """Calculate text complexity score (0-1)."""
        words = text.split()
        if not words:
            return 0.0
        
        avg_word_length = sum(len(word) for word in words) / len(words)
        sentences = len(re.split(r'[.!?]+', text))
        words_per_sentence = len(words) / max(1, sentences)
        
        # Normalize to 0-1 range
        complexity = min(1.0, (avg_word_length / 10 + words_per_sentence / 20) / 2)
        return complexity
    
    def detect_emotion_intent(self, text: str) -> Dict:
        """
        Detect emotional tone and intent in text.
        
        Args:
            text: Input text
            
        Returns:
            Dict with emotion and intent analysis
        """
        text_lower = text.lower()
        
        emotions = {
            'happy': ['happy', 'glad', 'excited', 'joy', 'great'],
            'sad': ['sad', 'unhappy', 'upset', 'disappointed'],
            'angry': ['angry', 'mad', 'frustrated', 'annoyed'],
            'anxious': ['worried', 'nervous', 'anxious', 'scared'],
            'calm': ['calm', 'relaxed', 'peaceful', 'fine']
        }
        
        detected_emotions = []
        for emotion, keywords in emotions.items():
            if any(keyword in text_lower for keyword in keywords):
                detected_emotions.append(emotion)
        
        # Detect intent (question vs statement)
        is_question = '?' in text or any(text_lower.startswith(q) for q in ['what', 'where', 'when', 'why', 'how', 'who'])
        
        return {
            'emotions': detected_emotions if detected_emotions else ['neutral'],
            'is_question': is_question,
            'intent': 'question' if is_question else 'statement',
            'text': text
        }


class VisualCommunicationAid:
    """Provides visual communication aids like picture exchange systems."""
    
    def __init__(self):
        self.symbol_library = self._initialize_symbols()
        self.communication_board = []
    
    def _initialize_symbols(self) -> Dict:
        """Initialize basic communication symbols/categories."""
        return {
            'needs': ['hungry', 'thirsty', 'tired', 'bathroom', 'help'],
            'feelings': ['happy', 'sad', 'angry', 'scared', 'calm'],
            'actions': ['eat', 'drink', 'play', 'sleep', 'go', 'stop'],
            'people': ['mom', 'dad', 'teacher', 'friend', 'doctor'],
            'places': ['home', 'school', 'park', 'store', 'outside'],
            'objects': ['toy', 'book', 'food', 'water', 'tablet']
        }
    
    def get_symbols_for_context(self, context: str) -> List[str]:
        """
        Get relevant communication symbols for a given context.
        
        Args:
            context: Context category (needs, feelings, actions, etc.)
            
        Returns:
            List of relevant symbols
        """
        return self.symbol_library.get(context, [])
    
    def create_communication_board(self, categories: List[str]) -> Dict:
        """
        Create a personalized communication board with selected categories.
        
        Args:
            categories: List of category names to include
            
        Returns:
            Dict with communication board configuration
        """
        board = {}
        for category in categories:
            if category in self.symbol_library:
                board[category] = self.symbol_library[category]
        
        self.communication_board = board
        
        return {
            'board': board,
            'total_symbols': sum(len(symbols) for symbols in board.values()),
            'categories': list(board.keys()),
            'timestamp': datetime.now().isoformat()
        }
    
    def interpret_symbol_sequence(self, symbols: List[str]) -> str:
        """
        Interpret a sequence of symbols into a sentence.
        
        Args:
            symbols: List of symbol names
            
        Returns:
            Interpreted sentence
        """
        if not symbols:
            return ""
        
        # Simple grammar rules
        sentence_parts = []
        
        # Check for "I" prefix
        if symbols[0] in ['I', 'me']:
            sentence_parts.append('I')
            symbols = symbols[1:]
        else:
            sentence_parts.append('I')
        
        # Add action verbs
        actions = [s for s in symbols if s in self.symbol_library.get('actions', [])]
        if actions:
            sentence_parts.extend(actions)
        
        # Add objects/needs
        for symbol in symbols:
            if symbol not in actions and symbol not in ['I', 'me']:
                sentence_parts.append(symbol)
        
        sentence = ' '.join(sentence_parts)
        return sentence.capitalize() + '.'
    
    def suggest_next_symbols(self, current_sequence: List[str]) -> List[str]:
        """
        Suggest next symbols based on current sequence.
        
        Args:
            current_sequence: Current symbol sequence
            
        Returns:
            List of suggested next symbols
        """
        if not current_sequence:
            # Suggest common starting symbols
            return ['I', 'help', 'want']
        
        last_symbol = current_sequence[-1]
        
        # If last was action, suggest objects
        if last_symbol in self.symbol_library.get('actions', []):
            return self.symbol_library.get('objects', []) + self.symbol_library.get('needs', [])
        
        # If last was feeling, suggest actions
        if last_symbol in self.symbol_library.get('feelings', []):
            return self.symbol_library.get('actions', [])
        
        # Default suggestions
        return self.symbol_library.get('actions', [])


class SpeechAdapter:
    """Adapters for speech-to-text and text-to-speech conversion."""
    
    def __init__(self):
        self.speech_history = []
    
    def speech_to_text(self, audio_data: bytes) -> Dict:
        """
        Convert speech to text (placeholder for actual STT integration).
        
        Args:
            audio_data: Audio data bytes
            
        Returns:
            Dict with transcription results
        """
        # This is a placeholder - in production, would integrate with
        # services like Google Speech-to-Text, AWS Transcribe, etc.
        
        result = {
            'transcription': '[Speech transcription would appear here]',
            'confidence': 0.95,
            'simplified': True,
            'timestamp': datetime.now().isoformat(),
            'note': 'Placeholder - requires STT service integration'
        }
        
        self.speech_history.append(result)
        return result
    
    def text_to_speech(self, text: str, voice_settings: Optional[Dict] = None) -> Dict:
        """
        Convert text to speech (placeholder for actual TTS integration).
        
        Args:
            text: Text to convert
            voice_settings: Optional voice customization settings
            
        Returns:
            Dict with speech synthesis results
        """
        # This is a placeholder - in production, would integrate with
        # services like Google TTS, Amazon Polly, etc.
        
        default_settings = {
            'rate': 'slow',  # slower speech for better comprehension
            'pitch': 'medium',
            'volume': 'normal'
        }
        
        settings = {**default_settings, **(voice_settings or {})}
        
        result = {
            'text': text,
            'audio_url': '[Audio URL would be here]',
            'settings': settings,
            'duration_estimate': len(text.split()) * 0.5,  # rough estimate
            'timestamp': datetime.now().isoformat(),
            'note': 'Placeholder - requires TTS service integration'
        }
        
        return result
    
    def get_speech_history(self, limit: int = 10) -> List[Dict]:
        """Get recent speech interaction history."""
        return self.speech_history[-limit:] if self.speech_history else []


class CommunicationAssistant:
    """
    Main communication assistance system integrating all components.
    """
    
    def __init__(self, user_id: Optional[str] = None):
        self.user_id = user_id or "default_user"
        self.simplifier = LanguageSimplifier()
        self.visual_aid = VisualCommunicationAid()
        self.speech_adapter = SpeechAdapter()
        self.conversation_history = []
    
    def process_text_input(self, text: str) -> Dict:
        """
        Process text input with simplification and emotion detection.
        
        Args:
            text: Input text
            
        Returns:
            Dict with processed results
        """
        simplified = self.simplifier.simplify_text(text)
        emotion_intent = self.simplifier.detect_emotion_intent(text)
        
        result = {
            'input': text,
            'simplified': simplified,
            'emotion_intent': emotion_intent,
            'timestamp': datetime.now().isoformat()
        }
        
        self.conversation_history.append(result)
        return result
    
    def create_visual_board(self, categories: List[str]) -> Dict:
        """Create a visual communication board."""
        return self.visual_aid.create_communication_board(categories)
    
    def interpret_visual_communication(self, symbols: List[str]) -> Dict:
        """
        Interpret visual symbol communication.
        
        Args:
            symbols: List of selected symbols
            
        Returns:
            Dict with interpretation and suggestions
        """
        interpretation = self.visual_aid.interpret_symbol_sequence(symbols)
        suggestions = self.visual_aid.suggest_next_symbols(symbols)
        
        return {
            'symbols': symbols,
            'interpretation': interpretation,
            'suggested_next': suggestions,
            'timestamp': datetime.now().isoformat()
        }
    
    def convert_speech(self, audio_data: bytes) -> Dict:
        """Convert speech to simplified text."""
        stt_result = self.speech_adapter.speech_to_text(audio_data)
        
        # Simplify the transcription
        if 'transcription' in stt_result:
            simplified = self.simplifier.simplify_text(stt_result['transcription'])
            stt_result['simplified_text'] = simplified
        
        return stt_result
    
    def speak_text(self, text: str, voice_settings: Optional[Dict] = None) -> Dict:
        """Convert text to speech."""
        return self.speech_adapter.text_to_speech(text, voice_settings)
    
    def get_conversation_summary(self) -> Dict:
        """Get summary of conversation history."""
        return {
            'user_id': self.user_id,
            'total_interactions': len(self.conversation_history),
            'recent_history': self.conversation_history[-5:] if self.conversation_history else [],
            'visual_board': self.visual_aid.communication_board
        }
