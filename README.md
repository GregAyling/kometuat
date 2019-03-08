# Komet
This application allows the Kedron Scout Group to maintain their membership list.

## User Access Types

### Administrator
This user runs the whole show. They have full permissions. 

To create such a user, set the following values in the "Permissions" block:
  * Active: True
  * Staff status: True
  * Superuser status: True
  * Groups: (None)
  * User permissions: (None)

### Data Manager
This user is able to:
  * View all membership data
  * Update all membership data
  * Create new members

To create such a user, set the following values in the "Permissions" block:
  * Active: True
  * Staff status: True
  * Superuser status: False
  * Groups: "Data Managers"
  * User permissions: (None)

### Data Viewer
This user is able to:
  * View all membership data

To create such a user, set the following values in the "Permissions" block:
  * Active: True
  * Staff status: True
  * Superuser status: False
  * Groups: "Viewers"
  * User permissions: (None)