from diaries.AbstractDiary import AbstractDiary

class TogawaDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return '途中から授業に置いてかれた…'

    def get_author(self):
        return 'Togawa'