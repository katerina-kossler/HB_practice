"""Classes for melon orders."""
from random import randint


class AbstractMelonOrder():
    """An abstract melon order with overarching properties and methods."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Determines a random base melon price between $5 and $9"""

        base_price = randint(5, 9)
        return base_price
  
    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == 'Christmas melon':
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        """updates order with shipping fee if less than 10 melons shipped"""

        total = super().get_total()
        if self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government order that is tax-free and undergoes a security
       inspection"""

    order_type = 'government'
    tax = 0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed=None):
        """Records if order has passed security inspection"""

        if passed:
            self.passed_inspection = True
