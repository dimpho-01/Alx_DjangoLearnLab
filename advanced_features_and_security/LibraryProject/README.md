# Permissions and Group Setup for LibraryProject

## Custom Permissions:
- `can_view` allows a user to view books.
- `can_create` allows a user to add new books.
- `can_edit` allows a user to modify existing books.
- `can_delete` allows a user to remove books.

## Groups:
- Editors: Can create and edit books.
- Viewers: Can only view books.
- Admins: Have all available permissions for full access.

## Applying Permissions in Views:
Permissions are enforced using the `@permission_required` decorator for function-based views or `PermissionRequiredMixin` for class-based views. Users required to be logged in, and a 403 Forbidden response is raised if the user lacks the permission.

## Testing:
Test the setup by creating user accounts for each group and attempting to perform actions as per their permissions.

----
# settings.py
- Configure security-related settings
- DEBUG set to False for production to prevent leak of sensitive data

# views.py
- Demonstrating use of ORM to prevent SQL injection
- Using Django forms for input validation and sanitation