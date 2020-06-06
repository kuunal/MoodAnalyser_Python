import pytest
from mood_analyser import MoodAnalyser
from exceptions.mood_analyser_exceptions import  MoodAnalyserError

class TestMoodAnalyser:

    def test_passes_for_happy_message_when_returns_happy(self):
        mood_object = MoodAnalyser()
        assert mood_object.analyse_mood("I am in happy mood!") == "Happy"

    def test_passes_for_sad_message_when_returns_sad(self):
        mood_object = MoodAnalyser()
        assert mood_object.analyse_mood("I am in sad mood!") == "Sad"

    def test_passes_when_message_passed_through_constructor_for_happy_message(self):
        mood_object1 = MoodAnalyser("I am in happy mood")
        assert mood_object1.analyse_mood() == "Happy"

    def test_passes_when_message_passed_through_constructor_for_sad_message(self):
        mood_object1 = MoodAnalyser("I am in sad mood")
        assert mood_object1.analyse_mood() == "Sad"
    
    def test_passes_for_none_message_when_throws_exception(self):
        with pytest.raises(MoodAnalyserError) as mood_exception:
            mood_object = MoodAnalyser()
            mood_object.analyse_mood(None) 
        assert str(mood_exception.value) == "Invalid message!"


    def test_given_constructor_when_none_message_throws_exception(self):
        with pytest.raises(MoodAnalyserError) as mood_exception:
            mood_object = MoodAnalyser(None)
            mood_object.analyse_mood() 
        assert str(mood_exception.value) == "Invalid message!"
        


    def test_given_empty_mood_throws_exception(self):
        with pytest.raises(MoodAnalyserError) as mood_exception:    
            mood_object = MoodAnalyser()
            mood_object.analyse_mood()
        assert str(mood_exception.value) == "Invalid message!"
    