

class mood_analyser:


    def analyse_mood(self,message):
        if "happy" in message.lower():
            return "Happy"
        return "Sad"