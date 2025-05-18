# 進入當前腳本所在目錄
Set-Location $PSScriptRoot

# 激活虛擬環境
& .\.venv\Scripts\Activate.ps1

# 安裝依賴（可選，如果需要的話請取消註釋）
# uv pip install -r .\pyproject.toml

# 運行主程式
uv run main.py
