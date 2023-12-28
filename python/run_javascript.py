import webview
 
URL = 'https://example.com/'
 
def run():
    window = webview.create_window('PythonからJavaScriptを実行する', url=URL, height=400)
    webview.start()