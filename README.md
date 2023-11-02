# 7G-Network
## Конфигурация приложения config.py
### Размер окна
FPS = 30
### Размер окна
MINIMUM_SIDE_WINDOW = 600
### Кол-во ячеек по X
CELL_QTY_X = 100
### Кол-во ячеек по Y
CELL_QTY_Y = 100
### Процент препядствий на карте
PROCENT_CELL_BANNED = 30
### Радиус действия башни
RADIUS = 2

![2023-11-02_12-52-11](https://github.com/Zheny-mc/7G-Network/assets/68734109/b589fcd3-c53b-410e-bbb2-244720dd9a11)


![2023-11-02_12-51-19](https://github.com/Zheny-mc/7G-Network/assets/68734109/f9d5b172-d10e-4e3b-8f30-b1aa90b389fa)

Test assignment 
for the Junior Python Developer position


Imagine that a telecommunications company is working on designing an efficient 7G-network layout for a new city. The city can be represented as a grid, where some blocks are obstructed and cannot have towers, while others can. The goal is to provide the maximum coverage with the minimum number of towers.

Task 1: Grid Representation
Create a class CityGrid that can represent the city as an N x M grid. During the initialization of the class, obstructed blocks are randomly placed with coverage >30% (we can change this parameter).

Task 2: Tower Coverage
Each tower has a fixed range R (in blocks) within which it provides coverage. This coverage is a square, with the tower in the center.
Implement a method in the CityGrid class to place a tower and visualize its coverage.

Task 3: Optimization Problem
Design an algorithm to place the minimum number of towers such that all of non-obstructed blocks are within the coverage of at least one tower. The algorithm cannot place towers on obstructed blocks.
Implement a method in the CityGrid class to display the placement of towers.

Task 5: Visualization
Implement functions to visualize the CityGrid, including obstructed blocks, towers, coverage areas, and data paths.
Use any Python plotting library of your choice, such as matplotlib or seaborn.
