from infra.services import Services


class TreConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Tre",
            path="./functions/tre",
            description="A simple hello world",
        )

        services.api_gateway.create_endpoint("GET", "/tre", function, public=True)
