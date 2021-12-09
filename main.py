from diaries.DiarySample import DiarySample
from diaries.KameiDiary import KameiDiary

diaries = [
    DiarySample().
    KameiDiary(),
]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
