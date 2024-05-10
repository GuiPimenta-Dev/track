import json
import boto3
import click


class LiveSQS:
    def __init__(self, region, printer):
        self.sqs = boto3.client("sqs", region_name=region)
        self.printer = printer
        self.lambda_client = boto3.client("lambda", region_name=region)
        self.queue_url = self.sqs.create_queue(QueueName="Live-Queue")["QueueUrl"]

    def subscribe(self, function_arn, stub_name):
        self.printer.change_spinner_legend("Setting up Lambda Trigger for SQS Queue")

        response = self.sqs.get_queue_attributes(QueueUrl=self.queue_url, AttributeNames=["QueueArn"])

        # Extract the ARN from the response
        queue_arn = response["Attributes"]["QueueArn"]

        self.lambda_client.add_permission(
            FunctionName=stub_name,
            StatementId="sqs_invoke",
            Action="lambda:InvokeFunction",
            Principal="sqs.amazonaws.com",
            SourceArn=queue_arn,
        )

        self.lambda_client.create_event_source_mapping(EventSourceArn=queue_arn, FunctionName=function_arn)

        return self.queue_arn

    def publish(self, subject, msg_attributes):
        self.printer.show_banner("SQS")
        self.printer.log(f"Subject: {subject}", "white", 1)
        self.printer.log(f"Message Attributes: {msg_attributes}", "white", 1, 1)

        message_attributes = {}
        if msg_attributes:
            try:
                message_attributes = json.loads(msg_attributes)
                if not isinstance(message_attributes, dict):
                    self.log_failure(self.printer)
                    exit()
            except:
                self.log_failure(self.printer)
                exit()

        message = click.prompt(click.style("Message", fg=(37, 171, 190)), type=str)
        try:
            self.sqs.send_message(QueueUrl=self.queue_url, MessageBody=message, MessageAttributes=message_attributes)
        except:
            self.log_failure(self.printer)

    @staticmethod
    def log_failure(printer):
        printer.log("Failed to Publish Message!", "red")
        printer.log("Example of a Valid Payload: ", "gray", 1)
        payload = {
            "message": "Hello World!",
            "subject": "Hello World!",
            "message_attributes": {"Author": {"StringValue": "Daniel", "DataType": "String"}},
        }
        printer.log(json.dumps(payload, indent=4), "gray", 1, 1)

    @staticmethod
    def parse_logs(event):
        record = event["Records"][0]
        message_body = record["body"]
        message_attributes = record.get("messageAttributes", {})

        return {
            "Records": [
                {
                    "body": message_body,
                    "messageAttributes": message_attributes,
                }
            ]
        }
