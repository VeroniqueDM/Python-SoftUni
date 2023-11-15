class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_worker_initialization_details(self):
        # Arrange + Act
        worker = Worker("Test Name", 100, 90)

        # Assert
        self.assertEqual("Test Name", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(90, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_energy_incrementation(self):
        # Arrange
        worker = Worker("Test Name", 100, 90)
        self.assertEqual(90, worker.energy)
        # Act
        worker.rest()
        # Assert
        self.assertEqual(91, worker.energy)

    def test_raising_error_for_work_without_energy(self):
        # Arrange
        worker = Worker("Test Name", 100, 0)

        # Act + Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_raising_error_for_work_negative_energy(self):
        # Arrange
        worker = Worker("Test Name", 100, -2)

        # Act + Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_salary_increase(self):
        # Arrange
        worker = Worker("Test Name", 100, 10)
        # Act
        self.assertEqual(0, worker.money)
        worker.work()
        # Assert
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_worker_energy_decrease_after_work(self):
        worker = Worker("Test Name", 100, 10)

        self.assertEqual(10, worker.energy)
        worker.work()
        self.assertEqual(9, worker.energy)

    def test_get_info_method(self):
        worker = Worker("Test Name", 100, 10)

        self.assertEqual('Test Name has saved 0 money.', worker.get_info())
        worker.work()
        self.assertEqual('Test Name has saved 100 money.', worker.get_info())
    
if __name__ == '__main__':
    main()