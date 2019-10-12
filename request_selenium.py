#coding=utf8
import requests,time,unittest,HTMLTestRunner
from yaml_jk import ya
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import ddt
@ddt.ddt
class A(unittest.TestCase):
    def __init__(self,methodName='runTest', param=None):
        super(A,self).__init__(methodName)
        self.param=param


    @ddt.data(*ya)
    #@ddt.file_data('config.yaml')
    @ddt.unpack
    def test_b(self,**y):
        re=requests.request(method=y['method'],url=y['url'],params=y['data'])
        self.assertIn(y['result'],re.content)

    def test_c(self):
        self.assertTrue(4%2)
    def test_d(self):
        self.assertIn('a','bdAAAa')
    @staticmethod
    def parame(classname,param):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(classname)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(classname(name, param=param))
            return suite


if __name__=='__main__':
#    unittest.main()
    f=open('result.html','w')
    result=HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title=u"测试报告",description=u'第一份测试报告')
    #discover=unittest.defaultTestLoader.discover('sas')
    testcase=unittest.TestSuite()
    testcase=unittest.TestLoader().loadTestsFromTestCase(A)
    #testcase.addTest(A('test_b'))
    #result=unittest.TextTestRunner(verbosity=2)
    result.run(testcase)

# uite = unittest.TestSuite()
# suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=42))
# suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
# unittest.TextTestRunner(verbosity=2).run(suite)

    #f.close()
'''
wb=webdriver.Ie()
wb.implicitly_wait(5)
wb.get('https://www.baidu.com/')
s=wb.find_element_by_name('tj_settingicon')
time.sleep(2)
ActionChains(wb).move_to_element(s).perform()
wb.find_element_by_css_selector('.setpref').click()




header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}

re=requests.get('https://www.baidu.com',verify=False,headers=header)


print re.text   #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
print re.content  #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩

print re.apparent_encoding,re.encoding
print re.apparent_encod
print re.close()
print re.cookies
print re.elapsed.total_seconds()
print re.headers
print re.status_code,re.ok
print re.url,re.reason,re.links
print re.request.headers
print re.iter_content(),re.iter_lines().next()
print re.raw

print re.status_code
with open(r'D:\ww.jpg','ab+') as f:
    for i in re.iter_content():
        f.write(i)

driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.get('https://www.runoob.com/')
time.sleep(2)
driver.back()
time.sleep(1)
driver.forward()
driver.set_window_size(800,160)
time.sleep(1)
driver.maximize_window()


from selenium.webdriver.support import expected_conditions as EC
import unittest
class BolgHome(unittest.TestCase):
    u'博客首页'
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'E:\软件列表\Chrome64_48.0.2564.109\chromedriver.exe')
        url = "http://www.cnblogs.com/yoyoketang/"
        cls.driver.get(url)
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        u'验证元素存在：博客园'
        locator = ("id", "blog_nav_sitehome")
        text = u"博客园"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_02(self):
        u'验证元素存在：首页'
        locator = ("id", "blog_nav_myhome")
        text = u"首页"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
    '''