import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# 1. 讀取 .env 檔案
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TEST_USER = os.getenv("TEST_USER")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

# 2. 🔥 高級加分項 2：初始化專業日誌設定
# 建立一個叫做 logs 的資料夾來放紀錄檔
os.makedirs("logs", exist_ok=True)
# 用今天的日期來命名 log 檔案，例如：test_run_20260912.log
log_filename = f"logs/test_run_{datetime.now().strftime('%Y%m%d')}.log"

# 設定 Log 的輸出格式（包含：時間、訊息等級、具體訊息、程式檔名與行數）
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)",
    handlers=[
        logging.FileHandler(log_filename, encoding="utf-8"), # 寫入檔案
        logging.StreamHandler()                              # 同時印在螢幕上
    ]
)

# 建立一個 logger 產生器，之後其他檔案都可以呼叫它
logger = logging.getLogger(__name__)

# 3. 測試日誌功能是否正常
logger.info("--- 系統初始化成功 ---")
logger.info(f"環境變數載入完畢，目標網址: {BASE_URL}")