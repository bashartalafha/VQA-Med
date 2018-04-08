import re
class Utility(object):
    @staticmethod
    def clean(line):
        line = line.lower()
        line = line.replace('?', ' ?')
        line = re.sub(' +',' ', line)
        return line.strip()     
    
