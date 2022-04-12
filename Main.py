
#Find all findings and Supress them All:

#Importing boto3 for AWS Python 
import boto3
from datetime import datetime

#Default Product ARn for Security Hub
productArn = "arn:aws:securityhub:us-east-1::product/aws/securityhub"

Sclient = boto3.Session(region_name='us-east-1')
client = boto3.client('securityhub')


#Variables:
SeverityLabel = 'MEDIUM'
WorkflowStatus = "NEW"
Status = "SUPPRESSED"

Note ='Supressing to clean up all findings'
UpdatedBy = "Maks-Derevencha"

#This loops in 100 findings - so Counter < X is how many Hundreds you want to loop through. This limits the findings buffer for space/speed. 
counter = 0

#aws securityhub get-findings
while counter < 10:
    counter += 1
    res = client.get_findings(
        Filters={
            'SeverityLabel': [
                {
                    'Value': SeverityLabel,
                    'Comparison': 'EQUALS'
                }
            ],
            'WorkflowStatus': [
                {
                    'Value': WorkflowStatus,
                    'Comparison' : "EQUALS"
                }
            ],
        },
        MaxResults=100
    )
    
    #Looping through each finding to change the Workflow and add a note based on the ID from above loop. 
    for x in range(0,100):
        print(f"Starting Loop {x}")
        id = res["Findings"][x]['Id']
        print(f"ID: {id}")
        #update the findings

        res2 = client.batch_update_findings(
            FindingIdentifiers=[
                {
                    "Id": id,
                    'ProductArn': str(productArn)

                },
            ],
            Note={
                'Text': Note,
                'UpdatedBy': UpdatedBy,
            },
            Workflow={
                'Status': Status
            }
        )

        print(res2)
