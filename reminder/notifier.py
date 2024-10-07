import requests
import os
import time

class TelegramNotifier:
    def __init__(self, token='your_token', chat_id='destination_chat_id'):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def get_username(self):
        # 获取当前用户名
        try:
            username = os.getlogin()
            return username
        except Exception as e:
            print(f"Error getting username: {e}")
            return "Unknown User"
    
    def get_current_filename(self):
        # 获取当前文件的名称
        try:
            current_file_name = os.path.basename(__file__)
            return current_file_name
        except Exception as e:
            print(f"Error getting filename: {e}")
            return "Unknown File"

    def send_message(self, message):
        try:
            # 获取当前用户名
            username = self.get_username()

            # 获取当前时间
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # 获取当前文件名
            current_file_name = self.get_current_filename()

            # 格式化要发送的消息，包含自定义信息、用户名、文件名和发送时间
            full_message = f"{message}\n\n用户名: {username}\n文件名: {current_file_name}\n发送时间: {current_time}"

            payload = {
                'chat_id': self.chat_id,
                'text': full_message
            }
            response = requests.post(self.api_url, data=payload)

            if response.status_code == 200:
                print("Message sent successfully!")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
	# 使用默认的 Telegram Token 和 Chat ID
	notifier = TelegramNotifier()

	# 用户输入自定义消息
	user_message = "test"

	# 调用 send_message 方法发送消息
	notifier.send_message(user_message)
