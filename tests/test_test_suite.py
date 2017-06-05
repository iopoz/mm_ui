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
        # assert app.place_details.is_place_name_matched(env.place_name)
        # assert app.place_details.is_place_type_matched(env.place_type)
        # assert app.place_details.is_place_address_matched(env.place_street +', '+ env.place_home)
        # assert app.place_details.is_place_distance_existed()
        # assert app.place_details.is_place_direction_existed()

    def test_2(self, app, env, storage):
        app.place_details.open_place_details()
        storage.place_info = app.place_details.get_place_info()
        app.place_details.change_coordinate_type()
        assert app.place_details.is_coordinates_changed(storage.place_info['coordinate'])
        app.place_details.click_edit_place()

    def test_3(self, app, env, storage):
        assert app.editor.is_editor_opened()
        # app.editor.add_new_language(env.language, env.name_place_in_language)
        # app.editor.add_zip_code(env.place_zip)
        # assert app.editor.is_field_correct(storage.place_info['time'])
        # assert app.editor.is_field_correct(storage.place_info['phone'])
        # assert app.editor.is_field_correct(storage.place_info['site'])
        # assert app.editor.is_field_correct(storage.place_info['cuisine'])
        # app.editor.turn_wifi_on()
        # app.editor.scroll_to_editor_top()
        app.editor.edit_working_time(env.t_open, env.t_close)
        app.editor.edit_email(env.email)
        app.editor.add_cuisine(env.new_cuisine)



