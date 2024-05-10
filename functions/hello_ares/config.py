from infra.services import Services


class HelloAresConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="HelloAres",
            path="./functions/hello_ares",
            description="A simple hello world",
        )

        services.api_gateway.create_endpoint("GET", "/hello_ares", function, public=True)
