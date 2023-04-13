import logging
logging.basicConfig(level=logging.DEBUG)
from calculadora import calculadora
    
def test_calculadora_1(monkeypatch):
    def fake_input():
        val = next(answers)
        print(f'Inserting value: {val}')
        return val
    
    monkeypatch.setattr('builtins.input', lambda x: fake_input())
    
    answers = iter(["1", 'suma', "1", 'salir'])
    calculadora()
    
    answers = iter(['r', "1", 'suma', "1", 'salir'])
    calculadora()
    