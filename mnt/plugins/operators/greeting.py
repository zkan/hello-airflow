from airflow.models.baseoperator import BaseOperator


class GreetingOperator(BaseOperator):
    """
    Simple example operator that logs one parameter and returns a string saying hi.
    :param my_parameter: (required) parameter taking any input.
    """

    def __init__(self, greeting: str, name: str, **kwargs) -> None:
        # initialize the parent operator
        super().__init__(**kwargs)

        # assign class variables
        self.greeting = greeting
        self.name = name

    # define the .execute() method that runs when a task uses this operator.
    # The Airflow context must always be passed to '.execute()', so make
    # sure to include the 'context' kwarg.
    def execute(self, context):
        self.log.info(f"{context}")

        greeting_message = f"{self.greeting}, {self.name}"
        self.log.info(greeting_message)

        # the return value of '.execute()' will be pushed to XCom by default
        return greeting_message
