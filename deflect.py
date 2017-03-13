#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import argparse
import argcomplete

import jira


def duplicate_issue(client, issue_id):
    issue = client.issue(issue_id)
    client.transition_issue(
        issue, 'Close Issue', resolution={'name': 'Duplicate'})


def ensure_duplicate(client, issue_id):
    while True:
        issue = client.issue(issue_id)
        if issue.fields.status in {'Reopened', 'Open'}:
            client.transition_issue(
                issue, 'Close Issue', resolution={'name': 'Duplicate'})
        time.sleep(10)


def _parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('jira_url')
    parser.add_argument('issue')
    parser.add_argument('--user-pwd', nargs=2)

    subparsers = parser.add_subparsers()
    cmd = subparsers.add_parser('dup')
    cmd.set_defaults(execute=duplicate_issue)

    cmd = subparsers.add_parser('dup4ever')
    cmd.set_defaults(execute=ensure_duplicate)

    argcomplete.autocomplete(parser)
    return parser.parse_args()


def main():
    args = _parse_cli()

    client = jira.JIRA(args.jira_url, basic_auth=args.user_pwd)
    args.execute(client, args.issue)


if __name__ == '__main__':
    main()
