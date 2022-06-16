from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Config:

    @staticmethod
    def webdriver_chrome():
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @staticmethod
    def webdriver_firefox():
        driver = webdriver.Firefox(service=Service("C:/geckodriver.exe"))
        return driver

    @staticmethod
    def webdriver_opera():
        from selenium import webdriver
        from webdriver_manager.opera import OperaDriverManager

        options = webdriver.ChromeOptions()
        options.add_argument('allow-elevated-browser')
        options.binary_location = "C:\\Users\\pedro\\AppData\\Local\\Programs\\Opera\\launcher.exe"
        return webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)

    @staticmethod
    def webdriver_ie():
        from selenium import webdriver
        from selenium.webdriver.ie.service import Service
        from webdriver_manager.microsoft import IEDriverManager

        return webdriver.Ie(service=Service(IEDriverManager().install()))

    @staticmethod
    def webdriver_chromium():
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.core.utils import ChromeType
        return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    @staticmethod
    def webdriver_brave():
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.core.utils import ChromeType
        return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

    @staticmethod
    def webdriver_edge():
        from selenium import webdriver
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    @staticmethod
    def webdriver_ie():
        from selenium import webdriver
        from selenium.webdriver.ie.service import Service
        from webdriver_manager.microsoft import IEDriverManager

        return webdriver.Ie(service=Service(IEDriverManager().install()))
