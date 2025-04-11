import todo


result = todo.addTask("Learn Python")
print("Test addTask:", "Pass" if "Learn Python" in todo.tasks else "Fail")


allTasks = todo.getTasks()
print("Test getTasks:", "Pass" if allTasks == ["Learn Python"] else "Fail")
