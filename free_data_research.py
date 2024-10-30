import pandas as pd
import numpy as np

if __name__ == '__main__':
    #1. Download dataset .csv from kaggle
    data_research = pd.read_csv('Impact_of_Remote_Work_on_Mental_Health.csv')
    dataframe = pd.DataFrame(data_research)
    print(dataframe)
    print("Описательные характеристики для датафрейма: ")
    # 2. Описательные характеристики для датафрейма:
        # df.info() - показывает общую информацию о датафреме, включая:
            # - количество строк и столбцов
            # - тип данных в столбцах
            # - Непустые значения в каждом столбце (non-null count)
    print(dataframe.info())
        # df.describe() - показывает статистические характеристики для числовых столбцов
            # - Среднее значение(mean)
            # - Стандартное отклонение(std)
            # - Минимальное значение(min)
            # - Квартили(25 %, 50 %, 75 %)
            # - Максимальное значение(max)
            # - Количество непустых значений(count)
    print(dataframe.describe())
    # df.types - Выводит типы данных каждого столбца DataFrame.
    print(dataframe.dtypes)
    # df.shape - Возвращает кортеж, содержащий количество строк и столбцов DataFrame.
    print(dataframe.shape)
    # df.columns - Возвращает список названий столбцов DataFrame.
    print(dataframe.columns)
    # df.index - Возвращает индекс DataFrame (список меток для строк).
    print(dataframe.index)
    # df.nunique() - Возвращает количество уникальных значений в каждом столбце DataFrame.
    print(dataframe.nunique())
    # df.describe(include='all') -  который выводит информацию и о нечисловых данных.
    print(dataframe.describe(include='all'))
    # df.isnull().sum() - Выводит количество пустых значений в каждом столбце DataFrame.
    print(dataframe.isnull().sum())
    # 3. Какие срезы можно использовать для анализа данных?
        # Выбор строк по индексу
            # df.iloc[start:stop:step] - выбирает строки по позиционному индексу.
                # Start - начальный индекс (включительно)
                # stop - конечный индекс (не включительно)
                # step - шаг (по умолчанию 1)
    print(dataframe.iloc[1:4])  # Вывод строк с индексами 1, 2, 3
    print(dataframe.iloc[::2])  # Вывод каждой второй строки

        # Выбор строк по меткам
            # df.loc[start:stop:step] - выбирает строки по меткам.
                # Start - начальная метка (включительно)
                # stop - конечная метка (не включительно)
                # step - шаг (по умолчанию 1)
    print(dataframe.loc[1:4])  # Вывод строк с метками 1, 2, 3, 4

        # Выбор столбцов по имени:
            # df[column_name] - выбирает столбец по имени.
            # df[[column1, column2]] - выбирает столбцы по имени.
    print(dataframe['Gender'])  # Вывод столбца 'Gender'
    print(dataframe[['Gender', 'Age']])  # Вывод столбцов 'Gender' и 'Age'


        # Сочетание срезов - можно комбинировать срезы для выбора подмножеств DataFrame:
            # df[start:stop:step][column_name] - выбирает строку и столбец по позиционному индексу.
    print(dataframe.iloc[1:4]['Age'])  # Вывод столбца 'Age' для строк с индексами 1, 2, 3

        # Условные срезы - использование булевых масок для выбора строк, удовлетворяющих определенным условиям:
            # df[condition] - выбирает строки, удовлетворяющие условию.
    print(dataframe[dataframe['Age'] > 30])  # Вывод строк, удовлетворяющих условию 'Age' > 30

        # df[(condition1) & (condition2)] - выбирает строки, удовлетворяющие условию condition1 и condition2.
    print(dataframe[(dataframe['Age'] > 30) & (dataframe['Gender'] == 'Male')])

        # Изменение значений в DataFrame:
            #df.loc['c', 'A'] = 10  # Изменяем значение в ячейке строки 'c', столбца 'A' на 10
    dataframe.loc['c', 'A'] = 10
    print(dataframe)

        # Управление столбцами и строками DataFrame:
    dataframe.drop('Age', axis=1)  # Удаляем столбец 'Age'
    print(dataframe)
    dataframe.drop(['Age', 'Gender'], axis=1)  # Удаляем столбцы 'Age' и 'Gender'
    print(dataframe)

    # 4. Какую полезную информацию можно получить о данных,
    # используя отбор и фильтрацию?
    # Сформировать необходимый поднабор данных и проанализировать его.

        # Анализ подгрупп:
    employees_females = dataframe[dataframe['Gender']=='Female']
    print(employees_females)

        #Фильтрация по условиям
    employees_females_high_age = employees_females[employees_females['Age']>55]
    print(employees_females_high_age)

        # Группировка и агрегации
    print(employees_females.columns)
    work_experience_females = employees_females.groupby('Years_of_Experience')['Hours_Worked_Per_Week'].sum()
    print(work_experience_females)

        # Поиск выбросов
    # Определение выбросов, необычных значений в данных, которые могут искажать результаты анализа.
    Work_Life_Balance_Rating_mean = employees_females['Work_Life_Balance_Rating'].mean()
    Work_Life_Balance_Rating_std = employees_females['Work_Life_Balance_Rating'].std()
    Work_Life_Balance_Rating_outliers = employees_females[np.abs(employees_females['Work_Life_Balance_Rating']
                                                                 - Work_Life_Balance_Rating_mean) > 2 * Work_Life_Balance_Rating_std]
    # Выбросы  более  чем  на  2  стандартных  отклонения  от  среднего
    print(Work_Life_Balance_Rating_outliers) #вывод говорит о том, что таких выбросов нет

    # 5. Выполнить сортировку применительно к исследуемому набору данных
        # employees_females dataframe
    age_asc_experience_decs = employees_females.sort_values(by=['Age', 'Years_of_Experience'], ascending=[False, True])  #- сортировка по возрасту(по убыванию)
    # и затем по опыту работы(по возрастанию).
    print(age_asc_experience_decs)

    sorted_by = 'Work_Life_Balance_Rating'
    sort_by_Work_Life_Balance_Rating = employees_females.sort_values(by= sorted_by)
    print(sort_by_Work_Life_Balance_Rating[sorted_by])

    # 6. Потренироваться в переименовании колонок
    employees_females = employees_females.rename(columns={'A': 'Optional_column'})
    print(employees_females.columns)

    # 7. Проверить DataFrame на наличие пропущенных значений,
    # выбрать один из методов работы с пропусками и применить его;

    print(employees_females.isnull().sum())

    # 8. Проверить DataFrame на наличие дубликатов;
    print(employees_females.duplicated().sum())
    employees_females.drop_duplicates(inplace=True)
    print(employees_females)

    print(employees_females.duplicated(subset=['Employee_ID']))


    # 9. Сделать предположение, какой новый признак можно было бы ввести для исследуемого набора данных,
    # и реализовать его в созданном DataFrame.

    dataframe['Remote_Work_Experience'] = dataframe['Years_of_Experience'] * (dataframe['Work_Location'] == 'Remote').astype(int)
    print(dataframe['Remote_Work_Experience'])

    dataframe['Overall_Wellbeing'] = (dataframe['Work_Life_Balance_Rating'] + dataframe['Stress_Level'] + dataframe['Sleep_Quality'] + dataframe[
        'Satisfaction_with_Remote_Work']) / 4
    print(dataframe['Overall_Wellbeing'])




