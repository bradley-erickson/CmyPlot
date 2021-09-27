from plotting.utils.routes import navbar_toggle


def test_navbar_toggle():

    clicks = 0
    is_open = True
    expected = is_open
    output = navbar_toggle.__wrapped__(clicks, is_open)
    print(output)
    assert output == expected

    clicks += 1
    expected = not is_open
    output = navbar_toggle.__wrapped__(clicks, is_open)
    assert output == expected