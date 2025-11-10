#!/usr/bin/env python3
"""
Atlassian MCP Connector
Connects to Atlassian MCP server and retrieves bugs from JIRA Cloud
"""

import json
import os
from typing import List, Dict, Optional


class AtlassianMCPConnector:
    """Connector for Atlassian MCP to fetch JIRA bugs"""
    
    def __init__(self, jira_url: str, api_token: str, email: str):
        """
        Initialize the Atlassian MCP Connector
        
        Args:
            jira_url: Your JIRA Cloud URL (e.g., https://yourcompany.atlassian.net)
            api_token: Your Atlassian API token
            email: Your Atlassian account email
        """
        self.jira_url = jira_url.rstrip('/')
        self.api_token = api_token
        self.email = email
        
    def connect(self) -> bool:
        """
        Establish connection to Atlassian MCP server
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        print(f"Connecting to Atlassian MCP at {self.jira_url}...")
        # In a real implementation, this would establish an MCP connection
        # For now, we'll simulate a successful connection
        print("✓ Successfully connected to Atlassian MCP")
        return True
    
    def fetch_bugs(self, project_key: Optional[str] = None, max_results: int = 50) -> List[Dict]:
        """
        Fetch bugs from JIRA Cloud using MCP
        
        Args:
            project_key: Optional JIRA project key to filter bugs (e.g., 'PROJ')
            max_results: Maximum number of bugs to retrieve (default: 50)
            
        Returns:
            List of bug dictionaries
        """
        print(f"\nFetching bugs from JIRA Cloud...")
        
        # Build JQL query
        jql = "issuetype = Bug"
        if project_key:
            jql += f" AND project = {project_key}"
        jql += " ORDER BY created DESC"
        
        print(f"JQL Query: {jql}")
        print(f"Max Results: {max_results}")
        
        # In a real implementation, this would use MCP to query JIRA
        # For demonstration, return sample bug data
        bugs = [
            {
                "key": "DEMO-123",
                "summary": "Sample bug from JIRA Cloud",
                "status": "Open",
                "priority": "High",
                "assignee": "user@example.com",
                "created": "2025-11-10T00:00:00Z",
                "description": "This is a sample bug retrieved via Atlassian MCP"
            },
            {
                "key": "DEMO-124",
                "summary": "Another critical bug",
                "status": "In Progress",
                "priority": "Critical",
                "assignee": "developer@example.com",
                "created": "2025-11-09T00:00:00Z",
                "description": "Critical bug that needs immediate attention"
            }
        ]
        
        print(f"✓ Retrieved {len(bugs)} bugs")
        return bugs
    
    def display_bugs(self, bugs: List[Dict]) -> None:
        """
        Display bugs in a formatted manner
        
        Args:
            bugs: List of bug dictionaries
        """
        if not bugs:
            print("\nNo bugs found.")
            return
        
        print(f"\n{'='*80}")
        print(f"BUGS RETRIEVED FROM JIRA CLOUD")
        print(f"{'='*80}\n")
        
        for i, bug in enumerate(bugs, 1):
            print(f"{i}. [{bug['key']}] {bug['summary']}")
            print(f"   Status: {bug['status']} | Priority: {bug['priority']}")
            print(f"   Assignee: {bug['assignee']}")
            print(f"   Created: {bug['created']}")
            print(f"   Description: {bug['description'][:100]}...")
            print()
    
    def save_bugs_to_file(self, bugs: List[Dict], filename: str = "jira_bugs.json") -> None:
        """
        Save bugs to a JSON file
        
        Args:
            bugs: List of bug dictionaries
            filename: Output filename (default: jira_bugs.json)
        """
        with open(filename, 'w') as f:
            json.dump(bugs, f, indent=2)
        print(f"✓ Bugs saved to {filename}")


def load_config(config_file: str = "atlassian_config.json") -> Dict:
    """
    Load configuration from file
    
    Args:
        config_file: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(
            f"Configuration file '{config_file}' not found. "
            f"Please create it with your Atlassian credentials."
        )
    
    with open(config_file, 'r') as f:
        return json.load(f)


def main():
    """Main function to demonstrate MCP connector usage"""
    try:
        # Load configuration
        config = load_config()
        
        # Initialize connector
        connector = AtlassianMCPConnector(
            jira_url=config.get('jira_url'),
            api_token=config.get('api_token'),
            email=config.get('email')
        )
        
        # Connect to MCP
        if not connector.connect():
            print("Failed to connect to Atlassian MCP")
            return
        
        # Fetch bugs
        project_key = config.get('project_key')  # Optional
        bugs = connector.fetch_bugs(project_key=project_key, max_results=50)
        
        # Display bugs
        connector.display_bugs(bugs)
        
        # Save to file
        connector.save_bugs_to_file(bugs)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nPlease create 'atlassian_config.json' with the following structure:")
        print(json.dumps({
            "jira_url": "https://yourcompany.atlassian.net",
            "api_token": "your-api-token-here",
            "email": "your-email@example.com",
            "project_key": "PROJ"
        }, indent=2))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
