# :chart_with_upwards_trend: Simplex-Method

## About

This project aims to solve the Travelling Salesman Problem for the Linear Programming class using an algorithm that implements the Simplex method with the Big M variation.

## The Travelling Salesman Problem

A salesman needs to make sales in some cities in the State of Minas Gerais (Brazil): 
- Belo Horizonte
- Governador Valadares
- Juiz de Fora
- Montes Claros
- Uberlândia

His path will start in Belo Horizonte.

To minimize travel costs, the salesman needs to establish the best route for circulation between cities.

The displacement between cities will be carried out by road transport. 

### Thus, the costs of tickets between cities were collected:
|                          | Belo Horizonte  |Governador Valadares   |  Juiz de Fora | Montes Claros  | Uberlândia  |
|  :---------:             | :---------:     | :---------:           | :---------:   |    :---------: | :---------: |
| **Belo Horizonte**       |     -           | 63.60                 | 53.20         | 90.40          | 159.40      |
| **Governador Valadares** |      63.60      | -                     | 90.80         | 106.8          | 169.40      |
| **Juiz de Fora**         |    53.20        |  90.80                | -             | 135.40         | 157,60      |
| **Montes Claros**        |    90.40        |        106.8          | 135.40        | -              | 125.40      |
| **Uberlândia**           |   159.40        | 169.40                | 157,60        | 125.40         | -           |
> Symmetric matrix 

The traveling salesman needs to establish a route that allows him to visit all the cities only once at the lowest cost of transfer and at the end, return to the initial city. 

## Technologies

- [Python](https://www.python.org)


## Requirements

To run and edit the project, be sure to have installed in your computer the following softwares:

- [Python](https://www.python.org/downloads/)
- A code editor

After that, you'll need to clone this repo:

```
git clone https://github.com/eppica/Simplex-Method.git
```

## Setup

Inside the project directory, [create a virtual environment](https://docs.python.org/3/library/venv.html) (venv)

At the ```cmd```, type:

```
python -m venv ./venv
```

After that you should see a venv directory.

To run commands using venv, go to ```Scripts``` directory inside ```venv```:
```
project
│   main.py
│   ...
└─── venv
     └─── Scripts
         │   activate
```
To use the virtual environment, run:

```
activate
```
Then, using the virtual environment, install the project requirements:

```
pip install -r requirements.txt
```

That will prevent you to install the libs in the local computer, and it will be available only on the project scope.  

## Editing

Whenever you install a new library, you need to update the ```requirements.txt``` file.

At the ```cmd```, run:
```
pip freeze > requirements.txt
```
## Running

### venv:
To see the project running, inside the virtual environment at ```cmd```, run:
```
python main.py
```

## :balance_scale: License

[MIT License](https://github.com/eppica/Simplex/blob/main/LICENSE)
