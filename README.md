# life_game_updated

раскрасить клетку - ПКМ<br />
передвижение по полю - ЛКМ + движение мышью в нужную сторону<br />
запустить/остановить игру - q<br />
приблизить - 1<br />
отдалить - 2<br />
ход назад - z<br />
ход вперед - x<br />
<br />
-----------для копающихся в коде---------<br />
points - координаты точек<br />
frames_for_wait (1..+inf) скорость обновления<br />
<br />
func drawing:<br />
test_camera_draw() - сетка<br />
screen.fill((0, 0, 0)) - цвет фона<br />
<br />
func draw_cells - 62 строка цвет клетки<br />
history_mode (True- вкл, False- выкл) позволяет перематывать ходы <br />
<br />
1th_demention :<br />
одномерные клеточные автоматы<br />
оригинальная идея принадлежит https://github.com/MrPr0per <br />
<br />
ПКМ - увеличить правило на 1 <br />
ЛКМ - уменьшить правило на 1 <br />
колесико - сменить сид генерации<br />
s - записать правило и сид в файл<br />
1 - уменьшить масштаб<br />
2 - увеличить масштаб<br />
