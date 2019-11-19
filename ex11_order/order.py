"""Order system."""


class OrderItem:
    """Order Item requested by a customer."""

    def __init__(self, customer: str, name: str, quantity: int, one_item_volume: int):
        """
        Constructor that creates an order item.

        :param customer: requester name.
        :param name: the name of the item.
        :param quantity: quantity that shows how many such items customer needs.
        :param one_item_volume: the volume of one item.
        """
        self.customer = customer
        self.name = name
        self.quantity = quantity
        self.one_item_volume = one_item_volume

    @property
    def total_volume(self) -> int:
        """
        Calculate and return total volume of the current order item.

        :return: Total volume (cm^3), int.
        """
        return self.quantity * self.one_item_volume


class OrderAggregator:
    """Algorithm of aggregating orders."""

    def __init__(self):
        """Initialize order aggregator."""

        self.order_items = []

    def add_item(self, item: OrderItem):
        """
        Add order item to the aggregator.

        :param item: Item to add.
        :return: None
        """
        self.order_items.append(item)

    def aggregate_order(self, customer: str, max_items_quantity: int, max_volume: int):
        """
        Create an order for customer which contains order lines added by add_item method.

        Iterate over added orders items and add them to order if they are for given customer
        and can fit to the order.

        :param customer: Customer's name to create an order for.
        :param max_items_quantity: Maximum amount on items in order.
        :param max_volume: Maximum volume of order. All items volumes must not exceed this value.
        :return: Order.
        """
        items = []
        current_quantity = 0
        current_volume = 0
        count = 0
        for item in self.order_items:
            if self.order_items[count].customer == customer:
                current_quantity += self.order_items[count].quantity
                current_volume += self.order_items[count].total_volume
                if max_items_quantity >= current_quantity:
                    if max_volume >= current_volume:
                        items.append(item)
            count += 1
        for item in items:
            self.order_items.remove(item)
        return Order(items)


class Order:
    """Combination of order items of one customer."""

    def __init__(self, order_items: list):
        """
        Constructor that creates an order.

        :param order_items: list of order items.
        """
        self.order_items = order_items
        self.destination = None

    @property
    def total_quantity(self) -> int:
        """
        Calculate and return the sum of quantities of all items in the order.

        :return: Total quantity as int.
        """
        total = 0
        for item in self.order_items:
            total += item.quantity
        return total

    @property
    def total_volume(self) -> int:
        """
        Calculate and return the total volume of all items in the order.

        :return: Total volume (cm^3) as int.
        """
        total = 0
        for item in self.order_items:
            total += item.quantity * item.one_item_volume
        return total


class ContainerAggregator:
    """Algorithm to prepare containers."""

    def __init__(self, container_volume: int):
        """
        Initialize Container Aggregator.

        :param container_volume: Volume of each container created by this aggregator.
        """
        self.container_volume = container_volume
        self.not_used_orders = []

    def prepare_containers(self, orders: tuple) -> dict:
        """
        Create containers and put orders to them.

        If order cannot be put to a container, it is added to self.not_used_orders list.

        :param orders: tuple of orders.
        :return: dict where keys are destinations and values are containers to that destination with orders.
        """
        containers = {}
        #  c = Container(12, orders)
        #  containers["Tallinn"] = [c]
        #  c2 = Container(13, [orders[3]])
        #  containers["Tallinn"].append(c2)

        for order in orders:
            c = Container(self.container_volume, [order])
            d = order.destination
            if d not in containers:
                if order.total_volume <= self.container_volume:
                    containers[d] = []
                else:
                    self.not_used_orders.append(c)
                    break
            fits = False
            for c in containers[d]:
                if order.total_volume <= self.container_volume:
                    containers[d].append(c)
                    fits = True
                    if fits:
                        break
            if not fits:
                containers[d] = [c]
                containers[d].append(c)
        return containers


class Container:
    """Container to transport orders."""

    def __init__(self, volume, orders):
        """Initialize container"""
        self.volume = volume
        self.orders = orders

    @property
    def volume_left(self):
        """"Calculate the free volume left in the container"""
        total = 0
        for item in self.orders:
            total += item.total_volume
        return self.volume - total


if __name__ == '__main__':
    print("Order items")

    order_item1 = OrderItem("Apple", "iPhone 11", 100, 10)
    order_item2 = OrderItem("Samsung", "Samsung Galaxy Note 10", 80, 10)
    order_item3 = OrderItem("Mööbel 24", "Laud", 300, 200)
    order_item4 = OrderItem("Apple", "iPhone 11 Pro", 200, 10)
    order_item5 = OrderItem("Mööbel 24", "Diivan", 20, 200)
    order_item6 = OrderItem("Mööbel 24", "Midagi väga suurt", 20, 400)

    print(order_item3.total_volume)  # 60000

    print("Order Aggregator")
    oa = OrderAggregator()
    oa.add_item(order_item1)
    oa.add_item(order_item2)
    oa.add_item(order_item3)
    oa.add_item(order_item4)
    oa.add_item(order_item5)
    oa.add_item(order_item6)
    print(f'Added {len(oa.order_items)}(6 is correct) order items')

    order1 = oa.aggregate_order("Apple", 350, 3000)
    order1.destination = "Tallinn"
    print(f'order1 has {len(order1.order_items)}(2 is correct) order items')

    order2 = oa.aggregate_order("Mööbel 24", 325, 64100)
    order2.destination = "Tallinn"
    print(f'order2 has {len(order2.order_items)}(2 is correct) order items')

    print(f'after orders creation, aggregator has only {len(oa.order_items)}(2 is correct) order items left.')

    print("Container Aggregator")
    ca = ContainerAggregator(70000)
    too_big_order = Order([OrderItem("Apple", "Apple Car", 10000, 300)])
    too_big_order.destination = "Somewhere"
    containers = ca.prepare_containers((order1, order2, too_big_order))
    print(f'prepare_containers produced containers to {len(containers)}(1 is correct) different destination(s)')
    try:
        containers_to_tallinn = containers['Tallinn']
        print(f'volume of the container to tallinn is {containers_to_tallinn[0].volume}(70000 is correct) cm^3')
        print(f'container to tallinn has {len(containers_to_tallinn[0].orders)}(2 is correct) orders')
    except KeyError:
        print('Container to Tallinn not found!')
    print(f'{len(ca.not_used_orders)}(1 is correct) cannot be added to containers')
