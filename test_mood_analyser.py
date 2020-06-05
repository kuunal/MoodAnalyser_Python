import pytest
from mood_analyser import mood_analyser


mood_object=""

def setup_module(module):
    global mood_object
    mood_object = mood_analyser()

def test_passes_for_happy_message_when_returns_happy():
    assert mood_object.analyse_mood("I am in happy mood!") == "Happy"

def test_passes_for_sad_message_when_returns_sad():
    assert mood_object.analyse_mood("I am in sad mood!") == "Sad"

def test_passes_when_message_passed_through_constructor_for_happy_message():
    mood_object1 = mood_analyser("I am in happy mood")
    assert mood_object1.analyse_mood() == "Happy"

def test_passes_when_message_passed_through_constructor_for_sad_message():
    mood_object1 = mood_analyser("I am in sad mood")
    assert mood_object1.analyse_mood() == "Sad"
