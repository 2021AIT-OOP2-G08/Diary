from diaries.AbstractDiary import AbstractDiary

class KatoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"
    
    def get_summary(self):
        return """オブジェも結構めんどかったけどそれ以上に物理のレポートがきちい"""

    def get_author(self):
        return "Kato"