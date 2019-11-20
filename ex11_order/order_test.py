import pytest
from order import Container
from order import ContainerAggregator
from order import Order
from order import OrderAggregator
from order import OrderItem


@pytest.mark.timeout(1.0)
def test__order_item__total_volume_is_correct():
    oi = OrderItem("customer", "item", 10, 20)

    assert oi.total_volume == 200


@pytest.mark.timeout(1.0)
def test__order__total_quantity_is_correct():
    o = Order([OrderItem("customer", "item", 2, 1), OrderItem("customer", "another item", 5, 1)])

    assert o.total_quantity == 7


@pytest.mark.timeout(1.0)
def test__order__has_destination_attribute_after_initialization():
    o = Order([OrderItem("customer", "item", 1, 1)])

    assert hasattr(o, 'destination')


@pytest.mark.timeout(1.0)
def test__order__total_volume_is_correct():
    o = Order([OrderItem("customer", "item", 4, 10), OrderItem("customer", "another item", 4, 30)])

    assert o.total_volume == 40 + 120


@pytest.mark.timeout(1.0)
def test__container__volume_left_is_correct_if_has_orders():
    orders = [Order([OrderItem("customer", "item1", 30, 5), OrderItem("customer", "item2", 3, 30)]),
              Order([OrderItem("customer", "item3", 20, 6)])]
    c = Container(1000, orders)

    assert c.volume_left == 1000 - (30 * 5 + 3 * 30 + 20 * 6)


@pytest.mark.timeout(1.0)
def test__container__volume_left_is_volume_if_no_orders():
    c = Container(300, [])

    assert c.volume_left == 300


@pytest.mark.timeout(1.0)
def test__order_aggregator__order_items_list_is_empty_after_creation():
    oa = OrderAggregator()

    assert len(oa.order_items) == 0


@pytest.mark.timeout(1.0)
def test__order_aggregator__order_item_is_added_to_list_after_calling_add_item():
    oa = OrderAggregator()
    item = OrderItem("customer", "item", 11, 1)

    oa.add_item(item)

    assert len(oa.order_items) == 1
    assert oa.order_items[0] is item


@pytest.mark.timeout(1.0)
def test__order_aggregator__all_order_items_are_in_the_list_if_add_item_is_called_multiple_times():
    oa = OrderAggregator()
    item1 = OrderItem("customer", "item", 11, 1)
    item2 = OrderItem("customer", "item2", 20, 4)

    oa.add_item(item1)
    oa.add_item(item2)

    assert len(oa.order_items) == 2
    assert oa.order_items[0] is item1
    assert oa.order_items[1] is item2


@pytest.mark.timeout(1.0)
def test__order_aggregator__aggregates_order_with_exact_capacity_and_quantity_for_customer():
    oa = OrderAggregator()
    item1 = OrderItem("customer", "item1", 1, 1)
    item2 = OrderItem("customer", "item2", 2, 2)
    oa.add_item(item1)
    oa.add_item(item2)

    order = oa.aggregate_order("customer", 3, 5)

    assert len(order.order_items) == 2
    assert order.order_items[0] is item1
    assert order.order_items[1] is item2


@pytest.mark.timeout(1.0)
def test__order_aggregator__ignores_other_customers_items_when_aggregating_order():
    oa = OrderAggregator()
    c1_item = OrderItem("customer1", "item1", 1, 1)
    c2_item = OrderItem("customer2", "item2", 2, 2)
    oa.add_item(c1_item)
    oa.add_item(c2_item)

    order = oa.aggregate_order("customer1", 3, 999999999999)

    assert len(order.order_items) == 1
    assert order.order_items[0] is c1_item

    assert len(oa.order_items) == 1
    assert oa.order_items[0] is c2_item


@pytest.mark.timeout(1.0)
def test__order_aggregator__ignores_next_item_if_max_items_quantity_is_exceeded():
    oa = OrderAggregator()
    item1 = OrderItem("customer", "item1", 1, 1)
    item2 = OrderItem("customer", "item2", 3, 2)
    oa.add_item(item1)
    oa.add_item(item2)

    order = oa.aggregate_order("customer", 3, 999999999999)

    assert len(order.order_items) == 1
    assert order.order_items[0] is item1

    assert len(oa.order_items) == 1
    assert oa.order_items[0] is item2


