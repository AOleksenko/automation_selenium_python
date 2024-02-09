from support.base_methods import BaseMethods

# Buttons
btn_add = "//div[@title = 'Add']"
btn_save = "//div[@title = 'Save']"
btn_delete = "//div[@title = 'Clear']"
btn_clear_filter = "//div[@title = 'Clear All Filters']"
btn_discard_changes = "//div[@title = 'Discard changes']"
btn_export_all_data = "//div[@title = 'Export all data to Excel']"

# Fields
search_field = "//input[contains (@aria-label, 'Search in the data grid')]"

# Dialogs/windows/popups
win_confirmation = "//div[contains(@class,'dx-popup-normal')]"


class BaseElements(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)