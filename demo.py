#
#
# # while True:
# #     try:
# #         driver.find_element_by_path("//*[@text='关于手机']").click()
# #         break
# #     except Exception as e:
# #         driver.swipe(100, 2000, 100, 1000)
# from appium import webdriver
#
#
# class init_driver():
#     desired_caps = dict()
#     desired_caps['platformName'] = 'Android'
#     desired_caps['platformVersion'] = '5.1'
#     desired_caps['deviceName'] = '192.168.2.101:5555'
#     desired_caps['appPackage'] = 'com.yunmall.lc'
#     desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
#
#     # page_source = ""
#     # while True:
#     #     try:
#     #         driver.find_element_by_xpath("//*@text='关于手机123'").click()
#     #     except Exception:
#     #         #屏幕宽高
#     #         width = driver.get_window_size()["width"]
#     #         height = driver.get_window_size()["height"]
#     #         #滑动小一点
#     #         bottom_x  = width / 2
#     #         bottom_y = height / 4 * 3
#     #         top_x = width / 2
#     #         top_y = height / 4 * 1
#     #         # driver.swipe(100, 2000, 100, 1000)
#     #         driver.swipe(bottom_x,bottom_y,top_x,top_y,3000)
#     #         if driver.page_source == page_source:
#     #             print("我是有底线的")
#     #             break
#     #         page_source = driver.page_source
#
#     def scroll_to_feature(feature,direction="up"):
#         """
#         边滑边找关于手机选项
#         :param direction:方向
#         "up":往上滑
#         "down":往下滑
#         "left":往左滑
#         "right":往右滑
#         :return:
#         """
#         page_source = ""
#         while True:
#             try:
#                 driver.find_element(*feature).click()
#                 break
#             except Exception:
#                 #屏幕宽高
#                 width = driver.get_window_size()["width"]
#                 height = driver.get_window_size()["height"]
#                 #滑动小一点
#
#                 center_x = width / 2
#                 center_y = height / 2
#
#                 left_x = width / 4 * 1
#                 left_y = center_y
#
#                 right_x = width / 4 * 3
#                 right_y = center_y
#
#                 bottom_x  = center_x
#                 bottom_y = height / 4 * 3
#                 top_x = center_x
#                 top_y = height / 4 * 1
#
#                 if direction == "up":
#                     driver.swipre(bottom_x,bottom_y,top_x,top_y,3000)
#                 if direction == "down":
#                     driver.swipre(top_x,top_y,bottom_x,bottom_y,3000)
#                 if direction == "left":
#                     driver.swipre(right_x,right_y,left_x,left_y,3000)
#                 if direction == "right":
#                     driver.swipre(left_x,left_y,right_x,right_y,3000)
#                 else:
#                     raise Exception("参数错误")
#                 # driver.swipe(100, 2000, 100, 1000)
#                 if driver.page_source == page_source:
#                     print("我是有底线的")
#                     break
#                 page_source = driver.page_source
#
#
# def scroll_page_one_time(direction="up")
#     """
#     滑动一次
#     :param direction:方向
#     "up":往上滑
#     "down":往下滑
#     "left":往左滑
#     "right":往右滑
#     :return:
#     """
#     width = driver.get_window_size()["width"]
#     height = driver.get_window_size()["height"]
#     # 滑动小一点
#
#     center_x = width / 2
#     center_y = height / 2
#
#     left_x = width / 4 * 1
#     left_y = center_y
#
#     right_x = width / 4 * 3
#     right_y = center_y
#
#     bottom_x = center_x
#     bottom_y = height / 4 * 3
#     top_x = center_x
#     top_y = height / 4 * 1
#
#     if direction == "up":
#         driver.swipre(bottom_x, bottom_y, top_x, top_y, 3000)
#     if direction == "down":
#         driver.swipre(top_x, top_y, bottom_x, bottom_y, 3000)
#     if direction == "left":
#         driver.swipre(right_x, right_y, left_x, left_y, 3000)
#     if direction == "right":
#         driver.swipre(left_x, left_y, right_x, right_y, 3000)
#     else:
#         raise Exception("参数错误")
#
# def scroll_to_feature(feature,direction="up")
#     """
#     边滑边找某个元素的特征
#     :param feature:元素的特征
#     :param direction:方向
#         "up"：从下往上
#         "down"：从上往下
#         "left"：从右往左
#         "down"：从左往右
#     :return:
#     """
#     page_source = ""
#     while True:
#         try:
#             driver.find_element(*feature).click()
#             break
#         except Exception:
#
#             scroll_page_one_time(direction)
#
#             if driver.page_source == page_source:
#                 print("我是有底线的")
#                 break
#             page_source = driver.page_source
#
# scroll_to_feature((By.XPATH, "//*[@text='关于手机']"))
#
#
#
#
# def find_element_with_scroll(feature,direction="up")
#     """
#     边滑边找某个元素的特征
#     :param feature:元素的特征
#     :param direction:方向
#         "up"：从下往上
#         "down"：从上往下
#         "left"：从右往左
#         "down"：从左往右
#     :return:
#     """
#     page_source = ""
#     while True:
#         try:
#             return driver.find_element(*feature)
#             break
#         except Exception:
#
#             scroll_page_one_time(direction)
#
#             if driver.page_source == page_source:
#                 print("我是有底线的")
#                 break
#             page_source = driver.page_source
#             #使用
# find_element_with_scroll((By.XPATH, "//*[@text='关于手机']")).click()
#
#
#
#
#
