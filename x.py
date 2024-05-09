import boto3

def get_api_gateway_url(stack_name):
    # Create a CloudFormation client
    client = boto3.client('cloudformation')

    # Retrieve the stack information
    response = client.describe_stacks(StackName=stack_name)

    # Loop through the outputs and find the API Gateway URL
    for stack in response['Stacks']:
        for output in stack['Outputs']:
            if output['OutputKey'] == 'API-GATEWAY-BASE-URL':
                return output['OutputValue']

    return None

# Example usage
stack_name = 'Dev-Dev-Track-Lambda-Stack'
api_url = get_api_gateway_url(stack_name)
print(f"API Gateway URL: {api_url}")
