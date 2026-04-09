from dataclasses import dataclass, field


@dataclass
class ShoppingCart:
    owner: str
    items: list[str] = field(default_factory=list)


cart = ShoppingCart('John')
cart.items.append('apples')
print(cart)
