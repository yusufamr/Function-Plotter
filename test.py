import pytest
import Plotter


@pytest.fixture
def app(qtbot):
    test_app = Plotter.Ui_MainWindow()
    return test_app

@pytest.mark.parametrize("value, valid", [
    ('x%2', False), ('x^2 + x&2', False), ('x*y', False),
    ('x^2 + 2/x + x*4', True), ( '3*x^4 - 3*x + 5', True),
    ('', False)
])
def test_PlotterFunction(app, qtbot, value, valid):
    app.TE_function.setText(value)
    assert app.FunctionCheck() == valid

@pytest.mark.parametrize("value, valid", [
    ('10' , True ) , ('-5', True ), ('0' , True ),
    ('' , False), ('$%' , False) , ('57%' , False)
])
def test_xMin(app, qtbot, value, valid):
    app.TE_xMin.setText(value)
    assert app.checkMinMax(app.TE_xMin.toPlainText(),"Min") == valid


@pytest.mark.parametrize("value, valid", [
    ('10' , True ) , ('-5', True ), ('0' , True ),
    ('' , False), ('$%' , False) , ('57B' , False)
])
def test_xMax(app, qtbot, value, valid):
    app.TE_xMax.setText(value)
    assert app.checkMinMax(app.TE_xMax.toPlainText(),"Max") == valid