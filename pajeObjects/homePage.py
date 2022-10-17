

def get_homePage_title(page):
    actTitle = page.inner_text('//*/title')
    return actTitle