import pytest


@pytest.yield_fixture(scope='session', autouse=True)
def init(app, env, storage):
    print('SetUP')
    storage.log = ''
    storage.log += app.enter_2_app.first_enter()
    if app.first_enter:
        app.navigate.go_to_search()
        app.search.search_place_by_coordinates(env.msk_center)


    yield (storage)  # everything after 'yield' is executed on tear-down
    print(storage.log)
    print('Tear-down')


class TestTestTask:
    def test_0(self, app, env):
        app.navigate.go_to_search()
        app.search.open_place_by_name_address(env.place_name, env.place_street +', '+ env.place_home)

    def test_1(self, app, env):
        assert app.place_details.is_place_details_shown()
        assert app.place_details.is_arrow_up()
        assert app.place_details.is_place_name_matched(env.place_name)
        assert app.place_details.is_place_type_matched(env.plase_type)
        assert app.place_details.is_place_address_matched(env.place_street +', '+ env.place_home)
        assert app.place_details.is_place_distance_existed()
        assert app.place_details.is_place_direction_existed()
        app.place_details.open_place_details()
