from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Firefox()
driver.get("http://52.49.91.111:8036/word-soup-challenge")


def click(id):
    try:
        driver.find_element_by_id(id).click()
    except StaleElementReferenceException:
        click(id)


def solve_word_soup():
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, '0-0')))
    rows = driver.find_elements_by_tag_name('tr')
    height = len(rows)
    width = len(rows[0].find_elements_by_tag_name("td"))

    soup = [['' for _ in range(width)] for _ in range(height)]
    letters = {}
    for i, row in enumerate(rows):
        columns = row.find_elements_by_tag_name("td")
        for j, col in enumerate(columns):
            soup[i][j] = col.text
            if col.text in letters:
                s = letters[col.text]
                s.add((j, i))
            else:
                s = {(j, i)}
            letters[col.text] = s

    words_div = driver.find_element_by_id('words')
    words_div = words_div.find_elements_by_xpath("//*[contains(@id, 'word-')]")
    words = []
    for word in words_div:
        words.append(word.text)

    for word in words:
        w = list(word)
        br = False
        for initial_pos in letters[w[0]]:
            if br:
                break
            x, y = initial_pos
            for horizontal in [-1, 0, 1]:
                if br:
                    break
                for vertical in [-1, 0, 1]:
                    if br:
                        break
                    if horizontal != 0 or vertical != 0:
                        end_h = horizontal * (len(w) - 1) + x
                        end_v = vertical * (len(w) - 1) + y
                        if 0 <= end_h < width and 0 <= end_v < height:
                            correct = True
                            for inc in range(1, len(w)):
                                xx = x + inc * horizontal
                                yy = y + inc * vertical
                                if soup[yy][xx] != w[inc]:
                                    correct = False
                                    break
                            if correct:
                                br = True
                                click("{}-{}".format(x, y))
                                click("{}-{}".format(end_h, end_v))

solve_word_soup()
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'btn-level-2')))
driver.find_element_by_id('btn-level-2').click()
solve_word_soup()
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.TAG_NAME, 'p')))
for p in driver.find_elements_by_tag_name('p'):
    print(p.text)
driver.close()




