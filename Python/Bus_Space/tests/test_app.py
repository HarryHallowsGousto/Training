from app import calculate_space

def test_that_when_no_excess_customers_return_0():
    # Arrange
    # Act
    actual_result = calculate_space(
        capacity=10,
        onboard=5,
        waiting_to_board=5
    )

    # Assert
    assert actual_result == 0


def test_when_excess_customers():
    # Arrange
    # Act
    actual_result = calculate_space(
        capacity=10,
        onboard=5,
        waiting_to_board=10
    )

    # Assert
    assert actual_result == 5