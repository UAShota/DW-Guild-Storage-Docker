"""
Help notices
"""

from .command_custom import DwgbCmdCustom, DwgbCmdConst
from ..classes import DwgbDatabase, DwgbTransport, DwgbMessage


class DwgbCmdHelp(DwgbCmdCustom):
    """ Команда подсказок """

    def __init__(self, database: DwgbDatabase, transport: DwgbTransport):
        """ Конструктор """
        super().__init__(database, transport)
        self.regHelp = self.getRegex(r"^(?:\[.+?\]|хочу) помощь")
        return

    def work(self, message: DwgbMessage):
        """ Обработка выражения """
        # Найдена просьба бафа
        if self.regHelp.match(message.text):
            return self.getHelp(message)
        # Ничего не найдено
        return False

    def getHelp(self, message: DwgbMessage):
        """ Отображение справки """
        tmp_text = ""
        tmp_text += "📦 https://vk.com/app7055214_-182985865\n"
        tmp_text += "🌐 Правила:\n"
        tmp_text += "👍🏻 нет оскорблений, треша\n"
        tmp_text += "👍🏻 нет тега Тирануса\n"
        tmp_text += "👍🏻 по неотложным проблемам [id66313242|Библиотекарь]"
        tmp_text += "🌐 Команды:\n"
        tmp_text += "🕶 хочу [количество] <полное или короткое имя предмета>\n"
        tmp_text += "🕶 хочу баф <атаки, защиты, удачи, человека> 🌕300\n"
        tmp_text += "🕶 хочу <чистыми, грязными> [o] <значение>\n"
        tmp_text += "🕶 хочу склад\n"
        tmp_text += "🕶 хочу цены\n"
        tmp_text += "🕶 хочу баланс\n"
        tmp_text += "🕶 хочу профиль\n"
        tmp_text += "🕶 газета <текст объявления> (100 символов)\n"
        tmp_text += "🕶 газета удалить\n"
        tmp_text += "🌐 Подсказки:\n"
        tmp_text += "💬 пополнение баланса - перевод предметов, золота, осколков на Марго\n"
        tmp_text += "💬 сохранение профиля - раз в три дня\n"
        tmp_text += "💬 продажа на склад %s%%, покупка - %s%% от цены\n" % (int(DwgbCmdConst.PERCENT_BUY * 100), int(DwgbCmdConst.PERCENT_SELL * 100))
        tmp_text += "🌐 Админка:\n"
        tmp_text += "🦖 склад кнопки\n"
        tmp_text += "🦖 склад обновить\n"
        tmp_text += "🦖 склад удалить <N>\n"
        tmp_text += "🦖 склад активность\n"
        tmp_text += "🦖 склад активность удалить <N>\n"
        tmp_text += "🦖 склад предмет <полное имя предмета> [-цена <N>] [-кол <N>] [-лим <N>] [-иконка <буква>] [-тег <слово>] [-сток <N>] [-доп <N>]\n"
        tmp_text += "🦖 склад процент <скупка> <продажа>\n"
        tmp_text += "🦖 склад цену [имя] [хорошо] [цена]\n"
        self.transport.writeChannel(tmp_text, message, False)
        # В любом случае операция успешна
        return True
