from diaries.DiarySample import DiarySample
from diaries.KatoDiary import KatoDiary
from diaries.IchihashiDiary import IchihashiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  KatoDiary(),
  IchihashiDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()