# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected output:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = " - Buy milk\n"
download_games = " - Download games"
todo_text = "My todo:" + "\n" + todoText + download_games + "\n" + " - Diablio".center(len(download_games))

print(todo_text)