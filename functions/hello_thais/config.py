from infra.services import Services


class HelloThaisConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="HelloThais",
            path="./functions/hello_thais",
            description="A simple hello world",
        )

        services.api_gateway.create_endpoint("GET", "/hello_thais", function, public=True)
