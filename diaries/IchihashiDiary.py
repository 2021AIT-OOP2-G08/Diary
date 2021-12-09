from diaries.AbstractDiary import AbstractDiary

class IchihashiDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return 'Githubについて大まかな内容を学んだ'

    def get_author(self):
        return 'Ichihashi'