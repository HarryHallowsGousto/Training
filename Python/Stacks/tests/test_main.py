from Stacks.src.main import Stack


def test_push():
    # Arrange
    item = "bla"

    stack = Stack()

    # Act
    stack.push(item=item)

    # Assert
    assert stack.stack[0] == "bla", "Error: Expected 'bla' in the stack."


def test_pop():
    # Arrange
    items = ["apple", "chocolate"]
    stack = Stack()

    # Act
    for item in items:
        stack.push(item=item)

    stack.pop()

    # Assert
    assert stack.stack == [items[1]]


def test_pop_raises_exception():
    # Arrange
    stack = Stack()

    # Act
    try:
        stack.pop()
    except ValueError as e:
        # Assert
        assert str(e) == "Stack is empty, so can't remove top item from the stack"


def test_peek():
    # Arrange
    items = ["pepper", "pakchoi"]
    stack = Stack()

    # Act
    for item in items:
        stack.push(item=item)

    stack.peek()

    # Assert
    assert stack.stack[0] == items[0], f"ValueError: was expecting '{items[0]}' to be returned"


def test_peek_raises_exception():
    # Arrange
    stack = Stack()

    # Act
    try:
        stack.peek()
    except ValueError as e:
        # Assert
        assert str(e) == "Stack is empty, so can't peek at the top item in stack"


def test_is_empty():
    # Arrange
    stack = Stack()

    # Act
    stack.is_empty()

    # Assert
    assert stack.is_empty() is True
