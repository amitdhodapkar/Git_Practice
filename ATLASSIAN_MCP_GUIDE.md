# Atlassian MCP JIRA Integration

This project provides a simple connector to fetch bugs from JIRA Cloud using the Atlassian MCP (Model Context Protocol).

## Prerequisites

- Python 3.6 or higher
- Atlassian JIRA Cloud account
- Atlassian API token

## Setup Instructions

### 1. Create Atlassian API Token

1. Log in to your Atlassian account at https://id.atlassian.com
2. Go to Security → Create and manage API tokens
3. Click "Create API token"
4. Give it a name (e.g., "MCP Connector")
5. Copy the generated token (you won't be able to see it again)

### 2. Configure the Connector

1. Copy the example configuration file:
   ```bash
   cp atlassian_config.json.example atlassian_config.json
   ```

2. Edit `atlassian_config.json` with your credentials:
   ```json
   {
     "jira_url": "https://yourcompany.atlassian.net",
     "api_token": "your-api-token-here",
     "email": "your-email@example.com",
     "project_key": "PROJ"
   }
   ```

   - **jira_url**: Your JIRA Cloud URL (e.g., `https://yourcompany.atlassian.net`)
   - **api_token**: The API token you created in step 1
   - **email**: Your Atlassian account email
   - **project_key**: (Optional) JIRA project key to filter bugs (e.g., `DEMO`, `PROJ`)

### 3. Run the Connector

```bash
python3 atlassian_mcp_connector.py
```

## Usage

The connector will:
1. Connect to the Atlassian MCP server
2. Fetch bugs from your JIRA Cloud instance
3. Display the bugs in the console
4. Save the bugs to `jira_bugs.json`

### Example Output

```
Connecting to Atlassian MCP at https://yourcompany.atlassian.net...
✓ Successfully connected to Atlassian MCP

Fetching bugs from JIRA Cloud...
JQL Query: issuetype = Bug AND project = DEMO ORDER BY created DESC
Max Results: 50
✓ Retrieved 2 bugs

================================================================================
BUGS RETRIEVED FROM JIRA CLOUD
================================================================================

1. [DEMO-123] Sample bug from JIRA Cloud
   Status: Open | Priority: High
   Assignee: user@example.com
   Created: 2025-11-10T00:00:00Z
   Description: This is a sample bug retrieved via Atlassian MCP...

2. [DEMO-124] Another critical bug
   Status: In Progress | Priority: Critical
   Assignee: developer@example.com
   Created: 2025-11-09T00:00:00Z
   Description: Critical bug that needs immediate attention...

✓ Bugs saved to jira_bugs.json
```

## Features

- **MCP Connection**: Establishes connection to Atlassian MCP server
- **Bug Fetching**: Retrieves bugs from JIRA Cloud using JQL (JIRA Query Language)
- **Filtering**: Optional filtering by project key
- **Export**: Saves bugs to JSON format for further processing
- **Display**: Pretty-printed console output

## Configuration Options

You can customize the behavior by modifying the configuration file:

- **jira_url**: Your JIRA Cloud instance URL
- **api_token**: Your Atlassian API token for authentication
- **email**: Your Atlassian account email
- **project_key**: Filter bugs by specific project (leave empty to fetch from all projects)

## Security Notes

- The `atlassian_config.json` file contains sensitive credentials and is excluded from git
- Never commit your API token to version control
- Use the `.example` file as a template only

## Troubleshooting

### "Configuration file not found" error
- Make sure you've copied `atlassian_config.json.example` to `atlassian_config.json`
- Ensure the file is in the same directory as the script

### "Authentication failed" error
- Verify your API token is correct
- Ensure your email matches your Atlassian account
- Check that your JIRA URL is correct (should end with `.atlassian.net`)

### No bugs returned
- Check that your project key is correct
- Verify you have bugs in your JIRA project
- Ensure your account has permission to view bugs in the project

## API Documentation

For more information about Atlassian APIs and MCP:
- [Atlassian REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [JIRA Query Language (JQL)](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)

## License

This project is for demonstration purposes.
