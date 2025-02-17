"""
Codigo para la adquisicion de datos de hotel y reservaciones
"""
import json
import os
import unittest
from typing import List, Dict


class Hotel:
    """
    Definicion de clase Hotel
    """
    def __init__(self, hotel_id: int, name: str, location: str,
                 rooms_available: int):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self) -> Dict:
        """
        Definicion de Dict
        """
        return {
            "id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms_available": self.rooms_available
        }

    def display_info(self) -> None:
        """
        Muestra la información del hotel.
        """
        print(f"Hotel ID: {self.hotel_id}")
        print(f"Nombre: {self.name}")
        print(f"Ubicación: {self.location}")
        print(f"Habitaciones disponibles: {self.rooms_available}")


def delete_hotel(hotels: List[Dict], hotel_id: int, file_path: str):
    """
    Definicion para detele hotel
    """
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    save_json_file(file_path, hotels)


def modify_hotel(hotels: List[Dict], hotel_id: int,
                 updated_info: Dict, file_path: str):
    """
    Definicion para modify hotel
    """
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel.update(updated_info)
            break
    save_json_file(file_path, hotels)


def reserve_room(hotels: List[Dict], hotel_id: int, file_path: str):
    """
    Definicion para reserve room
    """
    for hotel in hotels:
        if hotel["id"] == hotel_id and hotel["rooms_available"] > 0:
            hotel["rooms_available"] -= 1
            save_json_file(file_path, hotels)
            return "Reserva exitosa."
    return "No hay habitaciones disponibles."


def cancel_reservation(hotels: List[Dict], hotel_id: int, file_path: str):
    """
    Definicion para cancel reservation
    """
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["rooms_available"] += 1
            save_json_file(file_path, hotels)
            return "Reserva cancelada."
    return "Hotel no encontrado."


class Customer:
    """
    Definicion de clase  customer
    """
    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        """
        Definicion de metodo
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict:
        """
        Definicion de to dict
        """
        return {
            "id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    def display_info(self) -> None:
        """
        Muestra la informacion del cliente.
        """
        print(f"Cliente ID: {self.customer_id}")
        print(f"Nombre: {self.name}")
        print(f"Email: {self.email}")
        print(f"Telefono: {self.phone}")

def delete_customer(customers: List[Dict], customer_id: int,
                    file_path: str):
    """
    Definicion para delete customer
    """
    customers = [customer for customer in customers
                 if customer["id"] != customer_id]
    save_json_file(file_path, customers)


def modify_customer(customers: List[Dict], customer_id: int,
                    updated_info: Dict, file_path: str):
    """
    Definicion para modify customer
    """
    for customer in customers:
        if customer["id"] == customer_id:
            customer.update(updated_info)
            break
    save_json_file(file_path, customers)


class Reservation:
    """
    Definicion de clase reservation
    """
    def __init__(self, reservation_id: int, customer_id: int,
             hotel_id: int, dates: dict):
        """
        Definicion de metodo para la reservacion.
        """
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.check_in = dates.get('check_in', '')
        self.check_out = dates.get('check_out', '')

    def to_dict(self) -> Dict:
        """
        Definicion de to dict
        """
        return {
            "id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
            "check_in": self.check_in,
            "check_out": self.check_out
        }

    def display_reservation(self) -> None:
        """
        Muestra los detalles de la reservacion.
        """
        print(f"Reservacion ID: {self.reservation_id}")
        print(f"Cliente ID: {self.customer_id}")
        print(f"Hotel ID: {self.hotel_id}")
        print(f"Check-in: {self.check_in}")
        print(f"Check-out: {self.check_out}")


def cancel_reservation_entry(reservations: List[Dict],
                             reservation_id: int, file_path: str):
    """
    Definicion de cancel reservation entry
    """
    reservations = [reservation for reservation in reservations
                    if reservation["id"] != reservation_id]
    save_json_file(file_path, reservations)


def load_json_file(file_path: str) -> List[Dict]:
    """
    Definicion  de load json file
    """
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe.")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error al cargar {file_path}: {e}")
        return []


def save_json_file(file_path: str, data: List[Dict]):
    """
    Definicion de save json file
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error al guardar {file_path}: {e}")


class TestHotel(unittest.TestCase):
    """
    Definicion de clase Test hotel
    """
    def test_create_hotel(self):
        """
        Definicion de test create hotel
        """
        hotel = Hotel(1, "Hotel Playita", "Torreon", 10)
        self.assertEqual(hotel.to_dict()["name"], "Hotel Playita")


class TestCustomer(unittest.TestCase):
    """
    Definicion de clase testcustomer
    """
    def test_create_customer(self):
        """
        Definicionde test create customer
        """
        customer = Customer(1, "John Deere",
                            "Jonydeere@outlook.com", "1234567890")
        self.assertEqual(customer.to_dict()["email"], "Jonydeere@outlook.com")


class TestReservation(unittest.TestCase):
    """
    Definicion de clase testreservation
    """
    def test_create_reservation(self):
        """
        Definicion de test create reservation
        """
        dates = {"check_in": "2025-06-01", "check_out": "2025-06-10"}
        # Crear diccionario con fechas
        reservation = Reservation(1, 1, 1, dates)  # Pasar el diccionario como unico argumento
        self.assertEqual(reservation.to_dict()["check_in"], "2025-06-01")


def main():
    """
    Definicion  de main
    """
    hotels_file = input(
        "Ingrese el nombre del archivo que contiene los hoteles: "
    )
    customers_file = input(
        "Ingrese el nombre del archivo que contiene los clientes: "
    )
    reservations_file = input(
        "Ingrese el nombre del archivo que contiene las reservaciones: "
    )

    hotels = load_json_file(hotels_file)
    customers = load_json_file(customers_file)
    reservations = load_json_file(reservations_file)

    print(
        f"Se cargaron {len(hotels)} hoteles, {len(customers)} clientes "
        f"y {len(reservations)} reservas."
    )


if __name__ == "__main__":
    main()
    unittest.main()
