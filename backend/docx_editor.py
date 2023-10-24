from docx import Document
from docx.shared import Pt
import os.path
from data.config import DOC_PATH, RES_PATH


def add_to_docx(name, sex, course, form_type, level, base, year):

    document = Document(f'{DOC_PATH}')

    if sex == 'Мужской':
        sex_1 = 'он'
        sex_2 = 'обучающимся'
        sex_3 = 'Зачислен'
    elif sex == 'Женский':
        sex_1 = 'она'
        sex_2 = 'обучающейся'
        sex_3 = 'Зачислена'
    else:
        sex_1 = '[ОШИБКА]'
        sex_2 = '[ОШИБКА]'
        sex_3 = '[ОШИБКА]'

    if form_type == 'Очная':
        form_type_1 = 'очной'
    elif form_type == 'Заочная':
        form_type_1 = 'заочной'
    elif form_type == 'Очно-заочная':
        form_type_1 = 'очно-заочной'
    else:
        form_type_1 = '[ОШИБКА]'

    if level == 'Магистратура':
        level_1 = 'магистратуры'
        level_2 = '40.04.01'
    elif level == 'Бакалавриат':
        level_1 = 'бакалавриата'
        level_2 = '40.03.01'
    else:
        level_1 = '[ОШИБКА]'
        level_2 = '[ОШИБКА]'

    if base == 'Бюджет':
        base_1 = 'бюджетной'
    elif base == 'Коммерция':
        base_1 = 'платной'
    else:
        base_1 = '[ОШИБКА]'

    if (level == 'Бакалавриат') and (year.isdigit()):
        if form_type == 'Очная':
            end = f"июль {int(year) + 4} года"
        else:
            end = f"15 июля {int(year) + 4} года"
    else:
        end = '_____________________________'

    if form_type in ('Очно-заочная', 'Заочная'):
        start_date = '01 ноября'
    else:
        start_date = '01 сентября'

    first_par = f"Выдана {name} в том, " \
                f"что {sex_1} является {sex_2} {course} курса {form_type_1} формы обучения " \
                "Высшей школы права ФГБОУ ВО " \
                "«Московский государственный юридический университет имени О.Е.\xa0Кутафина " \
                "(МГЮА)» и обучается по основной профессиональной образовательной программе " \
                f"высшего образования – программе {level_1} по направлению " \
                f"подготовки {level_2} Юриспруденция."

    sec_par = f'Обучается на {base_1} основе.'

    third_par = f'Начало обучения с {start_date} {year} года.'

    fourth_par = f'{sex_3} приказом от _______________ года №\xa0____.'

    fifth_par = f'Предполагаемый срок окончания обучения: {end}.'

    for p in document.paragraphs:
        if 'FIRST_PAR' in p.text:
            p.text = first_par
        elif 'SEC_PAR' in p.text:
            p.text = sec_par
        elif 'THIRD_PAR' in p.text:
            p.text = third_par
            p.style = document.styles['Normal']
        elif 'FOURTH_PAR' in p.text:
            p.text = fourth_par
        elif 'FIFTH_PAR' in p.text:
            p.text = fifth_par


    document.save(f'{RES_PATH}')

