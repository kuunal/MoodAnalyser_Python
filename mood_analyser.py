from multipledispatch  import dispatch
from exceptions.mood_analyser_exceptions import  MoodAnalyserError

class MoodAnalyser:

    def __init__(self,*message):
        if(len(message)>0):
            MoodAnalyser.message=message[0]

    @dispatch(str)
    def analyse_mood(self,message):
        MoodAnalyser.message=message
        return self.analyse_mood()

    @dispatch()
    def analyse_mood(self):
        if MoodAnalyser.message == None:
            raise MoodAnalyserError("Invalid message","NULL")
        if "happy" in MoodAnalyser.message.lower():
            return "Happy"
        return "Sad"