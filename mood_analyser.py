from exceptions.mood_analyser_exceptions import  MoodAnalyserError

class MoodAnalyser:
    
    
    def __init__(self, *message):
        if(len(message)>0):
            MoodAnalyser.message=message[0]

    def analyse_mood(self, *message):
        try:
            if(len(message)>0):
                MoodAnalyser.message=message[0]
            if self.message == None:
                raise MoodAnalyserError("Invalid message!","NULL")
            if "happy" in MoodAnalyser.message.lower():
                return "Happy"
            elif "sad" in MoodAnalyser.message.lower():
                return "Sad"
        except AttributeError:
            raise MoodAnalyserError("Invalid message!","Empty")
    

    def equals(self, object):
        if self==object or isinstance(object,MoodAnalyser):
            return True
        