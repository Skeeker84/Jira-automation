"""Some simple authentication examples."""

from __future__ import annotations

from collections import Counter
from typing import cast
from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue
from dotenv import load_dotenv
load_dotenv("/home/skeeter/python-projects/.env")
# Some Authentication Methods
jira = JIRA("https://versuch2.atlassian.net",
    basic_auth=("Jira_Admin", "Jira_PWD"),  
    # a username/password tuple [Not recommended]
    # basic_auth=("email", "API token"),  # Jira Cloud: a username/token tuple
    # token_auth="API token",  # Self-Hosted Jira (e.g. Server): the PAT token
    # auth=("admin", "admin"),  # a username/password tuple for cookie auth [Not recommended]
)

# Who has authenticated
myself = jira.myself()

# Get the mutable application properties for this server (requires
# jira-system-administrators permission)
props = jira.application_properties()

# Find all issues reported by the admin
# Note: we cast() for mypy's benefit, as search_issues can also return the raw json !
#   This is if the following argument is used: `json_result=True`
issues = cast(ResultList[Issue], jira.search_issues("assignee=admin"))

# Find the top three projects containing issues reported by admin
top_three = Counter([issue.fields.project.key for issue in issues]).most_common(3)
print(issues)