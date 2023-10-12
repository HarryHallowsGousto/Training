def calculate_space(capacity: int, onboard: int, waiting_to_board: int) -> int:
    if capacity >= onboard + waiting_to_board:
        return 0
    else:
        passenger_excess = capacity - (onboard + waiting_to_board)
        return abs(passenger_excess)
