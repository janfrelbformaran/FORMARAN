from app import addTask, getTasks


def test_add_task():
    result = addTask("Test Task")
    assert result == "Task added."
    assert "Test Task" in getTasks()


def test_get_tasks():
    addTask("Another Task")
    tasks = getTasks()
    assert len(tasks) == 1
    assert tasks[0] == "Another Task"
