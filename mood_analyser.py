from multipledispatch  import dispatch

class mood_analyser:
    message=""

    def __init__(self,*message):
        if(len(message)>0):
            mood_analyser.message=message[0]

    @dispatch(str)
    def analyse_mood(self,message):
        mood_analyser.message=message
        return self.analyse_mood()

    @dispatch()
    def analyse_mood(self):
        if "happy" in mood_analyser.message.lower():
            return "Happy"
        return "Sad"