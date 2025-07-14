from utils.visual_compare import compare_screenshots

def test_visual_homepage(browser):
    browser.save_screenshot("current_homepage.png")
    diff = compare_screenshots("baseline_homepage.png", "current_homepage.png")
    assert diff < 5