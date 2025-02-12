# Crossy Road Clone

## Опис
Crossy Road Clone е игра инспирирана од популарната игра Crossy Road, развиена користејќи ја Python Pygame библиотеката. Играчот треба да премине низ различни терени (пат, река, трева) избегнувајќи пречки и собирајќи монети.

## Карактеристики
- 3 играчки карактери за избор
- 5 прогресивно потешки нивоа
- Различни типови на терен (пат, река, трева)
- Систем за поени преку собирање монети
- Прикажување на време и поени
- Можност за рестартирање на играта
- Избор на карактер од почетното мени

## Имплементација

### Структура на играта
Играта е изработена користејќи објектно-ориентиран пристап со следните главни класи:

```python
class Player:
    # Контролира движење на играчот и детекција на судири
    
class Car:
    # Управува со пречки од возила
    
class Log:
    # Контролира платформи за пловење во реките
    
class Coin:
    # Предмети за собирање поени
    
class Character:
    # Управува со различни ликови за играње
```

### Механика на играта
- Движење со копчињата со стрелки
- Детекција на судири со автомобили
- Механика за пловење на трупци
- Собирање монети за поени
- Прогресија низ нивоа

### Нивоа
Играта содржи 5 нивоа со различни конфигурации на терен и зголемена тежина:
- Ниво 1: Основно ниво за запознавање со механиките
- Ниво 2-4: Прогресивно потешки нивоа
- Ниво 5: Финално предизвикувачко ниво

## Контроли
- **↑**: Движење нагоре
- **←**: Движење лево
- **→**: Движење десно


## Зависности
- Pygame 2.x
- Python 3.x
- Системски фонтови (bahnschrift, berlinsansfb)


## Изработиле
- Мила Стаматовска 223057
- Јована Силјановска 221021 


---
*Забелешка: Оваа игра е креирана за едукативни цели и е инспирирана од оригиналната Crossy Road игра.*
