from datetime import datetime


def solution(today, terms, privacies):
    answer = []
    format = '%Y.%m.%d'
    today = datetime.strptime(today, format)

    table = {}
    for term in terms:
        record, month = term.split()
        table[record] = int(month)

    for i, priv in enumerate(privacies):
        sign_at, record_ = priv.split()

        sign_y, sign_m, sign_d = map(int, sign_at.split('.'))

        sign_m += table[record_]

        while sign_m > 12:
            sign_m -= 12
            sign_y += 1

        expired_at = datetime(year=sign_y, month=sign_m, day=sign_d)

        if expired_at <= today:
            answer.append(i + 1)

    answer.sort()
    return answer
