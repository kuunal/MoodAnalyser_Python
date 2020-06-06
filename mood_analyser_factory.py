from exceptions.mood_analyser_exceptions import MoodAnalyserError

class MoodAnalyserFactory:
    def return_mood_analyser_object(self, filename, classname, *parameters):
        try:
            mood_class = __import__(filename)
            mood_class = getattr(mood_class, classname)
        except (ModuleNotFoundError, AttributeError):
            raise MoodAnalyserError("Classname or package name is invalid!","Invalid class or package")
        else:
            if(len(parameters)==0):
                return mood_class()
            else:
                return mood_class(parameters[0])
