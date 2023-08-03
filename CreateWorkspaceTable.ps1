# Create new table in Log Analytics workspace - RUN on Cloudshell
$tableParams = @'
{
    "properties": {
        "schema": {
            "name": "MyTable_CL",
            "columns": [
                {
                    "name": "TimeGenerated",
                    "type": "datetime",
                    "description": "The time at which the data was generated"
                },
               {
                    "name": "Computer",
                    "type": "string",
                    "description": "The computer that generated the data"
                },
                {
                    "name": "AdditionalContext",
                    "type": "dynamic",
                    "description": "Additional message properties"
                },
                {
                    "name": "CounterName",
                    "type": "string",
                    "description": "Name of the counter"
                },
                {
                    "name": "CounterValue",
                    "type": "real",
                    "description": "Value collected for the counter"
                }
            ]
        }
    }
}
'@
$subscription='b93a54e9-00d4-47bb-918d-57ce97c597b6'
$resourcegroup='my-workspace'
$workspace='my-workspace'

Invoke-AzRestMethod -Path "/subscriptions/$subscription/resourcegroups/$resourcegroup/providers/microsoft.operationalinsights/workspaces/$workspace/tables/MyTable_CL?api-version=2021-12-01-preview" -Method PUT -payload $tableParams