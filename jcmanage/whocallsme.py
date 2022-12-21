# Library/program whocallsme.py. Get a score from whocallsme.com
# Copyright (C) 2014 David Brown
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class whocallsme:
    """
    This tries to grade a caller based on information found on WhoCallsMe.com
    TODO move to beautifulsoup library instead of selenium
    """

    def __init__(self):
        self.browser = None
        self.site = "http://whocallsme.com/nb/search.aspx?q="
        self.site2 = "http://whocallsme.com/Phone-Number.aspx/"

    def getScore(self, number):
        returnme = "0"
        try:
            # chrome doesn't quit?
            # if os.path.exists("/Applications/Google Chrome.app"):
            #    self.browser = webdriver.Chrome()
            # os.path.exists("/Applications/Firefox.app"):
            # self.browser = webdriver.Firefox()
            # else:
            #    self.browser = webdriver.Safari()
            self.browser = webdriver.Firefox()

            # self.browser.get( self.site  + number)
            self.browser.get(self.site2 + number)

            try:
                # use this to get numbers from front page
                # phones = self.browser.find_elements_by_css_selector('a.oos_previewTitle')
                # detail page, count of comments:
                returnme = str(
                    len(
                        self.browser.find_elements_by_css_selector(
                            "li.oos_postListItem"
                        )
                    )
                )
                # returnme = self.browser.find_elements_by_id('resInfo-1')[0].text.split()[1]

            except NoSuchElementException:
                assert 0, "Can't find listings"
        except:
            print("Couldn't get a proper response.")
        time.sleep(5)
        self.browser.close()
        self.browser.quit()
        return returnme

    def report(
        self, number, dateString="", callerString="", guessedName="", zipcode=""
    ):
        pass


if __name__ == "__main__":
    wc = whocallsme()
    import sys

    score = wc.getScore(sys.argv[1])
    print(score)
