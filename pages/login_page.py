from pages.base_page import BasePage
from config import BASE_URL

class LoginPage(BasePage):
    """登入頁面的物件模型，繼承自 BasePage"""

    # 🎯 網頁元件的定位點 (Selectors)
    # 如果以後前端改了 HTML，只要改這裡就好
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"# 用來抓取登入失敗時的錯誤訊息

    def open_page(self):
        """動作：打開登入網頁"""
        self.navigate(BASE_URL)

    def login_as(self, username: str, password: str):
        """動作：一氣呵成輸入帳密並點擊登入"""
        self.fill_text(self.USERNAME_INPUT, username, "帳號輸入框")
        self.fill_text(self.PASSWORD_INPUT, password, "密碼輸入框")
        self.click(self.LOGIN_BUTTON, "登入按鈕")

    def get_error_message(self) -> str:
        """動作：取得登入失敗的錯誤提示文字"""
        return self.get_text(self.ERROR_MESSAGE)