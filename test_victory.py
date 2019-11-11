from victory import date_to_str


def test_date_to_str():
    date = ['26.06.1799', '12.02.1809', '04.06.1975']
    date_text = ['двадцать шестое июня 1799 года', 'двенадцатое февраля 1809 года', 'четвертое июня 1975 года']
    for i in range(len(date)):
        assert date_to_str(date[i]) == date_text[i]