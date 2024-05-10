from infra.services import Services


class GuiConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Gui",
            path="./functions/gui",
            description="A simple hello world",
        )

        services.api_gateway.create_endpoint("GET", "/gui", function, public=True)
