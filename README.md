# deflec2mat
  The way to win dev-qa wars.
  
  tired of trying to reject - duplicate jira issue's and qa reopen it just because they get insult by the reject.
  
  so use this project to automate the rejects.

## Examples
./deflect.py http://jira.company.com [issue id] --user-pwd [user] [password] deflect  # assigne the issue to some lucky person

./deflect.py http://jira.company.com [issue id] --user-pwd [user] [password] dup  # set issue as duplicate

./deflect.py http://jira.company.com [issue id] --user-pwd [user] [password] dup4ever  # set as duplicate and every time someone changed its status return it to duplicate
