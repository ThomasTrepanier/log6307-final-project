import boto3

def get_roles_for_policy(policy_arn):
    client = boto3.client('iam')
    paginator = client.get_paginator('list_roles')

    roles_with_policy = []
    for page in paginator.paginate():
        for role in page['Roles']:
            attached_policies = client.list_attached_role_policies(RoleName=role['RoleName'])['AttachedPolicies']
            for policy in attached_policies:
                if policy['PolicyArn'] == policy_arn:
                    roles_with_policy.append(role['RoleName'])

    return roles_with_policy
