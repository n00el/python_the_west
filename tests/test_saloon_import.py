def test_saloon_import_does_not_require_plotting_stack():
    from the_west_inner.saloon import Quest

    assert Quest.__name__ == "Quest"
