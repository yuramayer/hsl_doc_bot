
def vars_from_dict(d):
    name = d.get('name', '[ФИО]')
    sex = d.get('sex', '[ПОЛ]')
    course = d.get('course', '[КУРС]')
    student_type = d.get('type', '[ФОРМА_ОБУЧЕНИЯ]')
    level = d.get('level', '[УРОВЕНЬ_ОБРАЗОВАНИЯ]')
    base = d.get('base', '[ОСНОВА_ОБУЧЕНИЯ]')
    year = d.get('year', '[ГОД]')

    return name, sex, course, student_type, level, base, year


def get_address_from_level(level, course, type_):
    if level not in ('Бакалавриат', 'Магистратура'):
        address = '[ОШИБКА АДРЕСА: Обратитесь к Юре, @botrqst]'
        return address
    if course not in ('1', '2', '3', '4'):
        address = '[ОШИБКА АДРЕСА: Обратитесь к Юре, @botrqst]'
        return address
    if type_ not in ('Очно-заочная', 'Очная', 'Заочная'):
        address = '[ОШИБКА АДРЕСА: Обратитесь к Юре, @botrqst]'
        return address
    if level == 'Бакалавриат':
        if course in ('2', '3', '4'):
            address = 'evstarodubova@msal.ru'
            return address
    if level == 'Магистратура':
        if type_ in ('Очно-заочная', 'Заочная'):
            address = 'ivchekun@msal.ru'
            return address
    address = 'ebtolmacheva@msal.ru'
    return address
