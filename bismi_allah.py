# بسم الله الرحمن الرحيم
# la ilaha illa Allah Mohammed Rassoul Allah

import flet as ft

# dikrDict("سبحان الله وبحمده", 100),
# dikrDict("أستغفر الله وأتوب إليه", 100),
# dikrDict("لا إلاه إلا الله وحده لا شريك له له الملك وله الحمد وهو على كل شيء قدير", 100),

def marra_or_marrat(number):
    if number in [1, 33, 100]:
        return "مرة"
    return "مرات"

def dikrDict(text, count):
    return {"text": text, "count": count}

favorite_dikr = [
    dikrDict("سبحان الله وبحمده", 100),
    dikrDict("أستغفر الله وأتوب إليه", 5),
    dikrDict("لا إلاه إلا الله وحده لا شريك له له الملك وله الحمد وهو على كل شيء قدير", 100),
    dikrDict("صلى الله على مخمد", 10),
]

morning_dikr = [
    dikrDict("آية الكرسي", 1),
    dikrDict("سبحان الله وبحمده", 100),
    dikrDict("أستغفر الله وأتوب إليه", 5),
    dikrDict("لا إلاه إلا الله وحده لا شريك له له الملك وله الحمد وهو على كل شيء قدير", 100),
    dikrDict("صلى الله على مخمد", 10),
]

adkar_lists_info = [
    {'name': 'المفضلة', 'icon': 'favorite', 'list': favorite_dikr},
    {'name': 'الصباح', 'icon': 'sunny', 'list': morning_dikr},
]

class Dikr(ft.Container):
    def __init__(self, dikr_dict):
        super().__init__()
        self.dikr_dict = dikr_dict
        self.dikr_count = 0
        self.progress_bar = ft.ProgressBar(value=(self.dikr_count / self.dikr_dict['count']))
        self.progress_label = ft.Text(str(self.dikr_dict['count']) + ' ' + marra_or_marrat(self.dikr_dict['count']), rtl=True)
        self.content = ft.Column(
            [
                ft.Text(dikr_dict['text']),
                self.progress_bar,
                self.progress_label,
            ],
        )
        def on_click(e):
            e.control.countUp()
        self.on_click = on_click

    def countUp(self):
        dikr_progress = (self.dikr_count / self.dikr_dict['count'])
        if dikr_progress >= 1:
            self.parent.next()
            return
        self.dikr_count += 1
        dikr_progress = (self.dikr_count / self.dikr_dict['count'])
        self.progress_bar.value = dikr_progress
        self.progress_label.value = (str(self.dikr_count) + ' - ' + str(self.dikr_dict['count']) + marra_or_marrat(self.dikr_dict['count']))
        if dikr_progress >= 1:
            self.parent.next()
            return
        self.update()

class DikrList(ft.Column):

    def __init__(self, dikr_list):
        super().__init__()
        self.expand=1
        self.dikr_list = [Dikr(dikr) for dikr in dikr_list]
        self.dikr_index = 0
        self.controls = [
            self.dikr_list[0],
            ft.Row(
                [
                    ft.ElevatedButton(text="previous dikr", on_click=DikrList.on_click_previous),
                    ft.ElevatedButton(text="next dikr", on_click=DikrList.on_click_next),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
        ]
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,

    def next(self):
        if self.dikr_index + 1 >= len(self.dikr_list):
            return
        self.dikr_index += 1
        self.controls[0] = self.dikr_list[self.dikr_index]
        self.update()

    def previous(self):
        if self.dikr_index <= 0:
            return
        self.dikr_index -= 1
        self.controls[0] = self.dikr_list[self.dikr_index]
        self.update()

    def on_click_next(e):
        e.control.parent.parent.next()

    def on_click_previous(e):
        e.control.parent.parent.previous()

class DikrListButton(ft.Container):
    def __init__(self, list_info):
        super().__init__()
        self.bg_color = '#eeeeee'
        # self.image = 
        self.content = ft.Column(
            [
                ft.Icon(list_info['icon']),
                ft.Text(list_info['name']),
            ]
        )
        self.dikr_list = list_info['list']
        def on_click(e):
            e.control.parent.parent.setDikrList(e.control.dikr_list)
        self.on_click = on_click


class AdkarListsButtons(ft.Column):
    def __init__(self, lists):
        super().__init__()

        self.controls = [DikrListButton(dikr_list) for dikr_list in lists]

class DikrApp(ft.Column):

    def __init__(self):
        super().__init__()

        self.adkar_lists_buttons = AdkarListsButtons(adkar_lists_info)

        def on_click(e):
            e.control.parent.goHome()

        self.counter = 0
        self.controls = [
            self.adkar_lists_buttons,
            ft.ElevatedButton(text="Home", on_click=on_click)
        ]

    def setDikrList(self, dikr_list):
        self.controls[0] = DikrList(dikr_list)
        self.update()

    def goHome(self):
        self.controls[0] = self.adkar_lists_buttons
        self.update()

def main(page):
    page.title = 'بسم الله الرحمن الرحيم'

    dikr_app = DikrApp()

    page.add(dikr_app)

ft.app(target=main)

