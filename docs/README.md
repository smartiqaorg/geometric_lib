# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
<! -- 2. Смотрим текущее состояние репозитория  -->
$ git status
On branch main
Your branch is up to date with 'origin/main'.
Changes to be committed:
  modified:   docs/README.md
  

<! -- 3. Добавляем измененный файл в область Индекса  -->
$ git add docs/


<! -- 4. Делаем коммит  -->
$ git commit -m "G-06: README change for practice"
[main 6ebf072] G-06: README change for practice
 1 file changed, 3 insertions(+), 1 deletion(-)
 

<! -- 5. Смотрим список коммитов  -->
 $ git log
commit 6ebf0727741af6f30a9962ad6790f5acdb3e7582 (HEAD -> main)
Author: Smartiqa Git Course User <smartiqa.test@mail.ru>
Date:   Sun Nov 14 16:24:54 2021 +0300

    G-06: README change for practice

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
