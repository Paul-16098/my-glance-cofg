# -*- coding: utf-8 -*-
import locale
import dotenv
import os
import subprocess
import paul_tools

# 預設的執行參數
RUN_ARG = ">glance.log"

# 獲取當前檔案的目錄路徑
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

# 主日誌檔案的路徑
MAIN_LOG_PATH = os.path.join(CURRENT_DIR, "main.log")


class GlanceError(Exception):
    """自定義的 Glance 錯誤異常類別"""

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.args}"


def initialize_logger():
    """初始化日誌記錄器"""
    logger = paul_tools.logger_init()
    logger.debug("logger init start")
    if os.path.exists(MAIN_LOG_PATH):
        os.remove(MAIN_LOG_PATH)  # 如果主日誌檔案存在，則刪除
        logger.debug(f"{MAIN_LOG_PATH} removed")
    logger.add(MAIN_LOG_PATH, level="DEBUG")  # 添加主日誌檔案
    logger.debug("logger init done")
    return logger


def load_environment_variables(logger):
    """載入環境變數"""
    dotenv.load_dotenv()
    logger.debug("dotenv load done")


def log_subprocess_output(logger, process):
    """記錄子進程的輸出"""
    logger.debug(f" return code: {process.returncode}")
    logger.debug(
        f"stdout: {process.stdout.decode(encoding=locale.getpreferredencoding()) if process.stdout else None}"
    )
    logger.debug(
        f"stderr: {process.stderr.decode(encoding=locale.getpreferredencoding()) if process.stderr else None}"
    )


def run(arg: str, logger, current_dir: str = CURRENT_DIR):
    """
    執行 glance 指令並記錄輸出。

    :param arg: glance 的參數
    :param current_dir: 執行指令的目錄
    :param logger: 日誌記錄器
    """
    logger.debug(f"running glance with arg: `{arg}`")
    process = subprocess.run(
        f"glance {arg}", shell=True, cwd=current_dir, capture_output=True
    )
    log_subprocess_output(logger, process)
    if process.returncode != 0:
        raise GlanceError(f"glance {arg} failed: {process.returncode}")
    logger.debug(f"finished processing arg: `{arg}`")


def main(
    # glance 的參數
    args: tuple[str, ...] = (
        # 輸出真實配置
        "config:print>glance.t.yml",
        # diagnose web
        # "diagnose",
        # test env
        "config:validate",
        # 執行
        RUN_ARG,
    ),
):
    """
    執行並測試 glance。

    :param args: glance 的參數
    :type args: tuple[str, ...]
    """
    logger = initialize_logger()
    load_environment_variables(logger)

    logger.debug(f"current dir: {CURRENT_DIR}")
    logger.debug(f"args: {args}")
    glance_file_path = os.path.join(CURRENT_DIR, "glance.t.yml")
    if os.path.exists(glance_file_path):
        os.remove(glance_file_path)

    for arg in args:
        try:
            run(arg, logger=logger)
        except KeyboardInterrupt:
            if arg == RUN_ARG:
                # 如果是執行參數，重新載入
                logger.info("\r---- reload ----\n")
                run(RUN_ARG, logger=logger)
            else:
                # 如果不是執行參數，則中止
                logger.info("\r---- abort ----\n")
                break
        except GlanceError as e:
            logger.error(e)  # 記錄自定義錯誤
            exit(1)
        except Exception as e:
            logger.error(f"Exception: {e}({e.args})")  # 記錄其他異常
            exit(1)
    exit(0)  # 正常結束


if __name__ == "__main__":
    main()  # 執行主函數
