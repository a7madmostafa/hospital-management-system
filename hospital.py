
import csv
from datetime import datetime

class Person:
    def __init__(self, person_id, name, age, gender):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        return f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Patient(Person):
    def __init__(self, person_id, name, age, gender, disease):
        super().__init__(person_id, name, age, gender)
        self.disease = disease

    def display_info(self):
        return super().display_info() + f", Disease: {self.disease}"

class Doctor(Person):
    def __init__(self, person_id, name, age, gender, specialty):
        super().__init__(person_id, name, age, gender)
        self.specialty = specialty

    def display_info(self):
        return super().display_info() + f", Specialty: {self.specialty}"

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def display_info(self):
        return f"Appointment ID: {self.appointment_id}\nDate: {self.date}\nPatient: {self.patient.name}\nDoctor: {self.doctor.name}"

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def create_appointment(self, appointment):
        self.appointments.append(appointment)

    def list_patients(self):
        return [p.display_info() for p in self.patients]

    def list_doctors(self):
        return [d.display_info() for d in self.doctors]

    def list_appointments(self):
        return [a.display_info() for a in self.appointments]

    def export_patients_to_csv(self, filename="patients.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Gender", "Disease"])
            for p in self.patients:
                writer.writerow([p.person_id, p.name, p.age, p.gender, p.disease])

    def export_doctors_to_csv(self, filename="doctors.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Gender", "Specialty"])
            for d in self.doctors:
                writer.writerow([d.person_id, d.name, d.age, d.gender, d.specialty])

    def export_appointments_to_csv(self, filename="appointments.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Appointment ID", "Date", "Patient ID", "Patient Name", "Doctor ID", "Doctor Name"])
            for a in self.appointments:
                writer.writerow([a.appointment_id, a.date, a.patient.person_id, a.patient.name, a.doctor.person_id, a.doctor.name])
