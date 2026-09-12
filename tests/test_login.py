import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
import config

def test_successful_login(page: Page):
    """測試案例 1：使用正確的帳密應該要成功登入"""
    login_page = LoginPage(page)
    
    # 步驟：打開網頁 -> 輸入正確帳密登入
    login_page.open_page()
    login_page.login_as(config.TEST_USER, config.TEST_PASSWORD)
    
    # 斷言（驗收）：成功登入後，網址應該要包含 "/inventory.html" (商品頁)
    assert "/inventory.html" in page.url

def test_failed_login(page: Page):
    """測試案例 2：使用錯誤的密碼應該要登入失敗並顯示錯誤訊息"""
    login_page = LoginPage(page)
    
    # 步驟：打開網頁 -> 輸入正確帳號 + 錯誤密碼
    login_page.open_page()
    login_page.login_as(config.TEST_USER, "wrong_password")
    
    # 斷言（驗收）：只要錯誤訊息裡面包含 "do not match" 就算通過！
    error_msg = login_page.get_error_message()
    assert "do not match" in error_msg