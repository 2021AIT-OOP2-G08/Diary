from diaries.DiarySample import DiarySample
from diaries.KameiDiary import KameiDiary
from diaries.NaruseDiary import NaruseDiary
from diaries.RenDiary import RenDiary
from diaries.HayasiDiary import HayasiDiary
from diaries.KatoDiary import KatoDiary
from diaries.IchihashiDiary import IchihashiDiary




# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  RenDiary(),
  KameiDiary(),
  NaruseDiary(),
  RenDiary(),
  HayasiDiary(),
  KatoDiary(),
  IchihashiDiary(),
  TogawaDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
