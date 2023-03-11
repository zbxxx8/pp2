disciplines = ['Statistics', 'PP2', 'Physics1', 'Calculus2', 'English2']
with open('2.txt', "w") as f:
        for i in disciplines:
                f.write(i+'\n')
content = open('2.txt')
print(content.read())
content.close()