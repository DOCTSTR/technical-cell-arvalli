def get_user_role(user):
    """
    Returns role string based on Django auth:
    ADMIN  -> superuser
    OFFICER -> user in OFFICER group
    VIEWER -> default
    """

    if user.is_superuser:
        return "ADMIN"

    try:
        groups = user.groups.values_list("name", flat=True)
    except Exception:
        return "VIEWER"

    if "OFFICER" in groups:
        return "OFFICER"

    return "VIEWER"
