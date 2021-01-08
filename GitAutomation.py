import json
import os
import tkinter
from tkinter.filedialog import askopenfilename

from selenium import webdriver


class Git:
    def __init__(self):
        self.directory = ""
        self.repository_name = ""

    def create_rep_in_git(self):
        driver = webdriver.Edge('/Users/Mohamed/Downloads/msedgedriver')
        data = json.load(open('D:\passwords.json'))
        password = data['github_password']
        username = data['github_username']
        driver.get('https://github.com/login')
        while True:
            try:
                driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]').send_keys(username)
                driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[3]').send_keys(password)
                driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[14]').click()
                break
            except:
                pass
        while True:
            try:
                driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a').click()
                break
            except:
                pass
        while True:
            try:
                driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input').send_keys(
                    self.repository_name)
                driver.find_element_by_xpath(
                    '/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]').click()
                driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').submit()
                driver.quit()
                break
            except:
                pass

    def cmd_upload_to_rep(self):
        url = 'https://github.com/Alimohamad21/{}.git'.format(self.repository_name)
        cmd2 = 'git remote add origin {}'.format(url)
        os.chdir(self.directory)
        os.system(
            'cmd /c "git init&git add .&git commit -m "First commit"&git branch -M main&{}&git push -f origin main"'.format(
                cmd2))

    def update_existing_repository(self):
        commit_name = input('Please enter a short description for your commit:')
        os.chdir(self.directory)
        os.system(
            'cmd /c "git add .&git commit -m "{}"&git push origin main"'.format(
                commit_name))

    def new_repository(self):
        self.repository_name = input('Please enter a name for your repo:')
        self.repository_name = self.repository_name.replace(' ', '-')
        self.create_rep_in_git()
        self.cmd_upload_to_rep()


choice = input('1-New Repository\n2-Existing Repository\nPlease choose an option form the above:')
root = tkinter.Tk()
root.withdraw()
git = Git()
git.directory = tkinter.filedialog.askdirectory()
if choice == '1':
    git.new_repository()
if choice == '2':
    git.update_existing_repository()
input('Press any button to exit')
