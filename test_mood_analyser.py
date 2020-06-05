import pytest
from mood_analyser import mood_analyser


mood_object=""

def setup_module(module):
    global mood_object
    mood_object = mood_analyser()

def test_passes_for_happy_message_when_returns_happy():
    assert mood_object.analyse_mood("I am in happy mood!") == "Happy"
