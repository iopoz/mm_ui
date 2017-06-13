import pytest


@pytest.yield_fixture(scope='session', autouse=True)
def init(app, env, storage):
    print('SetUP')
    storage.log = ''
    storage.log += app.enter_2_app.first_enter()
    if app.first_enter:
        app.navigate.navigate_to_my_place()
        app.enter_2_app.download_maps()
        app.navigate.go_to_search()
        app.search.search_place_by_coordinates(env.msk_center)
        app.enter_2_app.download_maps()
        assert app.place_details.is_place_details_shown()
        if not app.place_details.is_place_known():
            app.place_details.download_map()
        app.navigate.clear_search_results()
    storage.log += app.navigate.get_my_coordinate()
    app.navigate.hide_bottom_menu()

    yield (storage)  # everything after 'yield' is executed on tear-down
    print(storage.log)
    with open('log.txt', 'w') as file:
        file.write(storage.log)


class TestTestTask:
    def test_0(self, app, env, storage):
        app.navigate.go_to_search()
        storage.log += app.search.open_category_by_name(env.category)
        storage.log += app.search.open_place_by_name_address(env.place_name, env.place_street + ', ' + env.place_home)

    def test_1(self, app, env, storage):
        assert app.place_details.is_place_details_shown()
        assert app.place_details.is_arrow_up()
        storage.log += 'arrow is up \n'
        assert app.place_details.is_place_name_matched(env.place_name)
        storage.log += 'name is matched \n'
        assert app.place_details.is_place_type_matched(env.place_type)
        storage.log += 'type is matched \n'
        assert app.place_details.is_place_address_matched(env.place_street + ', ' + env.place_home)
        storage.log += 'address is matched \n'
        assert app.place_details.is_place_distance_existed()
        storage.log += 'distance exist \n'
        assert app.place_details.is_place_direction_existed()
        storage.log += 'direction exist \n'

    def test_2(self, app, env, storage):
        app.place_details.open_place_details()
        storage.place_info = app.place_details.get_place_info()
        app.place_details.change_coordinate_type()
        assert app.place_details.is_coordinates_changed(storage.place_info['coordinate'])
        app.place_details.click_edit_place()

    def test_3(self, app, env, storage):
        assert app.editor.is_editor_opened()
        storage.log += app.editor.add_new_language(env.language, env.name_place_in_language)
        storage.log += app.editor.add_zip_code(env.place_zip)
        assert app.editor.is_field_correct(storage.place_info['time'])
        assert app.editor.is_field_correct(storage.place_info['phone'])
        assert app.editor.is_field_correct(storage.place_info['site'])
        assert app.editor.is_field_correct(storage.place_info['cuisine'])
        storage.log += storage.place_info['coordinate'] + '\n'
        storage.log += storage.place_info['time'] + '\n'
        storage.log += storage.place_info['phone'] + '\n'
        storage.log += storage.place_info['site'] + '\n'
        storage.log += storage.place_info['cuisine'] + '\n'

        storage.log += app.editor.turn_wifi_on()
        app.editor.scroll_to_editor_top()
        storage.log += app.editor.edit_working_time(env.t_open, env.t_close)
        storage.log += app.editor.edit_email(env.email)
        storage.log += app.editor.add_cuisine(env.new_cuisine)
        app.navigate.save_changes()
        assert app.navigate.is_system_message_shown()
        app.navigate.cancel_system_message()
        app.navigate.back_to_map()
        assert app.place_details.is_place_details_shown()
        storage.log += 'user came back to the map'
