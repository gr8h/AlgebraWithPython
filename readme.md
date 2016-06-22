# Linear Algebra with Python

Linear algebra functions implemented in python.

## Getting Started

```
v1 = Vector([8.462, 7.893, -8.187])
w1 = Vector([6.984, -5.975, 4.778])

first_cross_product = v1.cross_product(w1)
print('cross product is: {}'.format(first_cross_product))

area_parallelogram = v1.area_of_parallelogram(w1)
print('area parallelogram is: {}'.format(round(area_parallelogram, 3)))

area_triangle = v1.area_of_triangle(w1)
print('area triangle is: {}'.format(round(area_triangle, 3)))
```
## License

NA
