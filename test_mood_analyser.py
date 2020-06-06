import pytest
from mood_analyser import MoodAnalyser
from exceptions.mood_analyser_exceptions import  MoodAnalyserError
from  mood_analyser_factory import MoodAnalyserFactory

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
    
    def test_given_moodanalyser_class_when_corect_returns_object(self):
        mood = MoodAnalyserFactory()
        mood_object = MoodAnalyser()
        assert mood_object.equals(mood.return_mood_analyser_object("mood_analyser","MoodAnalyser"))
        

    def test_given_MoodAnalyser_class_when_incorect_throws_exception(self):
        with pytest.raises(MoodAnalyserError) as e:
            mood = MoodAnalyserFactory()
            mood_object = MoodAnalyser()
            assert mood_object.equals(mood.return_mood_analyser_object("mood_analyser","Incorrect Class"))
        assert str(e.value) == "Classname or package name is invalid!" 

        
    def test_given_package_when_incorect_throws_exception(self):
        with pytest.raises(MoodAnalyserError) as e:
            mood = MoodAnalyserFactory()
            mood_object = MoodAnalyser()
            assert mood_object.equals(mood.return_mood_analyser_object("Incorrect Class","MoodAnalyser"))
        assert str(e.value) == "Classname or package name is invalid!" 

    
    def test_given_moodanalyser_class_with_parameters_when_corect_returns_object(self):
        mood = MoodAnalyserFactory()
        mood_object = MoodAnalyser()
        assert mood_object.equals(mood.return_mood_analyser_object("mood_analyser","MoodAnalyser","I am in happy mood"))
        
    # def test_given_parameterized_moodanalyser_object_(self):
    #     mood = MoodAnalyserFactory()
    #     mood_object = MoodAnalyser()
    #     result = mood.return_mood_analyser_object("mood_analyser","MoodAnalyser","I am in happy mood").analyse_mood()
    #     assert result == "Happy"


    def test_given_MoodAnalyser_class_when_incorect_throws_exception(self):
        with pytest.raises(MoodAnalyserError) as e:
            mood = MoodAnalyserFactory()
            mood_object = MoodAnalyser()
            assert mood_object.equals(mood.return_mood_analyser_object("mood_analyser","Incorrect Class","I am in happy mood"))
        assert str(e.value) == "Classname or package name is invalid!" 

    def test_given_method_name_when_correct_returns_happy(self):
        mood_object = MoodAnalyser("I am in happy mood")
        mood_factory = MoodAnalyserFactory()
        mood = mood_factory.invoke_methods("mood_analyser","MoodAnalyser", "analyse_mood", "I am in happy mood")
        assert mood is "Happy"

    def test_given_method_name_when_incorrect_returns_throws_exception(self):
        with pytest.raises(MoodAnalyserError) as e:
            mood_object = MoodAnalyser("I am in happy mood")
            mood_factory = MoodAnalyserFactory()
            mood = mood_factory.invoke_methods("mood_analyser","MoodAnalyser", "InvalidMethiod", "I am in happy mood")
            assert mood is "Happy"
        assert str(e.value) == "Invalid method name"