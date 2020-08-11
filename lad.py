if __name__ == "__main__":

    int('9900')
    int('42354')

    b = 10*50
    v = 8**8
    c = 100/10
    h = 100/45
    z = 80//9
    f = 80-50
    g = 50+70

    print(b, v, c, h, z, f, g)

days = { "days":"Понедельник\n" "вторник\n" "среда\n" "четверг\n" "пятница\n" "суббота \n" "воскресенье\n" }

print(days)

#

days2 = "\nДни недели:\n" "    Понедельник\n" "    Вторник\n" "    Среда\n"\
        "    Четверг\n" "    Пятница\n" "    Суббота\n" "    Воскресенье\n"

print(days2)

#

a = ' \t Пн\t вт\t среда\t четверг\t пятница\t суббота '

print(a)

#

one = 'asdasd / dgsdgd / eqtwre / bhdsgsdh / safsfasffsaf / asdqwfewf'
one2 = 'asdasd . gegw . assxxvr . ergregergre . geerger'
one3 = 'dasdger - dasfdsfasdsf - sfasfsafsfasfasfasfasf'
one4 = "dasdasdasd "
print( one.split('/'), one2.split('.'), one3.split('-'), one4   .split('/') )


pythons = {
'Chapman': 'Graham',
'Cleese': 'John',
'Gilliam': 'Terry',
'Idle': 'Eric',
'Jones': 'Terry',
'Palin': 'Michael',
 }

others = {
    'Marx': 'Groucho', 'Howard': 'Moe'
}

print(pythons.update(others))

print(pythons.clear())

print(pythons['Cleese'])