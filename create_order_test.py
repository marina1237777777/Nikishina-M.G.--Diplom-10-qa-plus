import sender_stand_request


def test_get_order_by_track():
    track = sender_stand_request.post_new_order()
    response = sender_stand_request.get_new_order_track(track)
    assert response.status_code == 200
