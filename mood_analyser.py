from exceptions.mood_analyser_exceptions import  MoodAnalyserError

class MoodAnalyser:
    message=""    
    
    def __init__(self, *message):
        if(len(message)>0):
            MoodAnalyser.message=message[0]

    def analyse_mood(self, *message):
        try:
            if(len(message)>0):
                self.message=message[0]
            self.check_empty(self.message)
            self.check_null(self.message)
            if "happy" in self.message.lower():
                return "Happy"
            return "Sad"
        except AttributeError:
            raise MoodAnalyserError("Invalid message!","Empty")
    
    def check_null(self, message):
        if self.message == None:
            raise MoodAnalyserError("Invalid message!","NULL")            


    def check_empty(self, message):
        if message == "":
            raise MoodAnalyserError("Invalid message!","Empty")

    def equals(self, object):
        if self==object or isinstance(object,MoodAnalyser):
            return True
        