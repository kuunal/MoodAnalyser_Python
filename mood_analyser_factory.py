

class MoodAnalyserFactory:
    def return_mood_analyser_object(self, filename):
        mood_class = __import__(filename)
        mood_class = getattr(mood_class,"MoodAnalyser")
        return mood_class()
