# ***Geometric Lib***

## General description

The library has functions for calculating the **area** and **perimeter** for a *circle*, *rectangle*, *square* and *triangle*. A **description block** is written for each function, which describes in detail what the function does, the type and meaning of the values passed, and the type and meaning of the values returned.
To do this, **2 commits** were made in the personal branch on *creating functions for rectangle* and *creating functions for triangle with correcting the formula for calculating the perimeter of the rectangle*, respectively. 

>Git commands that were used
```
git clone https://github.com/spideydamn/geomtric_lib.git
git branch new_features_409942
git checkout new_features_409942
git add rectangle.py
git commit –m “feat: added rectangle.py”
git add triangle.py
git add rectangle.py
git commit -m "feat: added triangle.py; fix: corrected perimeter formula in rectangle.py
git log –graph --oneline
git --graph main..new_features_409942
git diff 7e43ac fb3857
git checkout main
git merge new_features_409942
git push origin new_features_409942
git branch –d new_features_409942
```


## Description of each function with call examples

1. **circle.py**
    - area
        Returns the area of ​​a circle with the given radius
        *Example:*
        arguments:
        r = 3
        return value:
        28.274333882308138
    - perimetr
        Returns the perimeter of a circle with the given radius
        *Example:*
        arguments:
        r = 3
        return value:
        18.84955592153876
2. **rectangle.py**
    - area
        Returns the area of ​​a rectangle with the given sides
        *Example:*
        arguments:
        a = 2, b = 4
        return value:
        12
    - perimetr
        Returns the perimeter of a rectangle with given sides
        *Example:*
        arguments:
        a = 2, b = 4
        return value:
        12
3. **square.py**
    - area
        Returns the area of ​​a square with the passed side
        *Example:*
        arguments:
        a = 2
        return value:
        4
    - perimetr
        Returns the perimeter of ​​a square with the passed side
        *Example:*
        arguments:
        a = 2
        return value:
        8
4. **triangle.py**
    - area
        Returns the area of ​​a triangle with the given height and base
        *Example:*
        arguments:
        a = 2, h = 3
        return value:
        3
    - perimetr
        Returns the perimeter of a triangle with given sides
        *Example:*
        arguments:
        a = 2, b = 3, c = 4
        return value:
        9


## Project change history with commit hashes (except for the last entry)

* *fb3857bacb20cb46833fe1187e5787db07dce83b* (HEAD -> new_features_409942, origin/new_features_409942, origin/main, origin/HEAD, main) feat: added triangle.py; fix: corrected perimeter formula in rectangle.py
* *7e43ac9e544c228e8f4347defb2621e536ea6eb6* feat: added rectangle.py
* *d078c8d9ee6155f3cb0e577d28d337b791de28e2* L-03: Docs added
* *8ba9aeb3cea847b63a91ac378a2a6db758682460* L-03: Circle and square added