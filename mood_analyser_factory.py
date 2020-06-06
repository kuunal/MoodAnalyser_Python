from exceptions.mood_analyser_exceptions import MoodAnalyserError

class MoodAnalyserFactory:
    def return_mood_analyser_object(self, filename, classname):
        try:
            mood_class = __import__(filename)
            mood_class = getattr(mood_class, classname)
        except (ModuleNotFoundError, AttributeError):
            raise MoodAnalyserError("Classname or package name is invalid!","Invalid class or package")
        else:
            return mood_class()

