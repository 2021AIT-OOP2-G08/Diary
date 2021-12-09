from diaries.AbstractDiary import AbstractDiary


class NaruseDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return """今日はオブ演で初めてのグループワークだった。リーダーになったので頑張りたい。"""

    def get_author(self):
        return "Naruse"