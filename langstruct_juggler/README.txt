-------------------------------------- LangStruct Juggler intended for s.p.l.i.t game translation -----------------------------------------------
Author: Wollip
ver: 0.1

0) It is best to run both .bat batchers, first patch_in.bat, then patch_out.bat, to create the necessary file structure

1) Makes lang directory and necessary .txt files inside, if you don't have them

2) You have to input gamecode lines into the "rawstr.txt" file on each line, in order for script to work

3) You have to manually copy/paste all new batches from "eng.txt" to "ru.txt"(separate batches by AT LEAST 1 line)

4) How to use:
   - Run patch_in.bat and patch_out.bat
   - Paste each piece of code you intend to translate into the "lang/rawstr.txt" on each line
   - Run patch_in.bat, to convert "lang/rawstr.txt" lines to "en.txt" readable format
   - Ctrl+C all the necessary stuff from "lang/en.txt" to "lang/ru.txt"
   - Run patch_out.bat, to convert "lang/ru.txt" lines to "lang/ru_gamecode_lines.txt" gamecode format
   - Translated pieces of code are not on each line in "lang/ru_gamecode_lines.txt"

5) Enjoy :>

--------------------------------------- LangStruct Juggler созданный для перевода игры s.p.l.i.t ------------------------------------------------
Автор: Wollip
вер: 0.1

0) Лучше запустить оба .bat батчера, сначала patch_in.bat, потом patch_out.bat, для создания необходимой структуры

1) Создаёт lang папку с нелбходимыми .txt файлами внутри, если таковых нет

2) Вам нужно вставить необходимый для перевода игровой код в файл "rawstr.txt" на каждую линию, чтобы скрипт заработал

3) Вам нужно будет перенести вручную куски кода из "eng.txt" в "ru.txt"(оставьте между кусками ХОТЯ БЫ 1 линию)

4) Инструкции:
   - Запустить patch_in.bat и patch_out.bat
   - На каждую линию в "lang/rawstr.txt" вставьте по куску кода для перевода
   - Запустите patch_in.bat, чтобы конвертировать "lang/rawstr.txt" линии в читаемый формат в "en.txt"
   - Ctrl+C все нужные куски из "lang/en.txt" в "lang/ru.txt"
   - Запустите patch_out.bat, чтобы конвертировать "lang/ru.txt" линии обратно в формат кода в "lang/ru_gamecode_lines.txt"
   - Нужные переведённые куски теперь на каждой линии в "lang/ru_gamecode_lines.txt"

5) Наслаждайтесь :>