from todo import Todo

class Deliverable(Todo):
    results = "Document"
    
    def __init__(self,title,status,result):
        super().__init__(title,status)
        self.results = result
        
    def showTask(self):
        print(self.title + "[ " + self.status + " ] - Deliverable Type: " + self.results)
        
