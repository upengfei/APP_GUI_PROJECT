# coding:utf-8

import time,os
from macaca import WebElement,WebDriver,WebDriverException
from lib import read_conf,get_root_path
from functools import wraps
from lib import logger

flag="IMAGE:"


class BasicFE(object):
    """对常用的一些基本功能的扩展"""

    def get_driver(self):
        return self.driver

    @classmethod
    def set_driver(cls, dri):
        if isinstance(dri, WebDriver):
            cls.driver = dri
        else:
            raise WebDriverException("driver error")

    def _get_window_size(self):
        window = self.driver.get_window_size()
        y = window['height']
        x = window['width']

        return x, y

    @staticmethod
    def _get_element_size(element):
        if not isinstance(element,WebElement): raise Exception("element error!")
        rect = element.rect

        x_center = rect['x'] + rect['width'] / 2
        y_center = rect['y'] + rect['height'] / 2
        x_left = rect['x']
        y_up = rect['y']
        x_right = rect['x'] + rect['width']
        y_down = rect['y'] + rect['height']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def _swipe(self, fromX, fromY, toX, toY, steps):
        self.driver \
            .touch('drag', {'fromX': fromX, 'fromY': fromY, 'toX': toX, 'toY': toY, 'steps': steps})

    def swipe_up(self, element=None, steps=10):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.25 * y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_down(self, element=None, steps=10):
        """
        swipe down
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.75 * y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_left(self, element=None, steps=10):
        """
        swipe left
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.25 * x
            toY = 0.5 * y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_right(self, element=None, steps=10):
        """
        swipe right
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_right
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.75 * x
            toY = 0.5 * y

        self._swipe(fromX, fromY, toX, toY, steps)


def clean_dir(path):
    """清空目录"""
    if os.listdir(path):
        for item in os.listdir(path):
            file_path = os.path.join(path,item)
            if file_path:
              os.remove(file_path)


def _screenshots(name):
    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screenshot = name + '-' + date_time + '.png'
    image_dir_path = get_root_path() + os.sep + 'report'+ os.sep+'image'
    clean_dir(image_dir_path)
    imagePath = image_dir_path +os.sep+ screenshot
    print imagePath
    driver = BasicFE().get_driver()
    driver.save_screenshot(imagePath)
    return screenshot


def testInfo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info('\t--> %s', func.__name__)
            ret = func(*args, **kwargs)
            logger.info('<-- %s, %s\n', func.__name__, '测试通过')
            return ret
        except WebDriverException as e:
            logger.error('WebDriverException, %s', e)
            logger.error('\t<-- %s, %s, %s', func.__name__, 'WebDriverException', 'Error')

            if flag in str(e):
                raise WebDriverException(message=e)
            else:
                print e
                raise WebDriverException(message="Eorror:"+str(e)+"\n截图如下： "+flag + _screenshots(func.__name__))
        except AssertionError as e:
            logger.error('AssertionError, %s', e)
            logger.error('\t<-- %s, %s, %s', func.__name__, 'AssertionError', 'Error')

            if flag in str(e):
                raise AssertionError(e)
            else:
                print e
                raise AssertionError("Eorror:"+str(e)+"\n截图如下： "+flag + _screenshots(func.__name__))
        except Exception as e:
            logger.error('Exception, %s', e)
            print e
            logger.error('\t<-- %s, %s, %s', func.__name__, 'Exception', 'Error')

            if flag in str(e):

                raise "Eorror:"+str(e)
            else:
                print e
                raise Exception("Eorror:"+str(e)+"\n截图如下： "+flag + _screenshots(func.__name__))
    return wrapper


def app_init():
    try:
        rc = read_conf('AppConf.ini')
        desired_caps= {
            "platformName": '%s' % rc.get("Android", 'platformName'),
            "app":"%s" % rc.get("Android", 'app'),
            "reuse":"%s" % rc.get("Android", 'reuse'),
            "udid":"%s" % rc.get("Android", 'udid'),
        }
        print desired_caps
        driver = WebDriver(desired_caps)
        BasicFE.set_driver(driver)
        driver.init()
        return driver
    except Exception as e:
        raise "error:"+str(e)