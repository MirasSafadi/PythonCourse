class Line:
    def __init__(self,words = []):
        self.words = words
    def number_of_words(self):
        return len(self.words)
    def __str__(self):
        s = ""
        for st in self.words:
            s += st
            s += " "
        s += "\n"
        return s
    def addWord(self,word):
        self.words.append(word)
    def removeWord(self,word):
        i = self.words.index(word)
        self.words.pop(i)
    def updateWord(self,newWord,oldWord):
        i = self.words.index(oldWord)
        self.words[i] = newWord


class Page:
    def __init__(self,lines = []):
        self.lines = lines
    def number_of_words_in_page(self):
        total = 0
        for line in self.lines:
            total += line.number_of_words()
        return total
    def __str__(self):
        st = ""
        for line in self.lines:
            st += line.__str__()
            st += "\n"
        return st
    def addLine(self,line):
        self.lines.append(line)
    def removeLine(self,line):
        i = self.lines.index(line)
        self.lines.pop(i)
    def updateLine(self,newLine,oldLine):
        i = self.lines.index(oldLine)
        self.lines[i] = newLine

class Book:
    def __init__(self,pages = []):
        self.pages = pages
    def number_of_words_in_book(self):
        sum = 0
        for page in pages:
            sum += page.number_of_words_in_page()
        return sum
    def __str__(self):
        st = ""
        for page in self.pages:
            st += page.__str__()
            st += "\n"
            st += "-----------------"
            st += "\n"
        return st
    def addPage(self,page):
        self.pages.append(page)
    def removePage(self,page):
        i = self.pages.index(page)
        self.pages.pop(i)
    def updatePage(self,newPage,oldPage):
        i = self.pages.index(oldPage)
        self.pages[i] = newPage

def main():
    st1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis"
    line1 = Line(st1.split(" "))
    st2 = "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu"
    line2 = Line(st2.split(" "))
    st3 = "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    line3 = Line(st3.split(" "))
    page1 = Page([line1,line2,line3])
    st4 = "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis"
    line4 = Line(st4.split(" "))
    st5 = "sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut"
    line5 = Line(st5.split(" "))
    st6 = "ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum."
    line6 = Line(st6.split(" "))
    page2 = Page([line4,line5,line6])
    st7 = "Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl"
    line7 = Line(st7.split(" "))
    st8 = "adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus"
    line8 = Line(st8.split(" "))
    st9 = "quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst."
    line9 = Line(st9.split(" "))
    page3 = Page([line7,line8,line9])
    book = Book([page1,page2,page3])
    print(book)


if __name__ == "__main__": main()