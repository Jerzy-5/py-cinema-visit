# write your imports here
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    keys = []
    values = []
    lista = []
    counter = 0
    for custom in customers:
        for key, value in custom.items():
            if counter % 2 == 0:
                keys.append(value)
                counter += 1
            else:
                values.append(value)
                counter += 1

    slownik = dict(zip(keys, values))

    for key, value in slownik.items():
        lista.append(Customer(name=f"{key}", food=f"{value}"))

    for customer in lista:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    hall.movie_session(movie, lista, cleaner1)
