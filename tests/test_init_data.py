from the_west_inner.init_data import return_currency_data


def test_currency_parser_reads_current_initialization_shape():
    html = """
    <script>
    Player.init({"cash":146,"deposit":0,"upb":20,"nuggets":0,
                 "veteranPoints":0,"nested":{"cash":null}})
    </script>
    """

    assert return_currency_data(html) == {
        "cash": 146,
        "deposit": 0,
        "upb": 20,
        "nuggets": 0,
        "veteranPoints": 0,
    }
