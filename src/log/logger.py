import os.path
from datetime import datetime

class Logger():
    def __init__(self):
        pass
    
    #This is a simple log system - it is not thread-safe!
    @classmethod
    def log(cls,prefix: str, message: str, file="main_log.txt"):
        entry = f"[{prefix}] {message}"
        #create correct path to file
        my_path = os.getcwd().split("airTracker", 1)[0]
        my_path = os.path.join(my_path, "airTracker", "src", "log", file)
        
        #write to file
        if not os.path.exists(my_path):
            with open(my_path, "w", encoding=("UTF-8")) as f:
                f.write("Log-File for Air-Tracker. Created:"\
                        f" {datetime.today().isoformat()}\n\n")
        with open(my_path, "a", encoding=("UTF-8")) as f:
            f.write(f"{entry} -- {datetime.today().isoformat()}\n")
    
    @classmethod
    def log_csv(cls, message: tuple, file="data"):
        entry = cls.get_entry(message)
        #create correct path to file
        my_path = os.getcwd().split("airTracker", 1)[0]
        my_path = os.path.join(my_path, "airTracker", "src", "log", f"{file}.csv")
        
        #write to file
        if not os.path.exists(my_path):
            with open(my_path, "w", encoding=("UTF-8")) as f:
                pass
        with open(my_path, "a", encoding=("UTF-8")) as f:
            f.write(entry)

    @classmethod
    def get_entry(cls, message: tuple):
        return_value = ""
        for item in message:
            return_value += f"{item},"
        return f"{return_value[:-1]}\n"

