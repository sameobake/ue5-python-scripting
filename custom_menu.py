import unreal


def main():
    menus = unreal.ToolMenus.get()
    main_menu = menus.find_menu(unreal.Name('LevelEditor.MainMenu'))

    if not main_menu:
        unreal.log_error("""Failed to find the 'Main' menu. Something is wrong in the force!""")

    entry = unreal.ToolMenuEntry(
        name='Python.Tools',
        type=unreal.MultiBlockType.MENU_ENTRY,
        insert_position=unreal.ToolMenuInsert('', unreal.ToolMenuInsertType.FIRST)
    )
    entry.set_label(unreal.Text('Test Python Command'))
    entry.set_tool_tip(unreal.Text(''))
    entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON,
                             unreal.Name(''),
                             string='print("hello")'
                             )

    script_menu = main_menu.add_sub_menu(main_menu.get_name(),
                                         unreal.Name('PythonTools'),
                                         unreal.Name('Tool'),
                                         unreal.Text('CustomTools')
                                         )

    script_menu.add_menu_entry(unreal.Name('Scripts'), entry)

    # refresh the UI
    menus.refresh_all_widgets()


if __name__ == '__main__':
    main()
