# Glance 工具

此工具用於執行和測試 `glance` 指令，並記錄執行過程中的輸出和錯誤。

## 功能

- 載入環境變數。
- 執行多個 `glance` 指令。
- 支援錯誤處理和日誌記錄。

## 使用方法

1. 確保已安裝 `glance` 並配置相關環境變數。
2. 執行 `main.py` 以測試和執行 `glance` 指令。

```bash
./.venv/Scripts/activate
uv pip install -r .\pyproject.toml
uv run main.py
```

## 配置

- 預設執行參數定義於 `RUN_ARG`。
- 可修改 `main` 函數中的 `args` 參數以自定義執行的 `glance` 指令。

## 範例

以下為預設執行的指令：

1. 輸出真實配置至 `glance.t.yml`：

   ```bash
   glance config:print>glance.t.yml
   ```

2. 驗證配置：

   ```bash
   glance config:validate
   ```

3. 執行並記錄輸出至 `glance.log`：

   ```bash
   glance >glance.log
   ```

## 錯誤處理

- 若執行指令失敗，會拋出自定義的 `GlanceError` 並記錄錯誤。
- 支援 `KeyboardInterrupt` 中斷執行。

## 日誌

- 日誌檔案位於 `main.log`，記錄執行過程中的詳細資訊。
