## Intro to Julia tutorial

> [Video](https://www.youtube.com/watch?v=8h8rQyEpiZA)

### 1. Why do we want another language?

#### The two language problem
- Performance (Fortran,C,asm) vs. Productive (Python,Ruby,Matlab)
- Classical workaround? use two languages (prototype + production)
- **Julia : "looks like Python, feels like Lisp and runs like C!"**
- Looks like Python:
```Python
# Python
def sum(a):
    s = 0.0
    for x in a:
        s+=x
    return s
```
```Julia
# Julia
function sum(a)
  s = 0.0
  for x in a
    s+=x
  end
  return s
end
```
### 2. Julia in practice
### 3. Tutorial!
