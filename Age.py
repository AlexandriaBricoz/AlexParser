import random
class Human:
    __age = 0
    def info(self):
        print("set_age - вводит возраст\nget_age - выводит возраст\nmoi - вывод: привет")
    def __init__(self,a,b,z):
        if a > 0 and a<120:
            self.__age = a
        else:
            self.__age = 1
        self.__name = b
        self.zp = z
    def __Error(self):
        print('Вы ввели некоректное значение. Попробуйте ещё раз.')
    def set_age(self,a):
        while a<0:
            self.__Error()
            a = int(input())
        self.__age = a
        #return self._age
    def moi(self):
        return 'привет'
    def get_age(self):
        return self.__age
    def set_zp(self,a):
        self.zp = a
    def get_zp(self):
        return self.zp
    def set_name(self,a):
        self.__name = a
    def get_name(self):
        return self.__name

class Meneger(Human):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
class Cleaner(Human):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    # def info(self):
    #     pass
if __name__ == '__main__':
    wokers = []
    init = 1
    while init == 1 or init == 2 or init == 3:
        print('1-Желаете добавить сотрудника')
        print('2-Желаете изменить зарплату сотруднику')
        print('3-Вывод всех сотрудников')
        print(' -Выход')
        init = int(input())
        match init:
            case 1:
                print('  Желаете добавить менеджерa/уборщика(1/2)?')
                init2 = int(input())
                while (init2 != 1 and init2 != 2):
                    print('  Попробуйте ещё раз')
                    init2 = int(input())
                print('  Введите возраст, имя, зарплату:')
                if init2==1:
                    wokers.append(Meneger(int(input()),input(),int(input())))
                else:
                    wokers.append(Cleaner(int(input()), input(), int(input())))

            case 2:
                t = 0
                for f in wokers:
                    t = t + 1
                    print(t,' -  должность:',f.__class__.__name__, ' имя:', f.get_name(), ' зарплата:',f.get_zp())
                print(f'  Выберете сотруддника 1-{len(wokers)}')
                k = int(input())
                print('  Введите новую зарплату')
                wokers[k-1].set_zp(int(input()))
            case 3:
                t = 0
                for f in wokers:
                    t = t+1
                    print(t, ' -  должность:', f.__class__.__name__, ' имя:', f.get_name(),' возрст:',f.get_age(),'зарплата:', f.get_zp())
            case _:
                print('  До свидания')