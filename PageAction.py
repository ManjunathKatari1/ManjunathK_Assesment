from ManjunathKAssesment.PageObject import testObj
import string
from selenium import webdriver
import time

class action(object):
    def __init__(self,webdriver):
        self.driver=webdriver
        
    def url(self,webdriver):
        try:
            page = testObj(webdriver)
            
            page.openUrl()
            print("Page initiated")
            
            page.VerifyTile()
            print("Title verified")
            
            page.VerifyContent()
            print("Content verified")
            
            page.VerifyTable()
            print("Table verified")
            
            row_upper="1"
            row_lower="1"
            col_upper="1"
            col_lower="1"
#             print("Enter upper row value of cell/cells")
#             row_upper=input()
#             print("Enter lower row value of cell/cells")
#             row_lower=input()
#             print("Enter upper col value of cell/cells")
#             col_upper=input()
#             print("Enter lower col value of cell/cells")
#             col_lower=input()

            page.VerifyTableCell(row_upper,row_lower,col_upper,col_lower)
            print("Cells verified")
            
            page.VerifyImage()
            print("Image verified")
            
            page.VerifyFooter()
            print("Footer verified")
            
            page.ClickBlueButton()
            print("Blue Button verified")
            
            page.ClickRedButton()
            print("red Button verified")
            
            page.ClickGreenButton()
            print("green Button verified")
            
#             print("Enter row of edit button")
#             editRowNo=input()
            editRowNo="2"
            page.ClickEditButton(editRowNo)
            print("edit Button verified")
            
#             print("Enter row of delete button")
#             deleteRowNo=input()
            deleteRowNo="3"            
            page.ClickDeleteButton(deleteRowNo)
            print("delete Button verified")
            
            print("Test - Passed")
            
        except Exception as e:
            print("Test - Failed")
            raise e

obj = action(webdriver)
obj.url(webdriver)

time.sleep(100)

