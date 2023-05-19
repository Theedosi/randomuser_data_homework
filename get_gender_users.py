import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    f = 0
    m = 0
    x1 = []
    x = data['results']
    for i in x :
        x1.append(i['gender'])
        if i["gender"]== 'male':
            m = m + 1
        if i['gender']== 'female':
            f = f + 1
    dict = {
        'male' : m,
        'female': f
    }
    return dict
print(get_gender_users(get_data.data))
