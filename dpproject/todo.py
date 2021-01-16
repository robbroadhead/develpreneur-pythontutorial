class Todo:
    title = ""
    status = ""
    
    def __init__ (self,title,status):
        self.title = title
        self.status = status
        
    def showTask(self):
        print(self.title + "[ " + self.status + " ]")
        
    def workTask(self):
        if self.status == "In Progress":
            self.status = "Complete"
        if self.status == "New":
            self.status = "In Progress"

