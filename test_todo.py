import pytest
from app import addTask, getTasks



@pytest.fixture(autouse=True)
def reset_tasks():
    from app import tasks 
    tasks.clear()


def test_add_task():
    result = addTask("Test Task")
    assert result == "Task added."
    assert "Test Task" in getTasks()
    assert len(getTasks()) == 1


def test_get_tasks():
    addTask("Another Task")
    tasks = getTasks()
    assert len(tasks) == 1
    assert tasks[0] == "Another Task"
