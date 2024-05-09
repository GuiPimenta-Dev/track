from infra.services import Services


class HelloJhonyConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="HelloJhony",
            path="./functions/hello_jhony",
            description="A simple hello world",
            
        )

        services.api_gateway.create_endpoint("GET", "/hello_jhony", function, public=True)

            