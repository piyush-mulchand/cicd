import boto3

code_deploy = boto3.client('codedeploy')
lambda_func = boto3.client('lambda')

def cd_response(deploymentId,lifecycleEventHookExecutionId,status):
    return code_deploy.put_lifecycle_event_hook_execution_status(
                deploymentId=deploymentId,
                lifecycleEventHookExecutionId=lifecycleEventHookExecutionId,
                status=status
            )

def handler(event,context):
    deploymentId = event.deploymentId
    lifecycleEventHookExecutionId = event.lifecycleEventHookExecutionId
    lambda_respone = lambda_func.invoke(
                           FunctionName = os.environ['NewVersion'],
                           InvocationType='Event')
    if lambda_response:
        if lambda_response['message'] is 'success':
            response = cd_response(deploymentId,lifecycleEventHookExecutionId,'Succeeeded')
            print(response,' TEST PASS')
        else:
            response = cd_response(deploymentId,lifecycleEventHookExecutionId,'Failed')
            print(response,' TEST FAILED')