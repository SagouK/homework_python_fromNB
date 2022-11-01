from statistics import mode
import calc_rational as ratio
import calc_complex as complex
import view
import logger as log



value = view.chose_mode()

if value == 1:
    def button_click(): # рациональные
        choice = 1
        while choice == 1:
            user_expresion = view.get_value()
            ratio.init(user_expresion)
            result = ratio.do_it(user_expresion)
            view.view_data(result, "Result")
            log.calc_logger(result, user_expresion)
            choice = view.close_app()
        else:
            print('Всего доброго!')
            quit()
else:
    def button_click(): # комплексные
        choice = 1
        while choice == 1:
            user_expresion = view.get_value()
            complex.init(user_expresion)
            result = complex.do_it(user_expresion)
            view.view_data(result, "Result")
            log.calc_logger(result, user_expresion)
            choice = view.close_app()
        else:
            print('Всего доброго!')
            quit()

