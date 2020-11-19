from ..source.figure import Figure
import pytest


class TestSquare:

    def test_perimeter(self):
        perimeter = Figure(name='square', angles=4, sideA=2, sideB=None).perimeter
        assert perimeter == 8

    def test_area(self):
        area = Figure(name='square', angles=4, sideA=2, sideB=None).area
        assert area == 4

    def test_add_area_square_circle(self):
        square = Figure(name='square', angles=4, sideA=2, sideB=None)
        circle = Figure(name='circle', angles=0, sideA=2, sideB=None)
        assert round(square.add_area(circle), 2) == 16.57

    @pytest.mark.parametrize('name', ['rectangle', 'triangle'])
    def test_add_area(self, name):
        square = Figure(name='square', angles=4, sideA=2, sideB=None)
        another_figure = Figure(name=name, angles=4, sideA=2, sideB=2)
        assert square.add_area(another_figure) > 1

    def test_comparison_of_perimeter_and_area(self):
        perimeter = Figure(name='square', angles=4, sideA=2, sideB=None).perimeter
        area = Figure(name='square', angles=4, sideA=2, sideB=None).area
        assert perimeter > area


class TestRectangle:

    def test_perimeter(self):
        perimeter = Figure(name='rectangle', angles=4, sideA=2, sideB=1).perimeter
        assert perimeter == 6

    def test_area(self):
        area = Figure(name='rectangle', angles=4, sideA=2, sideB=1).area
        assert area == 2

    def test_add_area_square_triangle(self):
        rectangle = Figure(name='rectangle', angles=4, sideA=2, sideB=1)
        triangle = Figure(name='triangle', angles=3, sideA=2, sideB=1)
        assert rectangle.add_area(triangle) == 3

    @pytest.mark.parametrize('name', ['square', 'circle'])
    def test_add_area(self, name):
        rectangle = Figure(name='rectangle', angles=4, sideA=2, sideB=1)
        another_figure = Figure(name=name, angles=4, sideA=2, sideB=2)
        assert rectangle.add_area(another_figure) > 1

    def test_comparison_of_perimeter_and_area(self):
        perimeter = Figure(name='rectangle', angles=4, sideA=2, sideB=1).perimeter
        area = Figure(name='rectangle', angles=4, sideA=2, sideB=1).area
        assert perimeter > area


class TestTriangle:

    def test_perimeter(self):
        perimeter = Figure(name='triangle', angles=3, sideA=2, sideB=1).perimeter
        assert round(perimeter, 2) == 5.24

    def test_area(self):
        area = Figure(name='triangle', angles=3, sideA=2, sideB=1).area
        assert area == 1

    def test_add_area_square_circle(self):
        triangle = Figure(name='triangle', angles=3, sideA=2, sideB=1)
        circle = Figure(name='circle', angles=0, sideA=2, sideB=None)
        assert round(triangle.add_area(circle), 2) == 13.57

    @pytest.mark.parametrize('name', ['square', 'rectangle'])
    def test_add_area(self, name):
        triangle = Figure(name='triangle', angles=3, sideA=2, sideB=1)
        another_figure = Figure(name=name, angles=4, sideA=2, sideB=2)
        assert triangle.add_area(another_figure) > 1

    def test_comparison_of_perimeter_and_area(self):
        perimeter = Figure(name='triangle', angles=4, sideA=2, sideB=1).perimeter
        area = Figure(name='triangle', angles=4, sideA=2, sideB=1).area
        assert perimeter > area


class TestCircle:

    def test_perimeter(self):
        perimeter = Figure(name='circle', angles=0, sideA=2, sideB=None).perimeter
        assert round(perimeter, 2) == 12.57

    def test_area(self):
        area = Figure(name='circle', angles=0, sideA=2, sideB=None).area
        assert round(area, 2) == 12.57

    def test_add_area_square_square(self):
        circle = Figure(name='circle', angles=0, sideA=2, sideB=None)
        square = Figure(name='square', angles=4, sideA=2, sideB=None)
        assert round(circle.add_area(square), 2) == 16.57

    @pytest.mark.parametrize('name', ['triangle', 'rectangle'])
    def test_add_area(self, name):
        circle = Figure(name='circle', angles=0, sideA=2, sideB=None)
        another_figure = Figure(name=name, angles=4, sideA=2, sideB=2)
        assert circle.add_area(another_figure) > 1

    def test_comparison_of_perimeter_and_area(self):
        perimeter = Figure(name='circle', angles=0, sideA=2, sideB=None).perimeter
        area = Figure(name='circle', angles=0, sideA=2, sideB=None).area
        assert perimeter == area
