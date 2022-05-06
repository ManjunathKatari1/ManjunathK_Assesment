import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.select import Select
import random
import string
# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
import json

class testObj(object):
    delay = 90 # secs 
    titlePath="//h3[contains(.,'Challenging DOM')]"
    contentPath="/html/body/div[2]/div/div/p"
    ExpectedContentText="The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element."
    tablePath="/html/body/div[2]/div/div/div/div/div[2]"
    tableHeaderPath="//html/body/div[2]/div/div/div/div/div[2]/table/thead/tr/th["
    ExpectedHeaderContentText=["","Lorem","Ipsum","Dolor","Sit","Amet","Diceret","Action"]
    tablecontentPath="//html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr["
    TableContentText=["","Iuvaret","Apeirian","Adipisci","Definiebas","Consequuntur","Phaedrum","edit delete"]
    imagePath="//canvas[@id='canvas']"
    footerPath="//div[contains(.,'Powered by Elemental Selenium')]"
    buttonsPath="//div[@class='large-2 columns']"
    blueButtonsPath="//a[@class='button']"
    redButtonsPath="//a[@class='button alert']"
    greenButtonsPath="//a[@class='button success']"
    editButtonPath="//html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr["
    deleteButtonPath="/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr["
    
    def __init__(self,webdriver):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def openUrl(self):
        try:
            self.driver.get('https://the-internet.herokuapp.com/challenging_dom')
            time.sleep(5)
            print ("URL loaded")
        except Exception as e:
            print('URL not loaded')
            raise e
    
    def VerifyTile(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.titlePath)))        
            print('Title verified')          
        except Exception as e:
            print('Title not verified')
            raise e
    
    def VerifyContent(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.contentPath)))        
            print('Content Available')
            actualContentText=(self.driver.find_element_by_xpath(self.contentPath)).text
            if(self.ExpectedContentText==actualContentText):
                print("Content is:",actualContentText)
            else:
                print("Content not verified and it is:",actualContentText, "but expected",self.ExpectedContentText )
                raise Exception
            
        except Exception as e:
            print('Content not verified')
            raise e
    
    def VerifyTable(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.tablePath)))        
            print('Table Available')
            
            for x in range(1, 8):
                y=str(x)
                headercontent=self.tableHeaderPath+""+y+"]"
                actualHeaderContentText=(self.driver.find_element_by_xpath(headercontent)).text
                
                if(self.ExpectedHeaderContentText[x]==actualHeaderContentText):
                    print("Table Header Content at ",x," is:",actualHeaderContentText)
                else:
                    print("Table Header Content not verified at ",x," and it is:",actualHeaderContentText, " but expected",self.ExpectedHeaderContentText[x] )
                    raise Exception
                
            for i in range(1, 11):
                p=str(i)
                r=str(i-1)
                for j in range(1, 8):
                    q=str(j)
                    tablecontent=self.tablecontentPath+""+p+"]/td["+q+"]"
                    actualTableContentText=(self.driver.find_element_by_xpath(tablecontent)).text
                    if(j<7):
                        ExpectedTableContentText=self.TableContentText[j]+""+r+""
                    else:
                        ExpectedTableContentText=self.TableContentText[j]
                    
                    if(ExpectedTableContentText==actualTableContentText):
                        print("Table Content at ",i,",",j," is:",actualTableContentText)
                    else:
                        print("Table Header Content not verified at ",i,",",j," and it is:",actualTableContentText, " but expected",ExpectedTableContentText )
                        raise Exception
                
            print('Table  verified')
        except Exception as e:
            print('Table not verified')
            raise e
    
    def VerifyTableCell(self,row_upper,row_lower,col_upper,col_lower):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.tablePath)))        
            print('Table Available')
            
            for x in range(1, 8):
                y=str(x)
                headercontent=self.tableHeaderPath+""+y+"]"
                actualHeaderContentText=(self.driver.find_element_by_xpath(headercontent)).text
                
                if(self.ExpectedHeaderContentText[x]==actualHeaderContentText):
                    print("Table Header Content at ",x," is:",actualHeaderContentText)
                else:
                    print("Table Header Content not verified at ",x," and it is:",actualHeaderContentText, " but expected",self.ExpectedHeaderContentText[x] )
                    raise Exception
            
            row_upper=int(row_upper) + 1
            row_lower=int(row_lower)
            col_upper=int(col_upper) + 1
            col_lower=int(col_lower)
            
            if((row_upper<row_lower)):
                print("row upper value is less than row lower")
                raise Exception
            elif((col_upper<col_lower)):
                print("col upper value is less than col lower")
                raise Exception
            
            for i in range(row_lower, row_upper):
                p=str(i)
                r=str(i-1)
                for j in range(col_lower, col_upper):
                    q=str(j)
                    tablecontent=self.tablecontentPath+""+p+"]/td["+q+"]"
                    actualTableContentText=(self.driver.find_element_by_xpath(tablecontent)).text
                    if(j<7):
                        ExpectedTableContentText=self.TableContentText[j]+""+r+""
                    else:
                        ExpectedTableContentText=self.TableContentText[j]
                    
                    if(ExpectedTableContentText==actualTableContentText):
                        print("Cells Content at ",i,",",j," is:",actualTableContentText)
                    else:
                        print("Cells Header Content not verified at ",i,",",j," and it is:",actualTableContentText, " but expected",ExpectedTableContentText )
                        raise Exception
                
            print('Cells  verified')
        except Exception as e:
            print('Cells not verified')
            raise e
    
    def VerifyImage(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.imagePath)))        
            print('Image verified')          
        except Exception as e:
            print('Image not verified')
            raise e
    
    def VerifyFooter(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.footerPath)))        
            print('Footer verified')          
        except Exception as e:
            print('Footer not verified')
            raise e
    
    def ClickBlueButton(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.buttonsPath)))        
            print('Buttons available')
            self.driver.find_element_by_xpath(self.blueButtonsPath).click()
            time.sleep(5)
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.buttonsPath)))        
            print('Blue Button verified')
        except Exception as e:
            print('Blue Button not verified')
            raise e
    
    def ClickRedButton(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.buttonsPath)))        
            print('Buttons available')
            self.driver.find_element_by_xpath(self.redButtonsPath).click()
            time.sleep(5)
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.buttonsPath)))        
            print('red Button verified')
        except Exception as e:
            print('red Button not verified')
            raise e
    
    def ClickGreenButton(self):
        try:
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.buttonsPath)))        
            print('Buttons available')
            self.driver.find_element_by_xpath(self.greenButtonsPath).click()
            time.sleep(5)
            WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH,self.buttonsPath)))        
            print('green Button verified')
        except Exception as e:
            print('green Button not verified')
            raise e
    
    def ClickEditButton(self,editRowNo):
        try:
            editRowNo=str(editRowNo)
            editButPath=self.editButtonPath + "" +editRowNo+ "]/td[7]/a[1]"
            self.driver.find_element_by_xpath(editButPath).click()
            time.sleep(2)
            url=self.driver.current_url
            if (url== "https://the-internet.herokuapp.com/challenging_dom#edit") :
                print('edit Button clicked for row', editRowNo)
            
            print('edit Button verified')
        except Exception as e:
            print('edit Button not verified')
            raise e
    
    def ClickDeleteButton(self,deleteRowNo):
        try:
            deleteRowNo=str(deleteRowNo)
            deleteButPath=self.deleteButtonPath + "" +deleteRowNo+ "]/td[7]/a[2]"
            self.driver.find_element_by_xpath(deleteButPath).click()
            time.sleep(2)
            url=self.driver.current_url
            if (url== "https://the-internet.herokuapp.com/challenging_dom#delete") :
                print('edit Button clicked for row', deleteRowNo)
            
            print('edit Button verified')
        except Exception as e:
            print('edit Button not verified')
            raise e
        
    