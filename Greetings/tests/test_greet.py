from Greetings.src.greet import Greetings, People


def test_simple_greeting_input():
    # Arrange
    person = People(names="Andy")
    individual = Greetings(person)

    # Act
    greeting = Greetings.greet(individual)

    # Assert
    assert greeting == f"Hello, {person.names}."


def test_input_is_null_with_generic_greeting():
    # Arrange
    person = People(None)
    individual = Greetings(person)

    # Act
    greeting = Greetings.greet(individual)

    # Assert
    assert greeting == "Hello, my friend."


def test_input_is_uppercase_greeting():
    # Arrange
    person = People(
        names="JIM",
    )
    individual = Greetings(person)

    # Act
    greeting = Greetings.greet(individual)

    # Assert
    assert greeting == f"HELLO {person.names}!"


def test_two_input_greetings():
    # Arrange
    people = People(
        names=
        [
            "Sally",
            "Andre"
        ],
    )

    individuals = Greetings(people)
    # Act
    greeting = Greetings.greet(individuals)

    # Assert
    assert greeting == f"Hello, {people.names[0]} and {people.names[1]}."


def test_multiple_input_greetings():
    # Arrange
    people = People(
        names=
        [
            "Sally",
            "Andre",
            "Jim",
            "Poppy"
        ],
    )

    individuals = Greetings(people)
    # Act
    greeting = Greetings.greet(individuals)

    # Assert
    assert greeting == f"Hello, {people.names[0]}, {people.names[1]}, {people.names[2]} and {people.names[3]}."


def test_multiple_with_variance_input_greetings():
    # Arrange
    people = People(
        names=
        [
            "Sally",
            "Andre",
            "JIM",
            "Poppy"
        ],
    )

    individuals = Greetings(people)
    # Act
    greeting = Greetings.greet(individuals)

    # Assert
    assert greeting == f"Hello, {people.names[0]}, {people.names[1]} and {people.names[3]}. AND HELLO {people.names[2]}."


def test_multiple_names_provided_in_single_input():
    # Arrange
    people = People(
        names=[
            "Jimmy, Diana",
            "Bobby"
        ]
    )

    individuals = Greetings(people)
    # Act
    greeting = Greetings.greet(individuals)

    # Assert
    assert greeting == "Hello, Jimmy, Diana and Bobby."


def test_multiple_names_capitalised_in_single_input():
    # Arrange
    people = People(
        names=[
            "JIMMY, DIANA",
            "Bobby"
        ]
    )

    individuals = Greetings(people)
    # Act
    greeting = Greetings.greet(individuals)

    # Assert
    assert greeting == "Hello, Jimmy, DIANA and BOBBY."


def test_input_with_and_in_the_name():
    # Arrange
    people = People(
        names=[
            "Jimmy",
            "Diana",
            "Andy"
        ]
    )

    individuals = Greetings(people)
    # Act
    greeting = Greetings.greet(individuals)

    # Assert
    assert greeting == "Hello, Jimmy, Diana and Andy."


def test_double_quotes_opting_out_of_comma_input():
    people = People(
        names=[
            "Bill",
            "\"Charles, Richard\""
        ]
    )

    individuals = Greetings(people)

    greeting = Greetings.greet(individuals)

    assert greeting == "Hello, Bill and Charles, Richard."


