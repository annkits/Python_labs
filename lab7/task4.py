a = input("Комментарий: ")

if 'не ' in a:
    if 'не плохой' in a:
        a = a.replace("не плохой", "хороший")
    elif 'не плоха' in a:
        a= a.replace('не плоха', "хороша")
    elif 'не плохо' in a:
        a = a.replace('не плохо', 'хорошо')

print(a)