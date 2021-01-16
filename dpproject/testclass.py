from todo import Todo
from deliverable import Deliverable

task = Todo("Task 1","New")
task2 = Todo("Task 2","In Progress")
deliv1 = Deliverable("Deliverable 1","New","PDF")

mytasks = [task,deliv1,task2]

for item in mytasks:
    item.showTask()