@pytest.mark.timeout(1.0)
def test__order_aggregator__ignores_next_item_if_max_items_volume_is_exceeded():
    oa = OrderAggregator()
    item1 = OrderItem("customer", "item1", 1, 1)
    item2 = OrderItem("customer", "item2", 2, 2)
    oa.add_item(item1)
    oa.add_item(item2)

    order = oa.aggregate_order("customer", 3, 2)

    assert len(order.order_items) == 1
    assert order.order_items[0] is item1

    assert len(oa.order_items) == 1
    assert oa.order_items[0] is item2


@pytest.mark.timeout(1.0)
def test__order_aggregator__order_item_is_removed_after_it_is_aggregated_to_order():
    oa = OrderAggregator()
    item1 = OrderItem("customer", "item1", 1, 1)
    item2 = OrderItem("customer", "item2", 2, 2)
    oa.add_item(item1)
    oa.add_item(item2)

    oa.aggregate_order("customer", 3, 5)

    assert len(oa.order_items) == 0


@pytest.mark.timeout(1.0)
def test__container_aggregator__correct_container_volume_is_assigned_and_not_used_orders_is_empty_list_after_creation():
    ca = ContainerAggregator(400)

    assert ca.container_volume == 400
    assert ca.not_used_orders == []


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
def test__container_aggregator__sets_correct_volume_to_new_container():
    ca = ContainerAggregator(999999)
    order1 = Order([OrderItem("customer", "item1", 1, 1), OrderItem("customer", "item2", 1, 1)])
    order2 = Order([OrderItem("customer", "item1", 1, 1)])
    order1.destination = "Tallinn"
    order2.destination = "Tallinn"
    containers = ca.prepare_containers((order1, order2))

    assert containers['Tallinn'][0].volume == 999999


@pytest.mark.timeout(1.0)
def test__container_aggregator__returns_two_containers_with_correct_orders_and_volume_if_has_orders_to_two_different_destination():
    ca = ContainerAggregator(999999)
    order1 = Order([OrderItem("customer", "item1", 1, 1), OrderItem("customer", "item2", 1, 1)])
    order2 = Order([OrderItem("customer", "item1", 1, 1)])
    order1.destination = "Tallinn"
    order2.destination = "Tokyo"

    containers = ca.prepare_containers((order1, order2))

    assert len(containers) == 2

    tallinn_containers = containers['Tallinn']
    assert len(tallinn_containers) == 1
    assert tallinn_containers[0].volume == 999999
    assert tallinn_containers[0].orders == [order1]

    tokyo_containers = containers['Tokyo']
    assert len(tokyo_containers) == 1
    assert tokyo_containers[0].volume == 999999
    assert tokyo_containers[0].orders == [order2]


@pytest.mark.timeout(1.0)
def test__container_aggregator__creates_new_container_if_order_does__not_fit_to_already_existing_container():
    ca = ContainerAggregator(50)
    order1 = Order([OrderItem("customer", "item1", 4, 5), OrderItem("customer", "item2", 1, 28)])
    order2 = Order([OrderItem("customer", "item3", 1, 1)])
    order3 = Order([OrderItem("customer", "item4", 10, 2)])
    order1.destination = "Tallinn"
    order2.destination = "Tallinn"
    order3.destination = "Tallinn"

    containers = ca.prepare_containers((order1, order2, order3))

    assert len(containers) == 1

    tallinn_containers = containers['Tallinn']
    assert len(tallinn_containers) == 2

    assert tallinn_containers[0].volume == 50
    assert tallinn_containers[0].orders == [order1, order2]

    assert tallinn_containers[1].volume == 50
    assert tallinn_containers[1].orders == [order3]


@pytest.mark.timeout(1.0)
def test__container_aggregator__puts_orders_that_cannot_be_added_to_container_to_not_used_orders_list():
    ca = ContainerAggregator(50)
    order1 = Order([OrderItem("customer", "item1", 4, 5), OrderItem("customer", "item2", 1, 28)])
    order_that_wont_fit = Order([OrderItem("customer", "item4", 10, 10)])
    order3 = Order([OrderItem("customer", "item4", 10, 2)])
    order1.destination = "Tallinn"
    order3.destination = "Tallinn"
    order_that_wont_fit.destination = "Tallinn"

    ca.prepare_containers((order1, order_that_wont_fit, order3))

    assert ca.not_used_orders == [order_that_wont_fit]


@pytest.mark.timeout(1.0)
def test__container_aggregator__does_not_add_dest_to_dict_if_no_containers_are_created():
    ca = ContainerAggregator(50)
    order_that_wont_fit = Order([OrderItem("customer", "item4", 10, 10)])
    order_that_wont_fit.destination = "Tallinn"

    containers = ca.prepare_containers((order_that_wont_fit,))

    assert containers == {}


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
