"""
Unit tests for the Communication Assistant
"""

import unittest
from autism_support.communication import (
    LanguageSimplifier,
    VisualCommunicationAid,
    SpeechAdapter,
    CommunicationAssistant
)


class TestLanguageSimplifier(unittest.TestCase):
    """Test cases for LanguageSimplifier."""
    
    def setUp(self):
        self.simplifier = LanguageSimplifier()
    
    def test_simplify_idioms(self):
        """Test simplification of idioms."""
        text = "This task is a piece of cake!"
        result = self.simplifier.simplify_text(text)
        
        self.assertIn('easy', result['simplified'].lower())
        self.assertTrue(len(result['explanations']) > 0)
    
    def test_complexity_score(self):
        """Test complexity scoring."""
        simple_text = "The cat sat on the mat."
        complex_text = "The feline creature positioned itself upon the rectangular textile floor covering."
        
        simple_result = self.simplifier.simplify_text(simple_text)
        complex_result = self.simplifier.simplify_text(complex_text)
        
        self.assertLess(
            simple_result['complexity_score'],
            complex_result['complexity_score']
        )
    
    def test_emotion_detection(self):
        """Test emotion detection in text."""
        happy_text = "I am so happy and excited today!"
        result = self.simplifier.detect_emotion_intent(happy_text)
        
        self.assertIn('happy', result['emotions'])
        self.assertEqual(result['intent'], 'statement')
    
    def test_question_detection(self):
        """Test question intent detection."""
        question = "What time is it?"
        result = self.simplifier.detect_emotion_intent(question)
        
        self.assertTrue(result['is_question'])
        self.assertEqual(result['intent'], 'question')


class TestVisualCommunicationAid(unittest.TestCase):
    """Test cases for VisualCommunicationAid."""
    
    def setUp(self):
        self.visual_aid = VisualCommunicationAid()
    
    def test_get_symbols(self):
        """Test getting symbols for context."""
        needs = self.visual_aid.get_symbols_for_context('needs')
        
        self.assertTrue(len(needs) > 0)
        self.assertIn('hungry', needs)
    
    def test_create_board(self):
        """Test creating communication board."""
        result = self.visual_aid.create_communication_board(['needs', 'actions'])
        
        self.assertIn('needs', result['categories'])
        self.assertIn('actions', result['categories'])
        self.assertTrue(result['total_symbols'] > 0)
    
    def test_interpret_symbols(self):
        """Test interpreting symbol sequence."""
        symbols = ['I', 'hungry']
        interpretation = self.visual_aid.interpret_symbol_sequence(symbols)
        
        self.assertIn('hungry', interpretation.lower())
        self.assertTrue(interpretation.endswith('.'))
    
    def test_suggest_next_symbols(self):
        """Test symbol suggestions."""
        current = ['I', 'want']
        suggestions = self.visual_aid.suggest_next_symbols(current)
        
        self.assertTrue(len(suggestions) > 0)


class TestCommunicationAssistant(unittest.TestCase):
    """Test cases for CommunicationAssistant integration."""
    
    def setUp(self):
        self.assistant = CommunicationAssistant(user_id="test_user")
    
    def test_process_text(self):
        """Test text processing."""
        text = "It's raining cats and dogs!"
        result = self.assistant.process_text_input(text)
        
        self.assertIn('simplified', result)
        self.assertIn('emotion_intent', result)
        self.assertEqual(len(self.assistant.conversation_history), 1)
    
    def test_visual_board_creation(self):
        """Test creating visual board."""
        board = self.assistant.create_visual_board(['needs', 'feelings'])
        
        self.assertTrue(board['total_symbols'] > 0)
    
    def test_visual_communication(self):
        """Test visual symbol interpretation."""
        symbols = ['I', 'happy']
        result = self.assistant.interpret_visual_communication(symbols)
        
        self.assertIn('interpretation', result)
        self.assertIn('suggested_next', result)
    
    def test_conversation_summary(self):
        """Test getting conversation summary."""
        self.assistant.process_text_input("Hello")
        summary = self.assistant.get_conversation_summary()
        
        self.assertEqual(summary['user_id'], 'test_user')
        self.assertEqual(summary['total_interactions'], 1)


if __name__ == '__main__':
    unittest.main()
