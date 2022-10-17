import pytest
import pytest_check as validate
import os
from dotenv import load_dotenv
from pajeObjects.homePage import *

@pytest.fixture()
def test_setup(page):
    load_dotenv()
    base_url = os.getenv('base_url')
    page.goto(base_url)


@pytest.mark.usefixtures('test_setup')
def test_check_correct_page_loads(page):
    actTitle = get_homePage_title(page)
    if validate.equal(actTitle, os.getenv('homepagetitle')):
        print("The actual title of the page '" +actTitle+ "' does match with the expected title 'EaCodingTest1'")
    else:
        print("The actual title of the page '" +actTitle+ "' does match with the expected title 'EaCodingTest1'")


@pytest.mark.usefixtures('test_setup')
def test_check_festival_details_loads(page):
    innertext = page.inner_text('//*/ol/li[1]')
    noOffestivals = page.locator('//*/ol/li').count()
    if validate.greater(noOffestivals, 0):
        print("The page contains '" +str(noOffestivals)+ "' festival details which is greater than zero.")
    else:
        print("The page does not contain any festivals detail.")

@pytest.mark.usefixtures('test_setup')
def test_check_each_band_has_a_festival_associated(page):
    innertext = page.inner_text('//*/ol/li[1]')
    noOffestivals = page.locator('//*/ol/li').count()
    issueExist = False
    for x in range(1,noOffestivals+1):
        xpath = "//*/ol/li["+str(x)+"]/ul/li"
        innertext = page.inner_text(xpath)
        bandname = page.inner_text("//*/ol/li["+str(x)+"]")
        if validate.less_equal(len(innertext), 0):
            issueExist = True
            break

    if noOffestivals > 0:
        if validate.is_false(issueExist):
             print("The page contains band names for all festival details.")
             assert True
        if validate.is_true(issueExist):
            print("The page does not contain any festival details for band name '"+ bandname +"'.")
            assert False
    else:
        assert False
        print("The page does not contain any festivals detail.")


