import sender_orders


def test_create_order():
    result = send_order_positive()


def send_order_positive(debug=False):
    create_result = sender_orders.create_order()
    track = create_result.json()["track"]
    if debug == True:
            print("Track number = "+str(track))
            print("Full answer = " + str(create_result.content))

    assert create_result.status_code == 201, "Order not created"
    get_order_result = sender_orders.get_order_by_track(track)
    assert get_order_result.status_code == 200, "Order not found"
