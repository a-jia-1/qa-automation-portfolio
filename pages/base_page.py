import logging
from playwright.sync_api import Page

# 呼叫我們之前設定好的日誌系統
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        """初始化時，把 Playwright 的瀏覽器頁面（page）傳進來"""
        self.page = page

    def navigate(self, url: str):
        """封裝：前往特定網址"""
        logger.info(f"🌐 正在導航至網頁: {url}")
        self.page.goto(url)

    def click(self, selector: str, element_name: str = "元素"):
        """封裝：點擊元件"""
        logger.info(f"🖱️ 點擊【{element_name}】 -> 位置: {selector}")
        self.page.click(selector)

    def fill_text(self, selector: str, text: str, element_name: str = "輸入框"):
        """封裝：在輸入框打字"""
        # 如果是密碼，Log 裡面我們用 *** 遮蔽，保護資安
        log_text = "********" if "password" in selector.lower() or "password" in element_name.lower() else text
        logger.info(f"⌨️ 在【{element_name}】輸入: {log_text} -> 位置: {selector}")
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """封裝：取得網頁上的文字（用來做驗收/斷言）"""
        text = self.page.text_content(selector)
        return text.strip() if text else ""