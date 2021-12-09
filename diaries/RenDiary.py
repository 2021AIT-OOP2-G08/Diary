from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "授業スピードが早い。途中から混乱していた。"

    def get_author(self):
        return "Ren"