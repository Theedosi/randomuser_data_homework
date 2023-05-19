import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    y = []
    x = data['results']
    for i in x :
        y.append(i["email"])
    return y
print(get_email(get_data.data))

