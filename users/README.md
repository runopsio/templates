# Users Management Templates

A set of Runops Templates for delegating Runops users management to subgroups of an organization. This example uses squads as the subgroup, but can be adapted to any organization.

The goal is to enable team leaders to manage their teams' Runops users. Operations include users creation, removal, listing, and everything needed to reduce the overhead on users management from platform teams.

## `list.py`

Shows the total number of users from a team and the full list of users. The team is defined by the group with prefix `squad:` -- for instance: a user with the group `squad:payments` will see results only for users with the group `squad:payments`.

## `create.py`

Creates a new user for the team of the user executing the template. The team is defined by the group with prefix `squad:` -- for instance: a user with the group `squad:payments` will create a new user with the group `squad:payments`.

Inputs:
* `user_name`: The name of the user
* `user_email`: The email of the user. This is what links the user to the SSO provider. The user will only be able to signin to Runops after authenticating with this email.
* `user_role`: The value to be added as a group with prefix `meta_role:`. Example: for input: `developer`, the new user gets the group: `meta_role:developer`
