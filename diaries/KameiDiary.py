from diaries.AbstractDiary import AbstractDiary

class KameiDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-09"
    
    def get_summary(self):
        return "今日はオブジェクト指向プログラミング演習２のグループワーク演習だった。最高に楽しい"
    
    def get_author(self):
        return "Kamei"