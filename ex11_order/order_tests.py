import pytest
from order import Container
from order import ContainerAggregator
from order import Order
from order import OrderAggregator
from order import OrderItem

import pytest


@pytest.mark.timeout(1.0)
def test__container_aggregator__puts_orders_to_one_dest_container_if_possible():
    ca = ContainerAggregator(999999)
    order1 = Order([OrderItem("customer", "item1", 1, 1), OrderItem("customer", "item2", 1, 1)])
    order2 = Order([OrderItem("customer", "item1", 1, 1)])
    order3 = Order([OrderItem("customer5", "item1", 1, 1), OrderItem("customer3", "item2", 1, 1)])
    order4 = Order([OrderItem("customer", "item1", 1, 1)])
    order1.destination = "Tallinn"
    order2.destination = "Tallinn"
    order3.destination = "Tallinn"
    order4.destination = "Tallinn"
    orders = (order1, order2, order3, order4)

    containers = ca.prepare_containers(orders)

    assert len(containers) == 1
    assert containers['Tallinn'][0].orders == [order1, order2, order3, order4]


@pytest.mark.timeout(1.0)
def test__components_integration__create_containers_from_order_items__happy_case():
    orders_items = (
        OrderItem("Apple", "iPhone 11", 103, 10),
        OrderItem("Apple", "iPhone X", 41, 9),
        OrderItem("Tallink", "Laev", 1, 100000),  # too big
        OrderItem("Nike", "Sneakers", 244, 10),
        OrderItem("Nike", "Other ", 145, 11),
        OrderItem("Paper", "Paper", 1030, 5),
        OrderItem("Apple", "Apple TV", 12, 5),
        OrderItem("???", "___", 235, 10),
    )

    oa = OrderAggregator()
    for oi in orders_items:
        oa.add_item(oi)

    apple_orders_quantity = 103 + 41
    apple_orders_volume = 103 * 10 + 41 * 9
    apple_order = oa.aggregate_order("Apple", apple_orders_quantity, apple_orders_volume)
    apple_order.destination = "Somewhere"
    nike_order_quantity_with_buffer = 244 + 145 + 10
    nike_order_volume_with_buffer = 244 * 10 + 145 * 11 + 99
    nike_order = oa.aggregate_order("Nike", nike_order_quantity_with_buffer, nike_order_volume_with_buffer)
    nike_order.destination = "Neverland"

    volume = 244 * 10 + 145 * 11
    ca = ContainerAggregator(volume)
    containers = ca.prepare_containers((nike_order, apple_order))

    assert apple_order.total_quantity == apple_orders_quantity
    assert apple_order.total_volume == apple_orders_volume
    assert apple_order.order_items == [orders_items[0], orders_items[1]]

    assert nike_order.total_quantity == 244 + 145
    assert nike_order.total_volume == 244 * 10 + 145 * 11
    assert nike_order.order_items == [orders_items[3], orders_items[4]]

    assert len(containers) == 2
    somewhere_containers = containers['Somewhere']
    assert len(somewhere_containers) == 1
    assert somewhere_containers[0].volume == volume
    assert somewhere_containers[0].orders == [apple_order]

    neverland_containers = containers['Neverland']
    assert len(neverland_containers) == 1
    assert neverland_containers[0].volume == volume
    assert neverland_containers[0].orders == [nike_order]
